try:
  import requests
  logger.info("requests has been imported")
except Exception as e:
  logger.info(f'an error occured: {e}')
  
  
