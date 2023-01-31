# Final Project(Noops)
---
## Setting
[pyenv](https://github.com/pyenv/pyenv) 설치

```sh
# python 환경 설정
pyenv install 3.9.x(our version: 3.9.16)
pyenv global(or local) 3.9.x
pip install pipenv

pipenv --python 3.9.x
pipenv shell
pipenv install
pipenv install
pipenv install --dev
```

```sh
# vue 환경 설정

```
---
## how to use
1. install docker
2. git clone our project
3. move to DEV branch (main yet)
```sh
# mount
mkdir raw_image
touch app.log

docker compose up -d
# check if it works
docker compose logs
```