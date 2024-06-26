import sys

sys.path.append("./")
from connections.models import Information, Course, Location, tz,Department,Faculty
from connections.schemas import (
    CourseIn,
    UpdateCourse,
    GeneralIn,
    UpdateGeneral,
    LocationIn,
    UpdateLocation,
    FacultyIn,
    UpdateFaculty,
    DepartmentIn,
    UpdateDepartment,
    DeleteIN
)
from datetime import datetime
from sqlmodel import Session, select
from controllers import responses as r


async def add_location(body: LocationIn, db: Session):
    try:
        stmt = select(Location).where(
            Location.name == body.name, Location.latitude == body.latitude
        )
        check = db.exec(stmt).first()
        if check:
            return r.exists
        new = Location(**body.model_dump())
        db.add(new)
        db.commit()
        return r.created
    except Exception as e:
        print(e.args)
        return r.error_occured



async def edit_location(body: UpdateLocation, db: Session):
    try:
        stmt = select(Location).where(Location.id == body.location_id)
        check = db.exec(stmt).first()
        if not check:
            return r.not_found
        data = body.model_dump(exclude_unset=True)
        check.updated_at = datetime.now(tz)
        for key, value in data.items():
            if key == "location_id":
                continue
            setattr(check, key, value)
        db.add(check)
        db.commit()
        return r.updated
    except Exception as e:
        print(e.args)
        return r.error_occured



async def get_location(db: Session):
    try:
        stmt = select(Location).order_by(Location.updated_at.desc())
        check = db.exec(stmt).all()

        return {"code": 200, "message": "fetched", "status": "success", "data": check}

    except Exception as e:
        print(e.args)
        return r.error_occured





async def add_courses(body: CourseIn, db: Session):
    try:
        stmt = select(Course).where(
            Course.course_code == body.course_code
        )
        check = db.exec(stmt).first()
        if check:
            return r.exists
        new = Course(**body.model_dump())
        db.add(new)
        db.commit()
        return r.created
    except Exception as e:
        print(e.args)
        return r.error_occured



async def edit_courses(body: UpdateCourse, db: Session):
    try:
        stmt = select(Course).where(Course.id == body.course_id)
        check = db.exec(stmt).first()
        if not check:
            return r.not_found
        data = body.model_dump(exclude_unset=True)
        check.updated_at = datetime.now(tz)
        for key, value in data.items():
            if key == "course_id":
                continue
            setattr(check, key, value)
        db.add(check)
        db.commit()
        return r.updated
    except Exception as e:
        print(e.args)
        return r.error_occured



async def get_courses(db: Session):
    try:
        stmt = select(Course).order_by(Course.updated_at.desc())
        check = db.exec(stmt).all()

        return {"code": 200, "message": "fetched", "status": "success", "data": check}

    except Exception as e:
        print(e.args)
        return r.error_occured




async def add_general(body: GeneralIn, db: Session):
    try:
        stmt = select(Information).where(
            Information.title == body.title,Information.type == body.type
        )
        check = db.exec(stmt).first()
        if check:
            return r.exists
        new = Information(**body.model_dump())
        db.add(new)
        db.commit()
        return r.created
    except Exception as e:
        print(e.args)
        return r.error_occured



async def edit_general(body: UpdateGeneral, db: Session):
    try:
        stmt = select(Information).where(Information.id == body.information_id)
        check = db.exec(stmt).first()
        if not check:
            return r.not_found
        data = body.model_dump(exclude_unset=True)
        check.updated_at = datetime.now(tz)
        for key, value in data.items():
            if key == "information_id":
                continue
            setattr(check, key, value)
        db.add(check)
        db.commit()
        return r.updated
    except Exception as e:
        print(e.args)
        return r.error_occured



async def get_general(db: Session):
    try:
        stmt = select(Information).order_by(Information.updated_at.desc())
        check = db.exec(stmt).all()

        return {"code": 200, "message": "fetched", "status": "success", "data": check}

    except Exception as e:
        print(e.args)
        return r.error_occured



async def add_department(body: DepartmentIn, db: Session):
    try:
        stmt = select(Department).where(
            Department.name == body.name
        )
        check = db.exec(stmt).first()
        if check:
            return r.exists
        new = Department(**body.model_dump())
        db.add(new)
        db.commit()
        return r.created
    except Exception as e:
        print(e.args)
        return r.error_occured



async def edit_department(body: UpdateDepartment, db: Session):
    try:
        stmt = select(Department).where(Department.id == body.department_id)
        check = db.exec(stmt).first()
        if not check:
            return r.not_found
        data = body.model_dump(exclude_unset=True)
        check.updated_at = datetime.now(tz)
        for key, value in data.items():
            if key == "department_id":
                continue
            setattr(check, key, value)
        db.add(check)
        db.commit()
        return r.updated
    except Exception as e:
        print(e.args)
        return r.error_occured



async def get_department(db: Session):
    try:
        stmt = select(Department).order_by(Department.updated_at.desc())
        check = db.exec(stmt).all()

        return {"code": 200, "message": "fetched", "status": "success", "data": check}

    except Exception as e:
        print(e.args)
        return r.error_occured





async def add_faculty(body: FacultyIn, db: Session):
    try:
        stmt = select(Faculty).where(
            Faculty.name == body.name
        )
        check = db.exec(stmt).first()
        if check:
            return r.exists
        new = Faculty(**body.model_dump())
        db.add(new)
        db.commit()
        return r.created
    except Exception as e:
        print(e.args)
        return r.error_occured



async def edit_faculty(body: UpdateFaculty, db: Session):
    try:
        stmt = select(Faculty).where(Faculty.id == body.faculty_id)
        check = db.exec(stmt).first()
        if not check:
            return r.not_found
        data = body.model_dump(exclude_unset=True)
        check.updated_at = datetime.now(tz)
        for key, value in data.items():
            if key == "faculty_id":
                continue
            setattr(check, key, value)
        db.add(check)
        db.commit()
        return r.updated
    except Exception as e:
        print(e.args)
        return r.error_occured



async def get_faculty(db: Session):
    try:
        stmt = select(Faculty).order_by(Faculty.updated_at.desc())
        check = db.exec(stmt).all()

        return {"code": 200, "message": "fetched", "status": "success", "data": check}

    except Exception as e:
        print(e.args)
        return r.error_occured



async def delete_somethings(id: int, delete_type: str, db: Session):
    try:
        delete_type = delete_type.lower()

        if delete_type == "course":
            stmt = select(Course).where(Course.id == id)
        elif delete_type == "location":
            stmt = select(Location).where(Location.id == id)
        elif delete_type == "information":
            stmt = select(Information).where(Information.id == id)
        elif delete_type == "faculty":
            stmt = select(Faculty).where(Faculty.id == id)
        elif delete_type == "department":
            stmt = select(Department).where(Department.id == id)
        else:
            return {"code": 400, "message": "Invalid delete_type", "status": "error"}

        result = db.exec(stmt).first()
        if result:
            db.delete(result)
            db.commit()
            return {"code": 200, "message": "Deleted successfully", "status": "success"}
        else:
            return {"code": 404, "message": "Item not found", "status": "error"}

    except Exception as e:
        print(e.args)
        return {"code": 500, "message": "An error occurred", "status": "error"}
