import logging

def test_loggingDemo():

    #this object is responsible to log everything, it will capture the test file name
    logger = logging.getLogger(__name__) #logger is an object responsible of printing   #WHAT TO PRINT

    fileHandler = logging.FileHandler('logfile.log') #indicate where it should print   #WHERE TO PRINT
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s") #HOW TO PRINT (FORMAT)
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler) #filehandler object

    logger.setLevel(logging.INFO) #Debug will be skipped
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happened")
    logger.critical("Critical issue")
