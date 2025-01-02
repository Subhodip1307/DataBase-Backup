dbname="db.sqlite3"
tablenames=[]
ZipName="Backup"
URL=""

##############################################################################
import sqlite3################################################################
import csv####################################################################
import requests###############################################################
import os#####################################################################
import zipfile################################################################
import io#####################################################################
##############################################################################

zipile=zipfile.ZipFile(f"{ZipName}.zip",'w')
connection=sqlite3.connect(dbname)
cursur=connection.cursor()



def senddata(zipname=ZipName,url=URL):
    file={"file":open(f"{zipname}.zip",'rb')}
    data={"folderName":zipname}
    res=requests.post(url=url,files=file,data=data)
    if res.status_code == 200:
        print(res.json())
    else:
        print(res.status_code)
        print(res.json())
        print("someting went wrong")



if not tablenames:
    cursur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablenames=[i[0] for i in cursur.fetchall()]
for tablename in tablenames:
    query=f"SELECT * FROM {tablename}"
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

senddata()   
os.remove(f"{ZipName}.zip")