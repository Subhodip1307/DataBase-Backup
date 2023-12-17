# Script scheduleing

In This Section We will see how can we schedule our Data Base backup Script So we can get our backup after a fixed time

# Getting Started

We will use corn job for running our script on fixed time
 
 **To know more about it , [Click Here](https://www.hostinger.in/tutorials/cron-job)

- In most of the unix system corn job comes pre installed so to check that run the following script in your terminal

```bash

crontab -e

```
 **if you any error after runing that you need to install it with following script then run the first command
 
 ```bash
    sudo apt install cron
 ```

- After runing the first command (if you are running this first time it will ask to choose a text editor , choose any of your favorite) a page will open in your screen  , scroll down and and write this code

```bash
0 18 * * *  python3 /root/backupdbSQLite.py  /root/script2.log 2>&1
```
Let understand What is written here in 3 parts

- In first part '0 18 * * *' there i have written this. This part of code mean run the scipt at 18th hour of a day and run it every day

    ** If you want differnt time then  you visit [crontab](https://crontab.guru/) website 

- In the second part we are running your script in my case the script name is 'backupdbSQLite.py' and it's in root directory

- In the last and final part  I have specified a path where the error log will save (if the script ever get error it you see it from the log file) , you can give any location as you want

- After writing all of this just save the corn file and exit and you are all done

** now you will get daily backup in your telegram in a specified time **