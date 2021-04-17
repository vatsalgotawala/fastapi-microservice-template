# fastapi-microservice-template
This is a basic FastAPI template suitable for a small to medium scale service/application which you can use as a base for your service/application and start adding new routes for RestAPIs.

## Usage
**To get started with your service/application using this template, follow the below steps:**
1. Install [Python3.9](https://www.python.org/downloads/)
2. Install [Poetry](https://pypi.org/project/poetry/) which is used for dependency management
3. Refactor (along with its references) the directory `myservice` and rename it to be a suitable package name for your service/application
4. Update the name (to be the same as <app_directory> name you set in step 3) and description for your service/application in the `pyproject.toml` file. We will refer to this directory as <app_directory>
5. Update the name (to be the same as <app_directory> name you set in step 3), title and description for your service/application in the `<app_directory>/config.py` file
6. Create a [virtual environment](https://docs.python.org/3/library/venv.html) and configure the path for the same
7. Run below poetry commands from the root directory to install existing or add/remove new dependencies
    ```bash
    # To install all existing dependencies in pyproject.toml file
    poetry install

    # To add a new dependency
    poetry add <package_name>@~<x.x>
    poetry add requests@~2.24

    # To remove a dependency
    poetry remove <package_name>
    poetry remove requests
    ```
8. To run the service/application, you can run the below command from the `<app_directory>` and access the same over `http://localhost:8081`
    ```bash
    uvicorn --reload --host=0.0.0.0 --port=8081 main:app
    ```
