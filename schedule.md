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
** if you are running the command for the First time you will able to see something like this
<center>
 
 ![photo_2024-01-30_06-29-02](https://github.com/Subhodip1307/DataBase-Backup/assets/111901004/89e66097-b247-4166-a9df-806a141b3fb9)

</center>
 Its Just asking you to choose any text editor , you can chose any one of them ( I would like to suggest you to chose nano editor for that just presss 1 and the enter) 

- After runing the first command a page will open in your screen  , scroll down and and write this code

```bash
sytax: */5 * * * * /path to your/<env name>/bin/python3 BackupDatabase.py /<location for a log files>/<file name>.log 2>&1
example: */5 * * * * /root/Backupenv/bin/python3 BackupDatabase.py /root/mysqlbackupcode.log 2>&1
```
- Now save The changes ( ctrl +s ) and exit (ctrl+x) and you will see the code wll send backup in each 5 mins ( it was just testing purpose)
- If you get backup after few mintes then its working fine or if get an error the copy code form the path to BackupDatabase.py (ex: /root/Backupenv/bin/python3 BackupDatabase.py)
  and paste it in your VPS terminal and press enter will able to know the problem or you can check the log with the following command
  ```bash
  syntax : cat /<location for a log files>/<file name>.log
  example: cat /root/mysqlbackupcode.log
  ```
- Now If Every Thing went well you didn't have any problem now its set correct time for backup
- Open The crontab editor again and change the "*/5 * * * *" with "0 18 * * *"
- Now is Should Look like this 

```bash
sytax: 0 18 * * * /path to your/<env name>/bin/python3 BackupDatabase.py /<location for a log files>/<file name>.log 2>&1
example: 0 18 * * * /root/Backupenv/bin/python3 BackupDatabase.py /root/mysqlbackupcode.log 2>&1
```

Let understand What is written here in 3 parts

- In first part '0 18 * * *' there i have written this. This part of code mean run the scipt at 18th hour of a day and run it every day

    ** If you want differnt time then  you visit [crontab](https://crontab.guru/) website 

- In the second part we are running your script in my case the script name is 'backupdbSQLite.py' and it's in root directory

- In the last and final part  I have specified a path where the error log will save (if the script ever get error it you see it from the log file) , you can give any location as you want

- After writing all of this just save the corn file and exit and you are all done

** now you will get daily backup in your telegram in a specified time **
