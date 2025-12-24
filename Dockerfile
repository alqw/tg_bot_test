FROM astral/uv:python3.12-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

WORKDIR /src

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-install-project --no-dev

FROM python:3.12-slim-trixie

WORKDIR /app

COPY --from=builder /src/.venv /app/.venv

ENV PATH="/app/.venv/bin:$PATH"

COPY . .

CMD [ "uv", "run", "main.py" ]