FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y python python-pip
RUN pip install gunicorn

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py ./
COPY templates ./templates

EXPOSE 5000
CMD ["gunicorn", "-w", "10", "-b", "0.0.0.0:5000", "app:app"]
