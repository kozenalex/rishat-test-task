FROM python:latest

RUN pip3 install poetry

WORKDIR $HOME/
COPY . .
RUN poetry install

RUN make migrate

RUN make addadmin

CMD ["make", "start"]