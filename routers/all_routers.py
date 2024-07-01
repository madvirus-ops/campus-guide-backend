import sys

from connections.schemas import Login
from controllers.user_controller import userLogin

sys.path.append("./")
from connections.database import get_db
from fastapi import APIRouter, Response, Request, Depends
from sqlalchemy.orm import Session
from controllers.all_controllers import *
from connections.database import get_session

login_router = APIRouter(prefix="/api/v1", tags=["User"])
router = APIRouter(prefix="/api/v1", tags=["Courses"])
router2 = APIRouter(prefix="/api/v1", tags=["Locations"])
router3 = APIRouter(prefix="/api/v1", tags=["Information"])
router4 = APIRouter(prefix="/api/v1", tags=["Faculty"])
router5 = APIRouter(prefix="/api/v1", tags=["Department"])
common = APIRouter(prefix="/api/v1", tags=["Common"])


@login_router.post("/login")
async def login(
    body: Login,
    request: Request,
    response: Response,
):
    result = await userLogin(mat_no=body.mat_no)
    response.status_code = result["code"]
    return result


@router.post("/courses")
async def create__courses(
    body: CourseIn,
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    result = await add_courses(body, db)
    response.status_code = result["code"]
    return result


@router.get("/courses")
async def get__courses(
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    result = await get_courses(db)
    response.status_code = result["code"]
    return result


@router.put("/courses")
async def edit__courses(
    body: UpdateCourse,
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    result = await edit_courses(body, db)
    response.status_code = result["code"]
    return result


@router2.post("/locations")
async def create__location(
    body: LocationIn,
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    result = await add_location(body, db)
    response.status_code = result["code"]
    return result


@router2.get("/locations")
async def get__location(
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    result = await get_location(db)
    response.status_code = result["code"]
    return result


@router2.put("/locations")
async def edit__locations(
    body: UpdateLocation,
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    result = await edit_location(body, db)
    response.status_code = result["code"]
    return result


@router3.post("/informations")
async def create__informations(
    body: GeneralIn,
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    result = await add_general(body, db)
    response.status_code = result["code"]
    return result


@router3.get("/informations")
async def get__informations(
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    result = await get_general(db)
    response.status_code = result["code"]
    return result


@router3.put("/informations")
async def edit__informations(
    body: UpdateGeneral,
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    result = await edit_general(body, db)
    response.status_code = result["code"]
    return result


@router4.post("/faculty")
async def create__faculty(
    body: FacultyIn,
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    result = await add_faculty(body, db)
    response.status_code = result["code"]
    return result


@router4.get("/faculty")
async def get__faculty(
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    result = await get_faculty(db)
    response.status_code = result["code"]
    return result


@router4.put("/faculty")
async def edit__faculty(
    body: UpdateFaculty,
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    result = await edit_faculty(body, db)
    response.status_code = result["code"]
    return result


@router5.post("/department")
async def create__department(
    body: DepartmentIn,
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    result = await add_department(body, db)
    response.status_code = result["code"]
    return result


@router5.get("/department")
async def get__department(
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    result = await get_department(db)
    response.status_code = result["code"]
    return result


@router5.put("/department")
async def edit__department(
    body: UpdateDepartment,
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    result = await edit_department(body, db)
    response.status_code = result["code"]
    return result


@common.delete("/delete")
async def delete__something(
    body: DeleteIN,
    request: Request,
    response: Response,
    db: Session = Depends(get_session),
):
    """

    ```
    class DeleteType(str,Enum):
        department = "department"
        faculty = "faculty"
        information = "information"
        location = "location"
        course = "course"


    ```

    """
    result = await delete_somethings(body.id, body.delete_type.value, db)
    response.status_code = result["code"]
    return result
