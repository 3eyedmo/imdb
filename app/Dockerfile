FROM python:3.9.12-slim-buster
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD cd crawl && \
    scrapy crawl imdb_top_250 -o data/info.json