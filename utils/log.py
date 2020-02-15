import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

fh = logging.FileHandler(os.path.join(os.getcwd(), 'crm_py.log'))
fh.setLevel(logging.INFO)
fh.setFormatter(logging.Formatter('[%(process)d] [%(thread)d] [%(asctime)s] [%(levelname)s] [%(filename)s] [%(funcName)s] [%(lineno)d] %(message)s'))

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(logging.Formatter('[%(process)d] [%(thread)d] [%(asctime)s] [%(levelname)s] [%(filename)s] [%(funcName)s] [%(lineno)d] %(message)s'))

logger.setLevel(logging.INFO)
logger.addHandler(fh)
logger.addHandler(ch)








