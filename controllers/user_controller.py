import sys

sys.path.append("./")


from controllers.info_controller import getMatNoInfo


async def userLogin(mat_no: str):
    return getMatNoInfo(mat_no)
