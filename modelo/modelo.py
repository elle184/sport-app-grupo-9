# models.py
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel

class Event(BaseModel):
 id: Optional[UUID]=uuid4()
 name_event: str
 description_event: str
 state_event: int
