import sys
import os
import subprocess
import time
from datetime import datetime

argc=sys.argv
ttlexe="C:\\Program Files (x86)\\teraterm\\ttpmacro.exe"
try:
    ttllist=os.listdir(argc[1])

    for file in ttllist:
        if file.lower().endswith(".ttl"):
            file=argc[1]+"\\"+file
            file=os.path.abspath(file)
            subprocess.run([ttlexe, file], stdout=True)
            time.sleep(10)
except IndexError as e:
    errlog=open("error.log", "a", encoding='UTF-8')
    errlog.write(str(datetime.now())+"\n")
    errlog.write("type: "+str(type(e))+"\n")
    errlog.write("args: "+str(e.args)+"\n")
    errlog.write("Error: "+str(e)+"\n")
    errlog.close()
except Exception as e:
    errlog=open("error.log", "a", encoding="UTF-8")
    errlog.write(str(datetime.now())+"\n")
    errlog.write("type: "+str(type(e))+"\n")
    errlog.write("args: "+str(e.args)+"\n")
    errlog.write("Error: "+str(e)+"\n")
    errlog.close()