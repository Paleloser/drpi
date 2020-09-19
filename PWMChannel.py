from gpiozero import DigitalInputDevice
import time as time


class PWMInputDevice(DigitalInputDevice):

  def __init__(self, pin=None, pull_up=False, active_state=None, bounce_time=None, pin_factory=None):
    DigitalInputDevice.__init__(self, pin, pull_up, active_state, bounce_time, pin_factory)

    self.last_activated = False
    self.pulse_width = False

    # Asignar funciones de GPIO.DigitalInputDevice
    self.when_activated = self.__when_activated
    self.when_deactivated = self.__when_deactivated

  def __when_activated(self):
    self.last_activated = time.time()

  def __when_deactivated(self):
    self.pulse_width = time.time() - self.last_activated
