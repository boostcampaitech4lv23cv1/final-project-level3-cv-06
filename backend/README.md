## How to use

**환경 설정 파일 생성 위치 (commit 금지, commit 하고 reset --hard가 아닌 기록 전체를 지워주세요)**
backend/.env (DB연결 및 백엔드 관련 설정)
backend/env/key.json (GCP연결)
config/db/.env


```bash
# clone our porject
# put frontend build file to config/nginx (rename folder name "build")
docker compose up -d
```


