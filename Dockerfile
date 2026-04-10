# ---- Builder Stage ----
FROM python:3.12-slim AS builder

WORKDIR /app

# Install Poetry + export plugin
RUN pip install --no-cache-dir poetry poetry-plugin-export

# Copy dependency files
COPY pyproject.toml poetry.lock ./

# Export dependencies to requirements.txt
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --only main

# ---- Final Stage ----
FROM python:3.12-slim AS final

WORKDIR /app

# Install dependencies directly with pip (no Poetry overhead)
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the app source
COPY app/ ./app/

# Non-root user for security
RUN useradd -m appuser
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]