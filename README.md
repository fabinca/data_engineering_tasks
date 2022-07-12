# data_engineering_tasks

### System:

Ubuntu


### Requirements: 

docker
mongod
python3
pymongo, csv, datetime, django, matplotlib


### start docker for mongodb: 

-make sure you got the mongodb doker image: 

check: 

sudo docker images

otherwise pull it from docker.hub: 

sudo docker pull mongo

make sure the port you want to use is free (here: 27017)

sudo lsof -iTCP -sTCP:LISTEN -n -P

otherwise kill that process or choose a different port


### Connect: 

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


