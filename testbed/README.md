# aistage server 개발 환경 설정 방법

## pyenv prerequisite 설치
```bash
apt-get update
apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev
```

## pyenv 설치
---
```bash
apt-get update
apt-get install curl
curl https://pyenv.run | bash
```
### path 설정
```bash
vi ~/.bashrc
```
```bash
# ~/.bashrc에 아래 내용 추가
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

eval "$(pyenv virtualenv-init -)"
```
### locale 설정(pyenv 치면 오류메세지 뜨는 것 방지)
```bash
apt-get install locales
locale-gen en_US.UTF-8
```
```bash
source ~/.bashrc
```
---
## python 설치
```bash
pyenv install 3.9.16
```
### python 전역 설정
```bash
pyenv global 3.9.16
```
---
## pipenv 설치
```bash
pip install pipenv
```

## final project clone
```bash
git clone https://github.com/boostcampaitech4lv23cv1/final-project-level3-cv-06.git
```
```bash
cd final-project-level3-cv-06
```
## pipenv로 가상환경 생성
```bash
pipenv install
```
## google-chrome, chromedriver 설치
### google-chrome 설치
```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 
apt install ./google-chrome-stable_current_amd64.deb 
google-chrome --version
```
### chromedriver 설치
https://chromedriver.chromium.org/downloads 에서 google-chrome과 동일한 버전 다운로드
```bash
wget https://chromedriver.storage.googleapis.com/109.0.5414.74/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin/chromedriver
chown root:root /usr/bin/chromedriver
chmod +x /usr/bin/chromedriver
```

