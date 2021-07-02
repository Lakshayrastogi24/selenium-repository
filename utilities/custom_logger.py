import logging
import inspect

def customLogger(lgLv=logging.INFO):
    loggerName=inspect.stack()[1][3]
    logger=logging.getLogger(loggerName)

    logger.setLevel(level=logging.DEBUG)

    fileHandler=logging.FileHandler('automation.log',mode='a')
    fileHandler.setLevel(lgLv)

    formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger