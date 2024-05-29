from math import ceil
from typing import Any


class OnlineCourse:

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        return ceil(days / 7)

    @classmethod
    def from_dict(cls, course_dict: dict) -> Any:
        result = OnlineCourse.days_to_weeks(course_dict["days"])
        return cls(course_dict["name"], course_dict["description"], result)
