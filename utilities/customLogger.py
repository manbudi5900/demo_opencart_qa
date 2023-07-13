import logging
import os

class logGen():
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        # FileHandler() method takes location and path of log file
        fileHandler = logging.FileHandler('logs/logfile.log')
        # Formatter() method takes care of the log file formatting
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        # addHandler() method takes fileHandler object as parameter
        logger.addHandler(fileHandler)
        # setting the logger level
        logger.setLevel(logging.DEBUG)
        return logger