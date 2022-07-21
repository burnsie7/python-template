FROM python:3.9.0-slim-buster
RUN apt update && apt install -y gnupg && apt install -y software-properties-common && apt install -y build-essential
RUN apt update
RUN apt install -y git-all
COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt
