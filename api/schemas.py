import datetime
from pydantic import BaseModel


class B(BaseModel):
    id: int
    a_id: int
    data: str


class A(BaseModel):
    id: int
    data: str
    create_date: datetime.datetime
    bs: list[B] = []

    class Config:
        orm_mode = True
