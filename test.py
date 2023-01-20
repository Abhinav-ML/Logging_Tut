import logging

logging.basicConfig(filename="test.log",level = logging.INFO)
logging.info("This is my very first code for logging")
logging.warning("This will try to log some warning messages")
logging.error("Here some error occured from the system")
l = [1,2,3,4,5,6,7]
for i in l:
    if i == 2:
        logging.info("l : %s",l)
        logging.warning("Here 2 occured !!!")

logging.shutdown()