FROM python:3.12-slim

RUN pip install --no-cache-dir uv

WORKDIR /app

ENV PYTHONPATH=/app

COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev --frozen

COPY backend/ ./backend/
COPY frontend/ ./frontend/
COPY config.toml .

EXPOSE 8501

CMD ["uv", "run", "streamlit", "run", "frontend/app.py", "--server.address=0.0.0.0"]
