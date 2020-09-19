from PWMChannel import PWMInputDevice
import pigpio

pi = pigpio.pi()

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
output_pin = 23

percentage = PWM_FREQ * PWM_MIN_PERIOD
duty_cycle = 255 * percentage

pi.set_PWM_frequency(output_pin, PWM_FREQ)
pi.set_PWM_dutycycle(output_pin, round(duty_cycle))

while True:
  print(input_channel.pulse_width)