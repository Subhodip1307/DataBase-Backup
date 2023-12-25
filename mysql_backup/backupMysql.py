import mysql.connector
import asyncio
import csv
import telegram
import os
import zipfile
import io
from datetime import date

connection = mysql.connector.connect(
  host="localhost",
  user="qrjgh",
  password="Qrjgh@dm1n",
  database="qrcodejgh"
)

tablenames=[] # Type table Names
ZipName=f"backup_{date.today()}"
TELEGRAM_BOT_API_KEY="" # Telegram BOT API KEY
TELEGRAM_CHAT_ID="" # Telegram Chat ID # Kepp empty if you want full db backup


zipile=zipfile.ZipFile(f"{ZipName}.zip",'w')
cursur=connection.cursor()
if not tablenames:
    cursur.execute("SHOW TABLES;")
    tablenames=[i[0] for i in cursur.fetchall()]
for tablename in tablenames:
    query=f"SELECT * FROM {tablename} ';"
    cursur.execute(query)
    headers=[header[0] for header in cursur.description]
    output=cursur.fetchall()
    csv_file=io.StringIO()
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(headers)
    for i in output:
        csv_writer.writerow(i)
    csv_file.seek(0)
    zipile.writestr(f"{tablename}.csv",csv_file.read())
    csv_file.close()
connection.commit()
connection.close()
zipile.close()

async def send_message_async():
    bot_token = TELEGRAM_BOT_API_KEY
    chat_id = TELEGRAM_CHAT_ID
    bot = telegram.Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text='QRJGH Whole Backup')
    await bot.send_document(chat_id=chat_id, document=open(f'{ZipName}.zip', 'rb'))
async def main():
    await send_message_async()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    os.remove(f"{ZipName}.zip")
