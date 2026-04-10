FROM python:3.12

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy dependency files
COPY pyproject.toml poetry.lock /app/

# Install dependencies (NEW syntax)
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-root

# Copy full project
COPY . /app/

# Run FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]