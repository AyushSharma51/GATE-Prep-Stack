from enum import Enum


class GateBranch(str, Enum):
    CSE = "cse"
    DA = "da"
    ME = "me"
    EE = "ee"
    CE = "ce"
    EC = "ec"


# Mapping for display
BRANCH_FULL_FORM = {
    "cse": "Computer Science and Engineering",
    "da": "Data Science and Artificial Intelligence",
    "me": "Mechanical Engineering",
    "ee": "Electrical Engineering",
    "ce": "Civil Engineering",
    "ec": "Electronics and Communication Engineering",
}
