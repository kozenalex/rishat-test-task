FROM python:latest

RUN pip3 install poetry

WORKDIR /app
ADD . /app
RUN poetry install

RUN make migrate

RUN make addadmin

CMD ["make", "localstart"]