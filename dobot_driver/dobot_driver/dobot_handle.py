from dobot_driver.interface import Interface
from multiprocessing import Manager

manager = Manager()
lock = manager.Lock()
bot = Interface('/dev/ttyUSB0', lock)
