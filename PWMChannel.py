import pigpio
import time


class PWMInputDevice:

  def __init__(self, pin=None):
    self.last_activated = False
    self.pulse_width = False
    self.pin = pin
    self.pi = pigpio.pi()
    self.pi.callback(self.pin, pigpio.RISING_EDGE, self.__when_activated)
    self.pi.callback(self.pin, pigpio.FALLING_EDGE, self.__when_deactivated)

  def __when_activated(self, gpio, level, tick):
    self.last_activated = time.time()

  def __when_deactivated(self, gpio, level, tick):
    self.pulse_width = time.time() - self.last_activated
