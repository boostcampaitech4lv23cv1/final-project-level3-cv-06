# 목적
- storage server 예시 공유 → final project의 MLOps pipeline에 적용

# 기능
- storage(MINIO) docker server 생성
- storage(MINIO) server 파일 삽입

# 사용 방법

## storage server 실행
```bash
cd backend/storage_minio
docker compose up -d
```

## ../dataset에 포함된 image를 storage에 저장
```bash
python dummy_data_to_storage.py
```

## storage 접속
- localhost:9001

## storage server 종료 및 container 삭제
```bash
docker compose down -v
```