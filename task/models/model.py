import datetime

from sqlalchemy import Column, Text, Integer, String, DateTime, func, Boolean, ForeignKey

from task.config.db import DB_BASE

# models
# Register model contain user infomation
class Register(DB_BASE):
    __tablename__ = 'register'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, default=False)
    email = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now())
    modified_on = Column(DateTime,onupdate=datetime.datetime.now)
    mobile_no = Column(String(255), nullable=False, default=False)
    password = Column(String(255), nullable=False, default=False)
    confirm_password = Column(String(255), nullable=False, default=False)
    address = Column(Text, nullable=True, default=None)

# Task model contain task infomation
class Task(DB_BASE):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    priority_level = Column(Integer, nullable=False,default=0)
    due_date = Column(DateTime, nullable=False,)
    created_at = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('user.id'))
    task_name = Column(String(255), nullable=False, default=False)

