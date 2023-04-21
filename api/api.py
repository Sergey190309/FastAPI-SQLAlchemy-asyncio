# from __future__ import annotations

# import asyncio

from fastapi import FastAPI
# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import async_sessionmaker
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import selectinload

from api import crud, models, init_db, schemas

# SQLAlchemy specific code, as with any other app

app = FastAPI()


@app.on_event("startup")
async def startup():
    # await database.connect()
    async with init_db.engine.begin() as conn:
        # await conn.run_sync(models.Base.metadata.drop_all)
        await conn.run_sync(models.Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    pass
    # await database.disconnect()


@app.get("/a", response_model=list[schemas.A])
# async def read_a(async_session: async_sessionmaker[AsyncSession]):
async def read_a() -> list[models.A]:
    result = await crud.get_as()
    return result


@app.post("/a", response_model=schemas.A)
async def write_a(data: str) -> models.A:
    result = await crud.set_a(data=data)
    return result


@app.get("/")
async def root():
    return {"message": "Hello World"}
