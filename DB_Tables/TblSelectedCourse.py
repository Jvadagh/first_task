from fastapi import APIRouter, Body
from sqlalchemy import create_engine, text

router = APIRouter(prefix='/selectunit', tags=['SelectUnit'])
SQLALCHEMY_DATABASE_URL = "postgresql://changeme:changeme@localhost:5432/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


# Create
def insert_to_table(value1, value2):
    sql = text('INSERT INTO bridge ( "c-id" , "s-id" ) VALUES (\' ' + value1 + '\' , \' ' + value2 + ' \');')
    results = engine.execute(sql)
    return 'ok'


# Read
def read_from_table(item_id):
    r = []

    if item_id:
        sql = text('SELECT * FROM bridge WHERE \"s-id\"= ' + str(item_id) + ';')
        results = engine.execute(sql)
    else:
        sql = text('SELECT * FROM bridge;')
        results = engine.execute(sql)

    for result in results:
        r.append({"student_id": result[1], "course_id": result[0]})
    return r


# Update
def update_records(item_id, updated_value):
    # update a specific record
    if item_id and updated_value:
        sql = text('update bridge set "c-id" = ' + updated_value + '  WHERE "s-id"=' + item_id + ';')
        results = engine.execute(sql)
        return results
    else:
        return "enter item_id and updated_value"


# Delete
def delete_records(item_id):
    # delete specific record
    if item_id:
        sql = text('DELETE FROM bridge WHERE "c-id" =' + item_id + ';')
        results = engine.execute(sql)
    else:
        return "enter student-id"


@router.put('')
def update_record(s_id: str = None, updated_c_id_value: str = None):
    result = update_records(s_id, updated_c_id_value)
    return result


@router.delete('')
def delete_record(course_id: str = None):
    result = delete_records(course_id)
    return result


@router.get('')
def read_table(student_id: int = None):
    result = read_from_table(student_id)
    return result


@router.post('')
def add_course(body: dict = Body(...)):
    course_id = body['course ID']
    student_id = body['student ID']
    result = insert_to_table(course_id, student_id)
    return {"result": result}
