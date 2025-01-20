# Faculty Development Program (FDP) Presentation Content

## **What is Python? Why Python?**

* Python is a high-level, general-purpose programming language known for its readability and versatility. It emphasizes code clarity and simplicity, making it beginner-friendly while also being powerful enough for complex tasks.
* Python's popularity stems from its:
  - Readability: Clear and concise syntax, making it easier to learn and maintain.
  - Versatility: Suitable for a wide range of applications, from web development and data science to machine learning and automation.
  - Large Community: A vast and active community provides excellent support, extensive libraries, and abundant resources.

## **Python Trivia**

- Python interpreter 'CPython' is written in C language
- Python (1991) is older than Java (1995)
- Python is used in the International Space Station (ISS).

## **Transition to APIs**

Now that we have a basic understanding of Python, let's explore how it can be used to build powerful APIs. An API, <br>
or Application Programming Interface, acts as a messenger between different software systems, allowing them to communicate and exchange data.
**Analogy:** Restaurant Order

* Synchronous - REST, GRPC etc
* Asynchronous - Kafka, RabbitMQ etc
    

## **FastAPI**

FastAPI is a simple, modern, high-performance web framework for building APIs with Python

## **Setup environment** - install/setup Python venv, create project structure

* What's venv? Why do we need it?
  
* **Setup python venv in vscode:**
* Setup python venv in vscode -> Command Palette > Python: Create Environment
  
* **Setup venv in commandline**
  ```bash
  python3 -m venv .venv
  source ./.venv/bin/activate
  # To deactivate venv
  deactivate
  ```
* **Install required packages (uvicorn, fastapi)**
  ```bash
  pip install fastapi uvicorn "uvicorn[standard]" "fastapi[standard]" 
  ```

## **Build a hello world API using Python FastAPI**

* create a basic GET endpoint ("Hello World")
* **API Specification**: It is a contract between the API provider and the API consumers, ensuring that both parties understand how to interact with the API correctly.
* **HTTP methods**: GET, POST, DELETE, PATCH, PUT
* Show a simple API specification (sample_api_spec.yaml)
* Run the application and show the output
  ```bash
  uvicorn main:app --reload
  ```
 
## **Build a student-marks using Python FastAPI**
* APIs:
  - POST /students - Create a student record
  - PATCH /students/{id}  - Add marks to an existing student (update the student record)
  - GET /students - Get all students' details
  - GET /students/{id} - Get details of a student
* Run the application and show the output
  ```bash
  uvicorn main:app --reload
  ```
   
## **Q&A**

## **Additional Topics**
* Brief introduction about Language models
* Interfacing with models using Python/Jupiter Notebook
* Brief introduction to AI Agents
 
## **Conclusion**
* Share contact information  
