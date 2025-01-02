# Data-Base-Back-up (MySql Guide)
 **before start I am considering that you have read the [initial-page](../README.md).
 
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

## Database Set-up
It's prefered to create a new database user which only have the read permission over the database,in order to do that use the following commands :-

- Enter to mysql shell from where you can run your commands

- Createing The user

```bash
syntax: CREATE USER '<new user name>'@'localhost' IDENTIFIED BY '';
example: CREATE USER 'trisha'@'localhost' IDENTIFIED BY '';
```
- Granting permissions

```bash
syntax: GRANT SELECT ON <DB name>.* TO '<user-name>'@'localhost';
example: GRANT SELECT ON mydb.* TO 'trisha'@'localhost';
```
- Reloads privileges

```bash
FLUSH PRIVILEGES;
```

## Project Set-Up

- Open 'mysql_backup' folder and copy it to your server (or  you can just copied the python file and requirements.txt)

- In This Step You will have to provide your Database details, Here is a Example That how you should mention your Database Details
  ** First Look at the example then I will explain all one bye one.

```bash
Database_list=
{
    "EXAMPLE_NAME1":{"HOST":"localhost","USER":"subho","PASSWORD":"subho1234","DATABASE":"github","PORT":3306},
    "EXMAPLE_NAME2":{"HOST":"localhost","USER":"root","PASSWORD":"root1234","DATABASE":"gitlab","PORT":3307}
}
```

 ** If you Have Backup Two Databases to backup just provide the Same details two times with different Key name (ex: in my example is 'EXAMPLE_NAME1' and the port should be the same).

Now Let's understand What to Do with it with a few step

- At The beginning I am giving the name of zip files in which I want to get a backup of the database (ex: EXAMPLE_NAME1,EXMAPLE_NAME2)

  **If Don't Have multipule Mysql-Server to backup then you can comment or remove the second line or if you ar using two or more than that mysql runing then write them one by one like this and done forgot use a coma at the
     End of each Deatils
     
- Now Add The Host Name (By default mysql runs on localhost if your mysql is running on another host (ip) then provide the host address)
- Now add The User Name (It's suggested to create a user who have read privilege on your database or you can use root user but it's not suggested). Be sure That User details have privilege on that data base.
- Now add the User Password and Database Name and the Port( If you are not using docker to run mysql then the default port for your mysql will be 3306)
  

** If You are running a Docker Container in Your System and the port is exposed to the Host machine. For That Case, the host will be the 127.0.0.1 and enter the other credentials like password, user, and password port according to your docker container.

** If You Are Using Docker Container and the ports are not exposed to the Host, then You need To follow This [documentation](mysql_with_docker.md)

** If you are runing the backup code using docker then , you can now jump to the [schedule](../../schedule.md) section

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
   
- Now fill to variable with proper values.

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
**Now Let's [schedule](../../schedule.md) the Script for Daily Backup
