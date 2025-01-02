# Data-Base-Back-up (SQLITE Guide)
 **As we will work with SQLITE so I will you to suggest you to move only the 'sqlite_backup' folder or the python script to your VPS server,
 this code doesn't have any docker file , but if you want to dockerize it, you can.
<h1>Getting Started</h1>

- Open 'sqlite_backup' folder
- Next open the code python code file in any text editor.

  ***In my case I will use nano editor and as I have opned 'sqlite_backup' folder so my python file name will be 'backupdbSQLite'

   ```bash
   nano backupdbSQLite.py
   ```
- In This Step You will have to provide your Database path (code line number 10)

```bash
dbname="/path/to/your/db.sqlite3"
```
`In the Line 10 of the code file you will see a varibale call 'dbname' just give your database location

`** If you are a beginner then loging in your server as root or run this scpit as root 

- Now You Need to write down your table names of your data base you wanna  get backup or you can keep it empty if you wanna full backup

  ** In this scrript You can backup singel or multiple tables very easily

   ```bash
   tablenames=["tabales_name1","table_name2"]
   ```

   ** In line number 12 of the script add your table name in that 'tablenames' python list one by one
- Now You need specify your backup zip file name (code line number 18)

```bash
  ZipName="Backup{}".format(date.today())
```
** Give any name as you like or you can simpliy change the word 'Backup' with anyother word you want

- Now fill to variable with proper values.

```bash

  TELEGRAM_BOT_API_KEY="" # Telegram BOT API KEY
  TELEGRAM_CHAT_ID="" # Telegram Chat I

```

- Download Python Dependencies with the help of requirements.txt file.

```bash
    pip3 install -r requirements.txt
```
  
After That now we are ready to check the script and then we schedule the task for us
To check it just run the scipt in your vps server like this

```bash
python3 backupdbSQLite.py
```
 ** If you dont get any error while running script then you are ready to go to the next step to schedule it and if you get any error you can knock me in issues section
   
**Now Let's [schedule](../../schedule.md) the Script for Daily Backup
