FROM python:3.10.0-slim-buster

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y --no-install-recommends python3-dev gcc g++ libc-dev musl-dev openssh-client wget libpq-dev && apt-get clean -y
WORKDIR /
# copy over working files
COPY src src/
COPY requirements.txt ./
# dependencies install
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --use-pep517 -r requirements.txt

# Start the container
RUN ls -la
CMD ["python3", "-u", "src/handler.py"]