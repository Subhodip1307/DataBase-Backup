# MYSQL Backup With Docker

Here we will understand database if its under a docker-container ( you may have more than one).

Before starting we need to know the network of the container in which your database is runing. To Know that we need to gothrough all the following steps.


- The Network Name will be over the name of your project folder name, suppose I have a folder name "Backup" and its contains all of my code and my dockerfile now then the default network name will be 'backup_default'.
- To be sure run 'docker network ls ' and you will able to see all docker network running in your host machine . And then you will able to see your desired network

- Now Clone The Repo the take this 
