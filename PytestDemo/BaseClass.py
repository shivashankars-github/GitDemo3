import inspect
import logging

class BaseClass:

    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s  :%(levelname)s  :%(name)s   :%(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger


loggername = inspect.stack()[1][3]
logger = logging.getLogger(loggername)

filehandler = logging.FileHandler("logfille.log")
formatter = logging.Formatter()
fifile
logger.addHandler(filehandler)