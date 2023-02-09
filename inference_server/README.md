## How to set up
```bash
conda create -n infer python=3.9
source activate infer
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=11.0 -c pytorch
pip install "fastapi[all]"
pip install google-cloud-storage
pip install gunicorn

cd PaintTransformer_pkg
python setup.py develop
```

구글 GCS키를 env폴더에 넣어줍니다.

```bash
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:30001 #(your port)
```