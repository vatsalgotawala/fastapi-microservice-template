# fastapi-microservice-template
This is a basic FastAPI template suitable for a small to medium scale service/application which you can use as a base for your service/application and start adding new routes for RestAPIs.

## Usage
NOTE: All commands are executed from project root directory.
**To get started with your service/application using this template, follow the below steps:**
1. Install [python3.9](https://www.python.org/downloads/)
2. Install [poetry](https://pypi.org/project/poetry/) which is used for dependency management. Optionally, install [pre-commit](https://pre-commit.com/) to run git hooks
3. Refactor (along with its references) the directory `myservice` and rename it to be a suitable package name for your service/application. We will refer to this directory as <app_directory>
4. Update the name (to be the same as <app_directory> name you set in step 3) and description for your service/application in the `pyproject.toml` file
5. Update the name (to be the same as <app_directory> name you set in step 3), title and description for your service/application in the `<app_directory>/config.py` file
6. Create a [virtual environment](https://docs.python.org/3/library/venv.html) and configure the path for the same
7. Run below poetry commands to install existing or add/remove new dependencies
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
8. Optionally, run the below command to set up the git hook scripts using the `.pre-commit-config.yaml` file containing some pre-configured hooks
    ```bash
    pre-commit install
    ```
9. To run the service/application, you can run the below command and access the same over `http://localhost:8081`
    ```bash
    # Make sure to replace <app_directory> with your actual directory name
    uvicorn --reload --host=0.0.0.0 --port=8081 <app_directory>.main:app
    uvicorn --reload --host=0.0.0.0 --port=8081 myservice.main:app
    ```
10. To run the tests and get the test coverage report, you can run the below command
    ```bash
    # Make sure to replace <app_directory> with your actual directory name
    pytest --cov=<app_directory>
    pytest --cov=myservice
    ```

## Docker Compose Commands
NOTE: All commands are executed from project root directory.
```bash
# To run the service/application using docker compose
docker-compose up [--build]
```

## Docker Build Commands
NOTE: All commands are executed from project root directory.
```bash
# To build the development (debug) docker image
docker build --target debug-image -t fastapi-ms-template .

# To build the lightweight production docker image
docker build --target build-image -t fastapi-ms-template .
```
