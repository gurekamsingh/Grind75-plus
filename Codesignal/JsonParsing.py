# You are given a class of students, and you need to decide whether it is possible to divide them into a new group such that all students in that group have pairwise distinct surnames.
# In simple terms:
# No two students in the selected group should share the same surname.

# Your task is not to actually form the group, but to check whether it is possible
# GET http://localhost/studentList
# Response format
# {
#   "n": <int>,
#   "m": <int>,
#   "ids": [<int>, <int>, ..., <int>]
# }
# Meaning:
# n → number of students
# m → number of students you want in the new group
# ids → list of student IDs (distinct integers in range [0, n))
# This tells you which students exist and how many you’re trying to group.
import requests
import json

BASE_URL = "http://localhost" 
def can_divide():
    resp = requests.get(f"{BASE_URL}/studentList")
    data = json.loads(resp.text)

    surnames = set()
    m = data["m"]
    for student_id in data["ids"]:
        resp1 = requests.get(f"{BASE_URL}/student", params={"student_id": id})
        data1 = json.loads(resp1.text)
        surnames.add(data1["surname"])

        if len(surnames) >= m:
            return "class can be divided"
        return "class cannot be divided"
    
print(can_divide())

