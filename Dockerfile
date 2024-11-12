FROM python:3.13-slim 

RUN pip install -U poetry && \ 
    poetry config virtualenvs.create false

RUN mkdir -p /code/app && chmod 755 /code/app

WORKDIR /code/

COPY pyproject.toml poetry.lock /code/

RUN poetry install --no-dev --no-interaction --no-ansi

COPY ./app /code/app

ENV PYTHONPATH=/usr/local/bin/python3.12

RUN chmod +x /usr/local/bin/poetry

EXPOSE 8000

CMD ["poetry","run","uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
