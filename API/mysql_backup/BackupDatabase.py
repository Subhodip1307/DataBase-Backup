Database_list={
    "EXAMPLE_NAME1":{"HOST":"localhost","USER":"subho","PASSWORD":"subho1234","DATABASE":"github","PORT":3306},
    "EXMAPLE_NAME2":{"HOST":"localhost","USER":"root","PASSWORD":"root1234","DATABASE":"gitlab","PORT":3307}
}

url=""

#########################################################################################################
import mysql.connector###################################################################################
import csv###############################################################################################
import requests##########################################################################################
import os################################################################################################
import zipfile###########################################################################################
import io################################################################################################


def senddata(zipname):
    file={"file":open(f"{zipname}.zip",'rb')}
    data={"folderName":zipname}
    res=requests.post(url=url,files=file,data=data)
    if res.status_code == 200:
        print(res.json())
    else:
        print(res.status_code)
        print(res.json())
        print("someting went wrong")

for items in Database_list:
    tablenames=[]
    zipile=zipfile.ZipFile(f"{items}.zip",'w')
    connection = mysql.connector.connect(
       host=Database_list[items]["HOST"],
       user=Database_list[items]["USER"],
       password=Database_list[items]["PASSWORD"],
       database=Database_list[items]["DATABASE"],
       port=Database_list[items]["PORT"]
    )
    cursur=connection.cursor()
    cursur.execute("SHOW TABLES;")
    tablenames=[i[0] for i in cursur.fetchall()]
    for tablename in tablenames:
        query=f"SELECT * FROM {tablename} ;"
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
    print("The backup for {} is done".format(items))
    senddata(items)
    print("Deleting the zip")
    os.remove(f"{items}.zip")
