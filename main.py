from PWMChannel import PWMInputDevice
from gpiozero import PWMOutputDevice

PWM_FREQ = 500
PWM_MIN_PERIOD = 0.001  # 1ms
PWM_MAX_PERIOD = 0.002  # 1ms

##########
# Inputs #
##########

input_channel = PWMInputDevice(24)

###########
# Outputs #
###########

emulated_pwm = PWMOutputDevice(23, frequency=PWM_FREQ)
emulated_pwm.blink(on_time=PWM_MIN_PERIOD, off_time=(1 / PWM_FREQ - PWM_MIN_PERIOD))

while True:
  print(input_channel.pulse_width)
