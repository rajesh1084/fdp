from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


class Record(BaseModel):
    subject: str
    marks: int


class Student(BaseModel):
    rollno: int
    name: str
    marks: list[Record]


app = FastAPI()

origins = ["*"]  # Replace with actual allowed origins in production

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the 'static' folder for serving static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# In-memory storage (for simplicity)
students = []


@app.post("/students/")
async def add_student(record: Student):
    """
    Adds a new student with their initial marks.

    Args:
        record (Student): The student's information.

    Returns:
        dict: A dictionary with a message indicating success.
    """
    students.append(record)
    return {"message": "Student added successfully"}


@app.get("/students/{student_id}")
async def get_student_marks(rollno: int):
    """
    Retrieves marks for a specific student.

    Args:
        Roll No (int): The student's .

    Returns:
        dict: A dictionary containing the student's ID, name, and marks.
    """
    # for student in students:
    #     if student.rollno == rollno:
    #         return {
    #             "rollno": student.rollno,
    #             "name": student.name,
    #             "marks": student.marks,
    #         }
    # or using list comprehension
    ret = [s for s in students if s.rollno == rollno]
    if not ret:
        raise HTTPException(status_code=404, detail="Student not found")
    return ret
    # raise HTTPException(status_code=404, detail="Student not found")


@app.get("/students/")
async def get_all_students():
    """
    Retrieves all students.

    Returns:
        list: A list of dictionaries containing student information.
    """
    return students


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
