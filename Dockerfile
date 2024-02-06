FROM python:3.10-slim

WORKDIR /
# version lock keep shit safe
RUN pip install poetry==1.7.1
# copy over working files
COPY pyproject.toml poetry.lock ./
COPY src ./
# dependencies install
RUN poetry install --no-dev && rm -rf $POETRY_CACHE_DIR

# Start the container
CMD ["poetry", "run", "python", "-u", "src/handler.py"]