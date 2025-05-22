FROM python:3.10-slim

ENV POETRY_VERSION=1.8.2 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    curl build-essential libgl1-mesa-glx && \
    pip install --upgrade pip

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /app
COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8080
CMD ["poetry", "run", "flask", "--app=app.main", "run", "--host=0.0.0.0"]
