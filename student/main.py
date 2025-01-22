from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Record(BaseModel):
    subject: str
    marks: int


class Student(BaseModel):
    rollno: int
    name: str
    marks: list[Record]


app = FastAPI()


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
        Roll No (int): The student's roll no.

    Returns:
        dict: A dictionary containing the student's ID, name, and marks.
    """
    for student in students:
        if student.rollno == rollno:
            return {
                "rollno": student.rollno,
                "name": student.name,
                "marks": student.marks,
            }
    raise HTTPException(status_code=404, detail="Student not found")
    # or using list comprehension
    # ret = [s for s in students if s.rollno == rollno]
    # if not ret:
    #     raise HTTPException(status_code=404, detail="Student not found")
    # return ret


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
