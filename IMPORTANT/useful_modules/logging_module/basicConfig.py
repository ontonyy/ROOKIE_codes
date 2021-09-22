import logging

'''It seemed to me that 'basicConfig' is main attribute 
in module logging, and here is some simple examples: '''

# logging.basicConfig(format="%(process)d-%(levelname)s-%(message)s",
#                     level=logging.WARNING)
# logging.warning('Warning info')

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logging.info('Info log')