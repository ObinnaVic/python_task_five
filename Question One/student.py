from fastapi import HTTPException
from pydantic import BaseModel
from typing import Dict
import json
import os

class Student(BaseModel):
    name: str
    subject_scores: Dict[str, float]
    average: float = 0.0
    grade: str = ""
    
    def __init__(self, **data):
        super().__init__(**data)
        self.calculate_average_and_grade()
    
    def calculate_average_and_grade(self):
        if self.subject_scores:
            self.average = sum(self.subject_scores.values()) / len(self.subject_scores)
            if self.average >= 90:
                self.grade = "A"
            elif self.average >= 80:
                self.grade = "B"
            elif self.average >= 70:
                self.grade = "C"
            elif self.average >= 60:
                self.grade = "D"
            else:
                self.grade = "F"


def load_students():
    try:
        if os.path.exists("students.json"):
            with open("students.json", "r") as file:
                return json.load(file)
        return {}
    except Exception:
        return {}

def save_students(students):
    try:
        with open("students.json", "w") as file:
            json.dump(students, file, indent=2)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to save data")

