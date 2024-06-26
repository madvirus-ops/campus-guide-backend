import sys
sys.path.append("./")

error_occured = {
    "code":500,
    "message":"Error occured",
    "status":"error"
}

exists = {
    "code":400,
    "message":"Already exists",
    "status":"error"
}

created = {
    "code":201,
    "message":"created successfully",
    "status":"success"
}

updated = {
    "code":200,
    "message":"updated successfully",
    "status":"success"
}

not_found = {
    "code":404,
    "message":"not found or missing",
    "status":"error"
}

invalid_session = {
    "code":421,
    "message":"Session must be in the format '2023/2024' ",
    "status":"error"
}
