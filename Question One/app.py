from fastapi import FastAPI, HTTPException
from student import Student, load_students, save_students
app = FastAPI()

@app.post("/students/")
def create_student(student: Student):
    try:
        students = load_students()
        students[student.name] = student.dict()
        save_students(students)
        return student
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to create student")

@app.get("/students/{name}")
def get_student(name: str):
    try:
        students = load_students()
        if name not in students:
            raise HTTPException(status_code=404, detail="Student not found")
        return students[name]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve student")

@app.get("/students/")
def get_all_students():
    try:
        students = load_students()
        return list(students.values())
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to retrieve students")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)