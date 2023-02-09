# FROM ozoooooh/airflow-2.5.0-py3.9-custom:1.0
# # Install chrome broswer
# USER root
# # RUN apt-get update && apt-get install -y wget unzip \
# #     && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
# #     && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
# #     && apt-get -y update \
# #     && apt-get install -y google-chrome-stable
# RUN apt-get update \
#     && apt-get install -y $DEPS gcc python python-pip libdbus-glib-1-dev wget ttf-wqy-microhei ttf-wqy-zenhei xfonts-wqy libgtk2.0-0\
#     ## Install Chrome
#     && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
#     && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
#     && apt-get update && apt-get install -y google-chrome-stable
# USER airflow

# FROM apache/airflow:2.5.0-python3.9
# COPY requirements.txt /requirements.txt
# RUN pip install --user --upgrade pip \
#     && pip install --no-cache-dir --user -r /requirements.txt
# USER root
# # RUN apt-get update && apt-get install -y wget unzip
# # RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# # RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# # RUN apt-get -y update && apt-get -y install google-chrome-stable
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# RUN apt-get -y update
# RUN apt-get install -y google-chrome-stable


# # USER airflow

# FROM ozoooooh/airflow-2.5.0-py3.9-custom:1.0
# USER root
# RUN apt-get update \
#     && apt-get install chromium -y
# USER airflow


FROM apache/airflow:slim-2.5.1-python3.9
USER root
RUN apt-get update && apt-get install -y libpq-dev gcc
USER airflow
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
