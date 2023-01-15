# 목적
- DB, Storage에 저장된 image 데이터 중 inference 되지 않은 image를 모아 inference하여 DB, Storage 업데이트 하는 기능 → final project의 MLOps pipeline에 적용

# 기능
- psycopg2로 DB 조회
- Minio에서 이미지 파일 불러오기
- 불러온 이미지 파일 전송할 수 있도록 encoding (base64 encoding → ascii)
- FastAPI로 inference backend 서버 구성(input: 원본 image / output: gif)
- 전송된 response를 decoding (base64 decoding → gif)

# 사용 방법 (database server, storage_minio 가 실행된 상태 및 dummy data가 들어가있어야 테스트 가능)
-------------------------- 작업 중 -------------------------
<!-- ## database server 실행 및 table 생성
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
``` -->