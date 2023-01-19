# How to..

## airflow docker compose 실행

```bash
docker-compose up
```

## postgres 컨테이너 접속

```bash
docker exec -it $(docker ps -aqf name=airflow_reproduct-postgres-1) /bin/sh
```

## postgres db 접속

```bash
PGPASSWORD=airflow psql -h postgres -p 5432 -U airflow -d airflow
```

### SQL 테이블 생성

```sql
create table animal(
    category varchar(10),
    alt varchar(1000) null,
    srcset varchar(1000) null,
    img_path varchar(1000) null,
    img_width smallint null,
    img_height smallint null,
    label varchar(20),
    time Time null
);
update animal
set label = '';
```
## airflow webserver 접속

    http://localhost:8080 접속 후, crawling dag 실행