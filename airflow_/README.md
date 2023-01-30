# How to..

## airflow docker compose 실행

```bash
docker-compose up
```
## airflow webserver 접속

    1. http://localhost:8080 접속.
    2. 아이디:airflow 비번:airflow 입력.
    3. crawling dag 실행
---

## postgres 컨테이너 접속하는 방법

```bash
docker exec -it $(docker ps -aqf name=postgres-1) /bin/sh
```

## postgres db 접속하는 방법

```bash
PGPASSWORD=airflow psql -h postgres -p 5432 -U airflow -d airflow
```
