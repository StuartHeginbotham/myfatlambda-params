import logging
import sys 

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')

logging.info('Fat Lambda Params ****STARTED****')

try:
    logging.info(f'Fat Lambda started, param is: {sys.argv[1]}')
except:
    logging.info(f'Fat Lambda started but no input paramter supplied')

