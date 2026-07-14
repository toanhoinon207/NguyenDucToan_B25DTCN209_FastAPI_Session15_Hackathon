from sqlalchemy import Column, Integer, String, Float
from database import Base

class EmployeeModel(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key = True, index = True)
    full_name = Column(String(100), nullable = False)
    department = Column(String(50), nullable = False)
    position = Column(String(50), nullable= False)
    salary = Column(Float, nullable= False)
    