import logging

from fastapi import APIRouter, Request, Depends

from task.controller.task_controller import form
from task.schema.tasks import register_form, task_info

router = APIRouter(
    prefix='/new_task',
    tags=["new_task API's"],
)

# login api
@router.post('/login')
def login(email_or_mobile_no:str, password:str):
    result = form.login(email_or_mobile_no, password)
    return {"success": "OK", "message": "Login Form", "data": result}

# Registration form: Add user details
@router.post('/add')
async def add(data: register_form):
    result = form.insert(data)
    return {"success": "OK", "message": "Registration Form", "data": result}

# Edit User Information
@router.patch('/update_user/{registration_id}')
async def edit(registration_id: int,data:register_form):
    result = form.edit(registration_id,data)
    return {"success": "OK", "message": "Data updated successfully", "data": result}

# Get single user information
@router.get('/user_details/{id}')
async def user_details(id:int):
    result = form.user_details(id)
    return {"success": "OK", "message": "User details", "data": result}

# Delete single user information
@app.delete("/user_delete/{user_id}")
def delete_user(user_id: int):
    result = form.delete_user(user_id)
    return {"success": "OK", "message": "User is successfully deleted", "data": result}


# Add/Insert Task
@router.post('/task')
async def task(info:task_info):
    result = form.add_task(info)
    return {"success": "OK", "message": "Task added successfully", "data": result}

# Edit Task Information
@router.patch('/update_task/{task_id}')
async def edit(task_id: int,update_task:task_info):
    result = form.task_edit(task_id,update_task)
    return {"success": "OK", "message": "Data updated successfully", "data": result}

# Get single task information
@router.get('/Task_details/{id}')
async def task_details(id:int):
    result = form.task_details(id)
    return {"success": "OK", "message": "Task details", "data": result}

# Delete single task information
@app.delete("/task_delete/{task_id}")
def delete_hero(task_id: int):
    result = form.delete_task(task_id)
    return {"success": "OK", "message": "Task is successfully deleted", "data": result}


