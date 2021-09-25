FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /group_registration_server
WORKDIR /group_registration_server
ADD group_registration_server/requirements.txt /group_registration_server/
RUN pip install -r requirements.txt
ADD group_registration_server /group_registration_server/