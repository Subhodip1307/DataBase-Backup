# Data-Base-Back-up (MySql Guide)
 **before start I am considering that mysql in installed and running in your system.
 ** As we will work with mysql database so then move the 'mysql_backup' folder or just the 'backupMysql.py' to your server of vps
<h1>Getting Started</h1>

- Open 'mysql_backup' folder (not required you just copied the python file)

- Download Python Dependencies with the help of requirements.txt file.

  ```bash
    pip3 install -r requirements.txt
  ```
- Next open the code python code file in any text editor.

  ***In my case I will use nano editor and as I have opned 'sqlite_backup' folder so my python file name will be 'backupdbSQLite'

   ```bash
   nano backupMysql.py
   ```
- In This Step You will have to provide your Database details

```bash
connection = mysql.connector.connect(
  host="localhost",
  user="subhodip",
  password="subho@12",
  database="mydatabase"
)
```
So Here I am giving my user name of my data base and password and the table I want Backup (Be sure That The data base User details You are Providing have privilege on that data base)

- Now You Need to write down your table names of your data base you wanna  get backup or you can keep it empty if you wanna full backup

  ** In this scrript You can backup singel or multiple tables very easily

   ```bash
   tablenames=["tabales_name1","table_name2"]
   ``
   ** In line number 17 of the script add your table name in that 'tablenames' python list one by one
   
- Now You need specify your backup zip file name (code line number 18)

```bash
  ZipName="Backup{}".format(date.today())
```
** Give any name as you like or you can simpliy change the word 'Backup' with anyother word you want

  - Now we need to create a Telegram bot ( you can use [BOTFAHER](https://t.me/BotFather) and collect your BOT API Token

      ** I hope You Can create A Bot very easily if not you can watch any youtube tutorial for that

- Next We Need A Chat id to send message to that id ( You Can Use [RAWBOT](https://t.me/raw_data_bot) and collect your chat id )
- After Geting Chat-id and BOT API key fill the data in python file

```bash

  TELEGRAM_BOT_API_KEY="" # Telegram BOT API KEY
  TELEGRAM_CHAT_ID="" # Telegram Chat I

```

After That now we are ready to check the script and then we schedule the task for us
To check it just run the scipt in your vps server like this

```bash
python3 backupMysql.py
```
 ** If you dont get any error while running script then you are ready to go to the next step to schedule it and if you get any error you can knock me in issues section
   
**Now Let's [schedule](../schedule.md) the Script for Daily Backup
