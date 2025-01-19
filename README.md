* **What is Python? Why Python?**

* **Python Trivia**
    * Python interpreter 'CPython' is written in C language
    * Python (1991) is older than Java (1995)
    * Python is used in the International Space Station (ISS).

* **Transition to APIs**
    "Now that we have a basic understanding of Python, let's explore how it can be used to build powerful APIs. An API, or Application Programming Interface, acts as a messenger between different software systems, allowing them to communicate and exchange data."

    * **Analogy:** Restaurant Order, Library Catalog

* **FastAPI** is a modern, high-performance web framework for building APIs with Python

* **Setup environment** - install/setup Python venv, create project structure
    * **How to setup python venv in vscode:**
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

* **Build a simple API**
    * create a basic GET endpoint ("Hello World")
    * **tell briefly about API Specification:** It is a contract between the API provider and the API consumers, ensuring that both parties understand how to interact with the API correctly.
    * **tell briefly about HTTP methods:** GET, POST, DELETE, PATCH, PUT
