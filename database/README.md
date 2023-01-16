# 목적
- Save Paint를 위한 database server 생성 예시를 공유하여 final project의 MLOps pipeline에 적용

# 기능
- docker container인 PostgreSQL database server 생성
- container 생성 시 필요한 field를 포함하는 table 생성
- dummy_dataset_to_db.py를 통한 database 접근

# 사용 방법

## database server 실행 및 table 생성
```bash
cd backend/database
docker compose up -d
```

## ../dataset에 포함된 image 정보를 db에 저장
```bash
python dummy_dataset_to_db.py
```

## database 조회
```bash
PGPASSWORD=mypassword psql -h localhost -p 5432 -U myuser -d mydatabase
```
```sql
\d
select * from savepaint_img_data;
\q
```

## database server 종료 및 container 삭제
```bash
docker compose down -v
```