ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION} AS base-image
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    WORKDIR_PATH="/code" \
    VENV_PATH="/service_venv"
RUN apt-get update -y && apt-get install -y build-essential
WORKDIR $WORKDIR_PATH
RUN python -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"
RUN pip install --no-cache-dir --compile --upgrade pip poetry wheel
COPY pyproject.toml $WORKDIR_PATH/pyproject.toml
COPY poetry.lock $WORKDIR_PATH/poetry.lock
RUN poetry config virtualenvs.create false \
    && poetry install --no-root

ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION} AS debug-image
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    WORKDIR_PATH="/code" \
    VENV_PATH="/service_venv"
WORKDIR $WORKDIR_PATH
COPY --from=base-image $VENV_PATH $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"
COPY . $WORKDIR_PATH
RUN poetry config virtualenvs.create false \
    && poetry install

ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}-slim AS build-image
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    WORKDIR_PATH="/code" \
    VENV_PATH="/service_venv"
WORKDIR $WORKDIR_PATH
COPY --from=base-image $VENV_PATH $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"
COPY . $WORKDIR_PATH
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev
RUN pip install --use-feature=in-tree-build --no-cache-dir --compile $WORKDIR_PATH/.
# TODO: Update the name of the service in the last CMD argument
CMD ["uvicorn", "--host=0.0.0.0", "--port=8081", "myservice.main:app"]
