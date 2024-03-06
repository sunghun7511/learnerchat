FROM python:3.11
WORKDIR /app

RUN pip install --upgrade pip

RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction --no-root --no-cache --no-dev

COPY . .

ENTRYPOINT ["poetry", "run", "uvicorn", "learnerchat.app:create_app", "--host", "0.0.0.0", "--port", "1213"]
