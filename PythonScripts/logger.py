#This file contains logger initialization

import logging

class log:
    #Initialize logger
    logger = logging.getLogger('Camtasia UI Automation')
    hdlr = logging.FileHandler('App.log',mode='w')
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)
