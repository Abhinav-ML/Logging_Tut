import logging

logging.basicConfig(filename='test3.log',level=logging.INFO,format= '%(levelname)s %(name)s %(asctime)s %(message)s ')
logging.info('functionality of logging with real problems ')

def divide(a,b):
    logging.info("User has entered %s and %s",a,b)
    try:
        logging.info("We are into the function")
        div = a/b
        logging.info("Operation done successfullly!!")
        logging.info("Result is %s",div)
    except Exception as e:
        logging.exception(e)

    # return a/b
divide(5,3)