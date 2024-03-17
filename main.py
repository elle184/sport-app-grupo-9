# main.py
from fastapi import FastAPI
from modelo import Event
from typing import List
app = FastAPI()
db:List[Event]=[]
@app.get("/")
async def get_event():
    return db
 

@app.post("/api/v1/event")
async def create_event(event: Event):
 db.append(event)
 return {"id": event.id}


