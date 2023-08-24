FROM python:3.11-slim

LABEL description="Simple fastAPI app for cloudru_test_task"

LABEL maintainer="femakc@yandex.ru"

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./main.py /code

CMD ["uvicorn", "main:app", "--port", "8000"]
