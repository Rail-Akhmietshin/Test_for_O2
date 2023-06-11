FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


#ENV APP_HOME=/home/project/app
RUN mkdir /project
WORKDIR /project

RUN apt-get update && apt-get install -y netcat gunicorn
RUN curl -sSL https://install.python-poetry.org | python3 -


COPY pyproject.toml .
COPY poetry.lock .

RUN pip3 install poetry
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi


#RUN mkdir -p /home/project

RUN mkdir /project/static

COPY . /project

RUN chmod a+x *.sh