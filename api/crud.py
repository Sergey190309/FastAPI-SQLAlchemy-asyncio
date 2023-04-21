from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from api.init_db import async_session
from api.models import A


async def get_a_by_data(data: str) -> A | None:
    async with async_session() as session:
        stmt = select(A).where(A.data == data).options(selectinload(A.bs))
        query_result = await session.execute(stmt)
        result = query_result.scalars().first()
    return result


async def get_as():
    async with async_session() as session:
        stmt = select(A).options(selectinload(A.bs))
        query_result = await session.execute(stmt)
        # for item in result:
        #     print('item ->', item.__dict__, '\n')
    return query_result.scalars().all()


async def set_a(data: str) -> A:
    item = await get_a_by_data(data=data)
    if item:
        raise HTTPException(status_code=400, detail='Data already exists')
    async with async_session() as session:
        async with session.begin():
            session.add(A(data=data))
    result = await get_a_by_data(data=data)
    print('\ncrud\n',
          'result ->', result, '\n'
          )
    return result
    # async with async_session() as session:
    #     stmt = select(A).options(selectinload(A.bs))

    #     result = await session.execute(stmt)
