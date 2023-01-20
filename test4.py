import logging

logging.basicConfig(filename='test4.log',level='INFO',format='%(levelname)s %(name)s %(asctime)s %(message)s')

logging.info("This program is related to file handling")

try:
    logging.info("Trying to read a file")
    # with open('intro.txt', 'r') as f:
    #     a = f.read()
    # logging.info("Context of file \n %s",a)
    # logging.info("File reading completed")
    with open('abhinav.txt', 'r') as f:
        a = f.read()
    logging.info("Context of file \n %s",a)
    logging.info("File reading completed")
except Exception as e:
    logging.critical("This is serious thing. Think about it !!!")
    logging.error(e)
    # logging.exception(e)


