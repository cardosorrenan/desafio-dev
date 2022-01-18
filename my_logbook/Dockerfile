FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /opt/my_logbook
COPY . .
RUN python -m pip install --upgrade pip
RUN python -m pip install --upgrade setuptools
RUN pip install -r requirements.txt