import datetime
import logging

from sqlalchemy import update, func, or_

from task.config.db import SessionLocal

from task.models.model import Register, Task


class form:

    def login(email_or_mobile_no, password):
        with SessionLocal() as session:
            print("d",type(email_or_mobile_no))

            query = session.query(Register).filter(or_(Register.email == email_or_mobile_no,Register.mobile_no == email_or_mobile_no), Register.password==password).all()
            if len(query) != 0:
                return {"Login Successfully"}
            else:
                return {"Please enter valid email_id/mobile_no or password"}

    def insert(params):
        data = params.dict()
        if data['password'] != data['confirm_password']:
            return {'Entered password does not match'}

        with SessionLocal() as session:
            result = Register(**data)
            session.add(result)
            session.commit()
            session.refresh(result)

            return {"message":"Registration successful","user_id":result.id}

    def edit(registration_id, data):
        with SessionLocal() as session:

            db_user = session.query(Register).get(registration_id)
            if not db_user:
                raise HTTPException(status_code=404, detail="User not found")

            stored_data = data.dict()
            stored_model = Task(**stored_data)
            update_data = data.dict(exclude_unset=True)
            updated_data = stored_model.copy(update=update_data)
            post = jsonable_encoder(updated_data)
            return {"User information updated succussfully"}

    def user_details(id):
        with SessionLocal() as session:
            db_user = session.query(Register).get(id)
            if not db_user:
                raise HTTPException(status_code=404, detail="User not found")

            return db_user

    def delete_user(id):
        with SessionLocal() as session:
            db_user= session.query(Register).get(id)
            if not db_user:
                raise HTTPException(status_code=404, detail="User not found")

            session.delete(db_user)
            session.commit()
            return {"ok": True}

    def add_task(info):
        data = info.dict()
        with SessionLocal() as session:
            query = session.query(Register).filter(Register.id==data['user_id']).all()
            if len(query) != 0:
                raise HTTPException(status_code=404, detail="User is not authorised person to add task")

            result = Task(**data)
            session.add(result)
            session.commit()
            session.refresh(result)

            return {"message":"Task added successfully","task_id":result.id}

    def task_edit(task_id, update_task):
        with SessionLocal() as session:

            db_task = session.query(Task).get(task_id)
            if not db_task:
                raise HTTPException(status_code=404, detail="Task not found")

            stored_data = update_task.dict()
            stored_model = Task(**stored_data)
            update_data = update_task.dict(exclude_unset=True)
            updated_data = stored_model.copy(update=update_data)
            post = jsonable_encoder(updated_data)

            return {"Task updated succussfully"}


    def task_details(id):
        with SessionLocal() as session:
            db_task = session.query(Register).get(id)
            if not db_task:
                raise HTTPException(status_code=404, detail="Task not found")

            return db_task

    def delete_task(task_id):
        with SessionLocal() as session:
            db_task = session.query(Task).get(task_id)
            if not db_task:
                raise HTTPException(status_code=404, detail="Task not found")

            session.delete(db_task)
            session.commit()
            return {"ok": True}









