# data_engineering_tasks

### System:

Ubuntu


### Requirements: 

docker or mongod
python3
pymongo, csv, datetime, django, matplotlib


make sure the port you want to use is free (here: 27017)

sudo lsof -iTCP -sTCP:LISTEN -n -P

otherwise kill that process or choose a different port


### start docker container: 

-make sure you got the mongodb docker image: 

check: 

sudo docker images

otherwise pull it from docker.hub: 

sudo docker pull mongo

start the docker container: 

docker run -d -p 27017:27017 --name test-mongo mongo:latest

check if it's running with 

docker ps 

or

sudo lsof -iTCP -sTCP:LISTEN -n -P



### or with mongod: 

create directory for your database: 

mkdir mongo_data

connect with mongod & specify your directory:

mongod --dbpath mongo_data

or if you changed the port: 

mongod --dbpath mongo_data --port [portnumber]


### Load data into the db by running: 

python3 upload_csv.py


### Create a scatterplot with the data by running:

python3 scatter_plot.py


### Run Django App by:

cd turbines

python3 manage.py runserver


