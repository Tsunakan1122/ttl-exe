# Version 1.0.1
import sys
import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s:%(name)s - %(message)s", filename="ttl-exe.log")

argc=sys.argv
ttlexe="C:\\Program Files (x86)\\teraterm\\ttpmacro.exe"
try:
    ttllist=os.listdir(argc[1])

    for file in ttllist:
        if file.lower().endswith(".ttl"):
            file=argc[1]+"\\"+file
            file=os.path.abspath(file)
            logging.info("Start {}".format(file))
            subprocess.run([ttlexe, file], stdout=True, check=True, shell=True)

except IndexError as e:
    logging.error("type: "+str(type(e)))
    logging.error("args: "+str(e.args))
    logging.error("Error: "+str(e))

except Exception as e:
    logging.error("type: "+str(type(e)))
    logging.error("args: "+str(e.args))
    logging.error("Error: "+str(e))

finally:
    logging.info("Stop ttl-exe")