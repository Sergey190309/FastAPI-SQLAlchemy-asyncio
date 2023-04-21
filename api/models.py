import datetime
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import func

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class A(Base):
    __tablename__ = "a"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[str] = mapped_column(unique=True)
    create_date: Mapped[datetime.datetime] = mapped_column(
        server_default=func.now())
    bs: Mapped[List['B']] = relationship(lazy="raise")


class B(Base):
    __tablename__ = "b"
    id: Mapped[int] = mapped_column(primary_key=True)
    a_id: Mapped[int] = mapped_column(ForeignKey("a.id"))
    data: Mapped[str]
