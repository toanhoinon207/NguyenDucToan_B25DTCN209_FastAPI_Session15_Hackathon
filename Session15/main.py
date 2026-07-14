from fastapi import FastAPI, Depends, HTTPException, status
from database import engine, Base, get_db
from service import test_server, show_employees, find_employees_by_department, show_employee_detail, add_employee, edit_employee, remove_employee
from sqlalchemy.orm import Session
from schemas import EmployeeResponse

Base.metadata.create_all(bind = engine)

app = FastAPI()

def ResponseAPI(statusCode, error, message, data):
    return {
        "statusCode": statusCode,
        "error": error,
        "message": message,
        "data": data
    }

@app.get("/")
def check_server():
    return test_server()

@app.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    employees = show_employees(db)
    return ResponseAPI(
        200, 
        None, 
        "Lấy danh sách nhân viên thành công",
        employees
    )

@app.get("/employees/search")
def find_employee(department: str, db: Session = Depends(get_db)):
    employee = find_employees_by_department(db, department)
    return ResponseAPI(
        200,
        None,
        "Tìm thấy nhân viên",
        employee
    )

@app.get("/employees/{employee_id}")
def get_employees_detail(employee_id: int, db: Session = Depends(get_db)):
    employee = show_employee_detail(db, employee_id)
    if employee is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = {
                "statusCode": 404,
                "error": "Not Found",
                "message": "Không tìm thấy nhân viên",
                "data": None
            }
        )
    return ResponseAPI(
        200,
        None,
        "Tìm thấy nhân viên",
        employee
    )

@app.post("/employees")
def create_employee(employee: EmployeeResponse, db: Session = Depends(get_db)):
    new_employee = add_employee(db, employee)
    return ResponseAPI(
        201,
        None,
        "Thêm nhân viên thành công",
        new_employee
    )

@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee_update: EmployeeResponse, db: Session = Depends(get_db)):
    employee = edit_employee(db, employee_update, employee_id)
    if employee is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = {
                "statusCode": 404,
                "error": "Not Found",
                "message": "Không tìm thấy nhân viên",
                "data": None
            }
        )
    return ResponseAPI(
        200,
        None,
        "Cập nhật nhân viên thành công",
        employee_update
    )

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = remove_employee(db, employee_id)
    if employee is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = {
                "statusCode": 404,
                "error": "Not Found",
                "message": "Không tìm thấy nhân viên",
                "data": None
            }
        )
    return ResponseAPI(
        200,
        None,
        "Xóa nhân viên thành công",
        None
    )