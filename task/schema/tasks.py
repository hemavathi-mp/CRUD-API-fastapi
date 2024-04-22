from datetime import date
from typing import List, Optional

from pydantic import BaseModel

# schema
class register_form(BaseModel):
    mobile_no :int=None
    email :str=None
    name :str=None
    password :str=None
    confirm_password: str = None
    address: str = None

class task_info(BaseModel):
    priority_level :int=0
    due_date :date=None
    user_id: int = None
    task_name: str = None
