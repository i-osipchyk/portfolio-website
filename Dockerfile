FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev python3-venv

WORKDIR /app

COPY requirements.txt /app/

RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app

ENTRYPOINT ["venv/bin/python"]

CMD ["app.py"]
