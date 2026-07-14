from sqlalchemy.orm import Session
from models import EmployeeModel
from schemas import EmployeeResponse

def test_server():
    return {
        "messsage": "API đang chạy",
        "data": None
    }

def show_employees(db: Session):
    return db.query(EmployeeModel).all()

def find_employees_by_department(db: Session, department: str):
    return db.query(EmployeeModel).filter(EmployeeModel.department.contains(department)).all()

def show_employee_detail(db: Session, employee_id: int):
    employee = db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
    if employee is None:
        return None
    return employee

def add_employee(db: Session, employee: EmployeeResponse):
    new_employee = EmployeeModel(
        full_name = employee.full_name,
        department = employee.department,
        position = employee.position,
        salary = employee.salary
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def edit_employee(db: Session, employee_update: EmployeeResponse, employee_id: int):
    employee = db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
    if employee is None:
        return None
    employee.full_name = employee_update.full_name
    employee.department = employee_update.department
    employee.position = employee_update.position
    employee.salary = employee_update.salary
    db.commit()
    return employee

def remove_employee(db: Session, employee_id):
    employee = db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()
    if employee is None:
        return None
    db.delete(employee)
    db.commit()
    return employee