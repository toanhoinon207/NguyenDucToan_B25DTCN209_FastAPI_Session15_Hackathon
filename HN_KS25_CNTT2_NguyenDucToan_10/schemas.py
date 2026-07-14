from pydantic import BaseModel, Field

class EmployeeResponse(BaseModel):
    full_name: str = Field(..., min_length = 1)
    department: str = Field(..., min_length = 1)
    position: str = Field(..., min_length = 1)
    salary: float = Field(..., ge = 0)