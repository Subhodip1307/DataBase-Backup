# Data-Base-Back-up (SQLITE Guide)

<h1>Getting Started</h1>

- Open 'sqlite_backup' folder
- Download Python Dependencies with the help of requirements.txt file.

  ```bash
    pip3 install -r requirements.txt
  ```
- Next open the code python code file in any text editor.

  ***In my case I will use nano editor and as I have opned 'sqlite_backup' folder so my python file name will be 'backupdbSQLite'

   ```bash
   nano backupdbSQLite.py
   ```
- In This Step You will have to provide your Database path

```bash
dbname="/path/to/your/db.sqlite3"
```
In the Line 6 of the code file you will see a varibale call 'dbname' just give your database location

** If you are a beginner then loging in your server as root or run this scpit as root 

- Now You Need to write down your table names of your data base you wanna  get backup

  ** In this scrript You can backup singel or multiple tables very easily

   ```bash
   tablenames=["tabales_name1","table_name2"]
   ```

   ** In line number 7 of the script add your table name in that 'tablenames' python list one by one

  - Now we need to create a Telegram bot ( you can use [BOTFAHER](https://t.me/BotFather) and collect your BOT API Token

      ** I hope You Can create A Bot very easily if not you can watch any youtube tutorial for that

- Next We Need A Chat id to send message to that id ( You Can Use [RAWBOT](https://t.me/raw_data_bot) and collect your chat id )
   
    
