# ---------- build stage ----------
FROM ghcr.io/astral-sh/uv:debian AS builder
WORKDIR /app

ENV UV_SYSTEM_PYTHON=1
RUN --mount=type=cache,target=/root/.cache/uv true

COPY pyproject.toml uv.lock ./
RUN touch README.md
RUN uv sync -q

COPY src src

# ---------- runtime stage ----------
FROM gcr.io/distroless/python3-debian12:nonroot
WORKDIR /app

# runtime needs the uv binary and site-packages we just built
COPY --from=builder /usr/local /usr/local
# copy your code and hand ownership to the unprivileged user
COPY --from=builder --chown=nonroot:nonroot /app /app

# good hygiene
ENV PYTHONUNBUFFERED=1

USER nonroot
ENTRYPOINT ["python", "-m", "src.{{cookiecutter.package_name}}.hello"]
