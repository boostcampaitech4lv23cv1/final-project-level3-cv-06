FROM python:3.9

WORKDIR /app

# 상대경로 절대경로 둘 다 가능
COPY ../app .

COPY ../Pipfile .
COPY ../Pipfile.lock .

RUN apt-get update && apt-get install -y \
libgl1-mesa-glx \
libglib2.0-0

RUN pip install pipenv

RUN pipenv install

CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]