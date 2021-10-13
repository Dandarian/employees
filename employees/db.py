from sqlalchemy import (
    MetaData, Table, Column,
    Integer, String, Date
)
from sqlalchemy_utils import EmailType
import aiopg.sa

meta = MetaData()

employee = Table(
    'employee', meta,

    Column('id', Integer, primary_key=True),
    Column('employee_name', String(200), nullable=False),
    Column('e_mail', EmailType, nullable=False),
    Column('phone_number', Integer, nullable=False),
    Column('inn', Integer, nullable=False),
    Column('position', String(200), nullable=False),
    Column('department', Integer, nullable=False),
    Column('passport', Integer, nullable=False),
    Column('passport_issued', String(200), nullable=False),
    Column('education', String(200), nullable=False),
    Column('address', String(200), nullable=False),
    Column('birth_date', Date, nullable=False)
)


async def pg_context(app):
    engine = await aiopg.sa.create_engine(
        database='postgres',
        user='postgres',
        password='postgres',
        host='db',
        port=5432,
    )
    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()


async def post_employee(conn, field_values):
    stmt = employee.insert().values([field_values])
    await conn.execute(stmt)


async def put_employee(conn, id, field_values):
    stmt = employee.update().where(employee.c.id == id).values(field_values)
    await conn.execute(stmt)
