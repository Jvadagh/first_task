from fastapi import APIRouter, Body, status
from sqlalchemy import create_engine, text

router = APIRouter(prefix='/students', tags=['Students'])
SQLALCHEMY_DATABASE_URL = "postgresql://changeme:changeme@localhost:5432/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


# Create
def insert_to_table(value):
    sql = text('INSERT INTO students ( flname ) VALUES (\'' + value + '\');')
    results = engine.execute(sql)
    return status


# Read
def read_from_table(item_id):
    r = []

    if item_id:
        sql = text('SELECT * FROM students WHERE \"s-id\"= ' + str(item_id) + ';')
        results = engine.execute(sql)
    else:
        sql = text('SELECT * FROM students;')
        results = engine.execute(sql)

    for result in results:
        r.append({"student_id": result[1], "student_name": result[0]})
    return r


# Update
def update_records(item_id, updated_value):
    # update a specific record
    if item_id and updated_value:
        sql = text('update students set flname = ' + updated_value + '  WHERE "s-id"=' + item_id + ';')
        results = engine.execute(sql)
        return results
    else:
        return "enter item_id and updated_value"


# Delete
def delete_records(item_id):
    # delete specific record
    if item_id:
        sql = text('DELETE FROM students WHERE "s-id" =' + item_id + ';')
        results = engine.execute(sql)
    else:
        return "enter student-id"


@router.put('')
def update_record(item_id: str = None, updated_value: str = None):
    result = update_records(item_id, updated_value)
    return result


@router.delete('')
def delete_record(student_id: str = None):
    result = delete_records(student_id)
    return result


@router.get('')
def read_table(item_id: int = None):
    result = read_from_table(item_id)
    return result


@router.post('', status_code=status.HTTP_200_OK)
def add_student(body: dict = Body(...)):
    name = body['flname']
    result = insert_to_table(name)
    return {"result": status.HTTP_200_OK}
