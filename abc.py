import streamlit as st
from logzero import logger
import subprocess
import time
import ast


st.write("check")
logger.info("Initiating the process")
start_time = time.time()
last_save_time_1min = start_time
last_save_time_5min = start_time
data_1min = []
data_5min = []

output = subprocess.Popen([f"{sys.executable}", 'sample.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

for line in iter(output.stdout.readline, b''):
 
 current_time = time.time()
 logger.info("check 1")


 if current_time - last_save_time_1min >= 60:
     logger.info("written to 1min DB")
     last_save_time_1min = current_time


 logger.info("check 5")
  
 if current_time - last_save_time_5min >= 60:
     logger.info("written to 1min DB")
     last_save_time_5min = current_time
