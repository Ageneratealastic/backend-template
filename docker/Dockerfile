# 多阶段构建
FROM python:3.11-slim AS builder
WORKDIR /app
COPY pyproject.toml .
RUN pip install --user hatchling && hatch build

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY src/ ./src/
COPY alembic/ ./alembic/
COPY alembic.ini .
ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000
CMD ["uvicorn", "src.myapp.main:app", "--host", "0.0.0.0", "--port", "8000"]