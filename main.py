from sensor.exception import SensorException
import os 
import sys

from sensor.logger import logging

def test_exception():
    try:
        logging.info("yaha pe error ayegi division by zero wali")
        a = 1/0
    except Exception as e:
        raise SensorException(e,sys)    



if __name__ == "__main__":  # module controller
    try:
        test_exception()
    except Exception as e:
        print(e)