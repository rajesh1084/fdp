from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

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
async def add_student(student_id: int, name: str, marks: list):
    """
    Adds a new student with their initial marks.

    Args:
        student_id (int): The student's ID.
        name (str): The student's name.
        marks (list): A list of dictionaries,
                     where each dictionary contains "subject" and "marks".
                     Example: [{"subject": "Math", "marks": 85}, {"subject": "Science", "marks": 90}]

    Returns:
        dict: A dictionary with a message indicating success.
    """
    new_student = {"student_id": student_id, "name": name, "marks": marks}
    students.append(new_student)
    return {"message": "Student added successfully"}


@app.get("/students/{student_id}")
async def get_student_marks(student_id: int):
    """
    Retrieves marks for a specific student.

    Args:
        student_id (int): The student's ID.

    Returns:
        dict: A dictionary containing the student's ID, name, and marks.
    """
    for student in students:
        if student["student_id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


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
