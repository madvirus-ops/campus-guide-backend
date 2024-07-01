import sys
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

sys.path.append("./")
from .database import get_env, tz


class AbstractModel(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(tz))


class Location(AbstractModel, table=True):
    __tablename__ = "locations"
    name: str = Field(index=True)
    type: str
    latitude: str
    longitude: str
    description: str
    thumbnail: str
    department: Optional["Department"] = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="location"
    )
    faculty: Optional["Faculty"] = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="location"
    )


class Department(AbstractModel, table=True):
    __tablename__ = "departments"
    name: str = Field(index=True)
    location_id: int = Field(foreign_key="locations.id")
    faculty_id: int = Field(foreign_key="faculty.id", nullable=True)
    contact_email: str
    contact_phone: str
    head_of_department: str
    location: Optional["Location"] = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="department"
    )
    faculty: Optional["Faculty"] = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="department"
    )
    course: Optional["Course"] = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="department"
    )


class Faculty(AbstractModel, table=True):
    __tablename__ = "faculty"
    name: str = Field(index=True)
    location_id: int = Field(foreign_key="locations.id")
    email: str
    bio: str

    location: Optional["Location"] = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="faculty"
    )
    department: Optional["Department"] = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="faculty"
    )


class Course(AbstractModel, table=True):
    __tablename__ = "courses"
    department_id: int = Field(foreign_key="departments.id")
    course_name: str
    course_code: str
    credits: int
    department: Optional["Department"] = Relationship(
        sa_relationship_kwargs={"cascade": "delete"}, back_populates="course"
    )


class Information(AbstractModel, table=True):
    __tablename__ = "information"
    title: str
    content: str
    type: str
