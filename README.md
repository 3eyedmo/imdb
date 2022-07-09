# discription :
this project aimed at scraping information of top 250 movies of IMDB.

# installation :
### using docker
```bash
cd app
docker-compose up --build
```
### in linux
```bash
cd app
python3 -m pip install -r requirements.txt
cd crawl
scrapy crawl imdb_top_250 -o data/info.json
```
