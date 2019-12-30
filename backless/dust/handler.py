import os
import sqlalchemy as db

def dust(event, context):
    db_url = os.getenv("CX_DB_URL")
    db_prefix = 'postgresql+psycopg2' if 'postgres' in db_url else '' 
    db_user = os.getenv("CX_DB_USER")
    db_pwd = os.getenv("CX_DB_PWD")

    access_url = db_url.split("//")
    access_url = f'{db_prefix}://{db_user}:{db_pwd}@{access_url[1]}'

    engine = db.create_engine(access_url)
    connection = engine.connect()

    inspector = db.inspect(engine)
    
    result = {'db_url': db_url,'tables': inspector.get_table_names()}
    connection.close()
    return result