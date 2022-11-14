from fastapi import APIRouter, Body
from sqlalchemy import create_engine, text

router = APIRouter(prefix='/course', tags=['Course'])
SQLALCHEMY_DATABASE_URL = "postgresql://changeme:changeme@localhost:5432/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


# Create
def insert_to_table(value):
    sql = text('INSERT INTO courses ( course_name ) VALUES (\'' + value + '\');')
    results = engine.execute(sql)
    return 'ok'


# Read
def read_from_table(item_id):
    r = []

    if item_id:
        sql = text('SELECT * FROM courses WHERE \"c-id\"= ' + str(item_id) + ';')
        results = engine.execute(sql)
    else:
        sql = text('SELECT * FROM courses;')
        results = engine.execute(sql)

    for result in results:
        r.append({"course_id": result[1], "course_name": result[0]})
    return r


# Update
def update_records(item_id, updated_value):
    # update a specific record
    if item_id and updated_value:
        sql = text('update courses set course_name = ' + updated_value + '  WHERE "c-id"=' + item_id + ';')
        results = engine.execute(sql)
        return results
    else:
        return "enter item_id and updated_value"


# Delete
def delete_records(item_id):
    # delete specific record
    if item_id:
        sql = text('DELETE FROM courses WHERE "c-id" =' + item_id + ';')
        results = engine.execute(sql)
        return results
    else:
        return "enter course-id"


@router.put('')
def update_record(item_id: str = None, updated_value: str = None):
    result = update_records(item_id, updated_value)
    return result


@router.delete('')
def delete_record(course_id: str = None):
    result = delete_records(course_id)
    return result


@router.get('')
def read_table(item_id: int = None):
    result = read_from_table(item_id)
    return result


@router.post('')
def add_course(body: dict = Body(...)):
    course_name = body['course title']
    result = insert_to_table(course_name)
    return {"result": 'result'}
