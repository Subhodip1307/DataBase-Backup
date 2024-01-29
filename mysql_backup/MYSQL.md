# Data-Base-Back-up (MySql Guide)
 **before start I am considering that mysql in installed and running in your system.
 
 ** As we will work with mysql database so then move the 'mysql_backup' folder or just the 'backupMysql.py' to your server of vps

# Features
before starting Let look at the Features and know why you should Use this
- Able to Take Backup of multipule Mysql runing in diffent container (docker images)
- Completely Free and no need to care about stroage (As it's use Telegram to backup)
- Get Daily Backup in your Telegram Chat
- Easy To Setup
- Poltable (will run in any OS) as it's Made with python 
- Easy to Schedule Time For Backup   
 
<h1>Getting Started</h1>

- Open 'mysql_backup' folder and copy it to your server (or  you can just copied the python file and requirements.txt)
- Donwload Virtualenv in your system (if you Already Have you can skip this step)

  ```bash
  pip install virtualenv
        or
  pip3 install virtualenv
        or
  sudo apt-get install python3-virtualenv
  ```
  
- Create a Virtualenv in python ( in my case i will name it as backupenv)

```bash
 syntax: python3 -m venv <env name>
 example: python3 -m venv backupenv
```
- Activate The Virtualenv

```bash
syntax: source/<env name>/bin/acticate
example: source/backupenv/bin/acticate
```

- Download Python Dependencies with the help of requirements.txt file.

  ```bash
    pip3 install -r requirements.txt
  ```
- Next open the code python code file in any text editor.

  ***In my case I will use nano editor and as I have opned 'mysql_backup' folder so my python file name will be 'BackupDatabase.py'

   ```bash
   nano BackupDatabase.py
   ```
   
- In This Step You will have to provide your Database details, Here is a Example That how you should mention your Database Details

```bash
Database_list={
    "EXAMPLE_NAME1":{"HOST":"localhost","USER":"subho","PASSWORD":"subho1234","DATABASE":"github","PORT":3306},
    "EXMAPLE_NAME2":{"HOST":"localhost","USER":"root","PASSWORD":"root1234","DATABASE":"gitlab","PORT":3307}
}
```
Now Let's understand What to Do with it with few step

- At The begining I am giving the name of zipfiles in which I want to get backup of the database (ex: EXAMPLE_NAME1,EXMAPLE_NAME2)

  **If Don't Have multipule Mysql-Server to backup then you can comment or remove the second line or if you ar useing two or more than that mysql runing then write them one by one like this and done forgot use a coma at the
     End of each Deatils
     
- Now Add The Host Name (By default mysql runs on localhost if your mysql is running on another host (ip) then provide the host address)
- Now add The User Name (It's suggested to create a user who have read privilege on your database or you can use root user but it's not suggested). Be sure That User details have privilege on that data base
- Now add the User Password and Database Name and the Port( If you are not useing dcoker to run mysql then the default port for your mysql will be 3306) 
** Sorry to say that if you  wanna whole database backup of a mysql-server for that if have to write down the whole details for each database this limitaion will fix soon 

# Setup TelegramBot

- Now we need to create a Telegram bot ( you can use [BOTFAHER](https://t.me/BotFather) and collect your BOT API Token)
  
      ** I hope You Can create A Bot very easily if not you can watch any youtube tutorial for that

- Next We Need A Chat id to send message to that id ( You Can Use [RAWBOT](https://t.me/raw_data_bot) and collect your chat id )

  **once you message in this id the bot will reply you with your chat id
  
- After Geting Chat-id and BOT API key fill the data in python file

```bash

TELEGRAM_BOT_API_KEY="" # Telegram BOT API KEY
TELEGRAM_CHAT_ID=0000 # Telegram Chat ID # telegram chat id will be a integer so dont use singel or double quotes

```

After That now we are ready to check the script and then we schedule the task for us
To check it just run the scipt in your vps server like this ( I hop you didn't deactivated your virtualenv)

```bash
python3 BackupDatabase.py
```
 ** If you dont get any error while running script then you are ready to go to the next step to schedule it and if you get any error you can knock me in issues section
- Now Deactivate The Virtualenv and Move to the next part with this following command

  ```bash
 deactivate
  ```
   
**Now Let's [schedule](../schedule.md) the Script for Daily Backup
