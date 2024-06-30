import sys

sys.path.append("./")
from sqlmodel import SQLModel
from enum import Enum


class Login(SQLModel):
    mat_no: str


class LocationIn(SQLModel):
    name: str
    type: str
    latitude: str
    longitude: str
    description: str
    thumbnail: str


class UpdateLocation(LocationIn):
    location_id: int


class CourseIn(SQLModel):
    department_id: int
    course_name: str
    course_code: str
    credits: int


class UpdateCourse(CourseIn):
    course_id: int


class GeneralIn(SQLModel):
    title: str
    content: str
    type: str


class UpdateGeneral(GeneralIn):
    information_id: int


class DepartmentIn(SQLModel):
    name: str
    location_id: int
    faculty_id: int
    contact_email: str
    contact_phone: str
    head_of_department: str


class UpdateDepartment(DepartmentIn):
    department_id: int


class FacultyIn(SQLModel):
    name: str
    location_id: int
    email: str
    bio: str


class UpdateFaculty(FacultyIn):
    faculty_id: int


class DeleteType(str, Enum):
    department = "department"
    faculty = "faculty"
    information = "information"
    location = "location"
    course = "course"


class DeleteIN(SQLModel):
    id: int
    delete_type: DeleteType
