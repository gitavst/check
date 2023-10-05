import streamlit as st
from logzero import logger
st.write("the code is going ot check")
try:
  import requests
  logger.info("requests has been imported")
except Exception as e:
  logger.info(f'an error occured: {e}')
  
  
