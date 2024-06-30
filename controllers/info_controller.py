import os
import requests as re
from bs4 import BeautifulSoup
from dotenv import load_dotenv

import sys

sys.path.append("./")


load_dotenv()


# Retrieve the endpoint URL from the environment variables
endpoint = os.getenv("CELL_LINK")


def getMatNoInfo(matno: str):

    url = endpoint + "?matric_no=" + matno
    res = re.get(url).text
    soup = BeautifulSoup(res, features="html.parser")

    def extractor(a, b):
        return soup.find(f"{a}", {"id": f"{b}"}).text

    if soup.title.string == "Runtime Error":
        return {
            "code": 404,
            "status": "error",
            "message": "Matric number not found",
        }

    else:
        return {
            "code": 200,
            "status": "success",
            "message": "Information retrieved successfully",
            # find imgPassport and get the src attribute
            "image": soup.find("img", {"id": "imgPassport"}).get("src"),
            "message": "success",
            "name": extractor("span", "lblFullName"),
            "address": extractor("span", "lblAddress"),
            "phone": extractor("span", "lblPhone"),
            "email": extractor("span", "lblEmail"),
            "mat_no": extractor("span", "lblMatricNo"),
            "faculty": extractor("span", "lblFaculty"),
            "department": extractor("span", "lblDepartment"),
        }
