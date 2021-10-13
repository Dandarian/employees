from sqlalchemy import create_engine, MetaData
from db import employee


def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[employee])


if __name__ == '__main__':
    db_url = 'postgresql://postgres:postgres@db:5432/postgres'
    engine = create_engine(db_url)

    create_tables(engine)
