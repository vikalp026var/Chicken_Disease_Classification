import logging
import os
import sys 
from datetime import datetime

''''File name is defined '''
file_name=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

''' logs path '''
log_path=os.path.join(os.getcwd(),'logs',file_name)

''' make the directory '''
os.makedirs(log_path,exist_ok=True)

'''Log file path is defined '''

LOG_FILE_PATH=os.path.join(log_path,file_name)

''' logging basic confriguration defined '''

logging.basicConfig(filename=LOG_FILE_PATH,
                    format="[%(asctime)s]%(lineno)d %(name)s-%(levelname)s -%(message)s",
                    level=logging.INFO)