import inspect
import logging


class BaseClass:

    def getLogger(self):

        loggerName = inspect.stack()[1][3]
        # this object is responsible to log everything, it will capture the test file name
        logger = logging.getLogger(loggerName)  # logger is an object responsible of printing   #WHAT TO PRINT

        fileHandler = logging.FileHandler('logfile.log')  # indicate where it should print   #WHERE TO PRINT
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # HOW TO PRINT (FORMAT)
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)  # Debug will be skipped

        return  logger

