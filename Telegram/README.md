# DataBase-Backup
<h1>Overview</h1>

This Python script provides a convenient and fun way to back up your database data using a Telegram bot. Instead of relying on traditional backup methods, this script leverages the simplicity and accessibility of Telegram to deliver your database backups directly to you.

<h1>Features</h1>
<b>Telegram Integration:</b> Receive your database backups seamlessly through Telegram, making it easy to stay informed about the status of your backups.

<b>Scheduled Backups:</b> Set up scheduled backups to ensure regular updates of your database data without manual intervention.

<b>Compact Archive Format:</b> The script exports database data into a compact and efficient CSV file, ensuring efficient storage and easy retrieval.

## Supported Database Systems

This script currently supports the following database systems:

- **SQLite**: A lightweight, file-based database system. Perfect for small to medium-sized applications.
- **MYSQL/MYSQL-SERVER**: MySQL is a relational database management system (RDBMS) that uses Structured Query Language (SQL) to store, manage, and retrieve data
- Comming more soon.....

## Limitations
- Only 50 M.B. of data can be send at a time (hence suitable for only samll projects).
- No Error Handeling
  
<h1>Getting Started</h1>

- Set up Telegram bot
- To create a Telegram bot ( you can use [BOTFAHER](https://t.me/BotFather) and collect your BOT API Token)
  
      ** I hope You Can create A Bot very easily if not you can watch any youtube tutorial for that

- Next We Need A Chat id to send message to that id ( You Can Use [RAWBOT](https://t.me/raw_data_bot) and collect your chat id )

  **once you message in this id the bot will reply you with your chat id

- Docker installed and set-up in your system
            
            or,

- Install Python to your system (If you wanna run the code directly in host machine)


- [SQLITE](sqlite_backup/DBSQLITE.md)
- [MYSQL/MYSQL-SERVER](mysql_backup/MYSQL.md)
