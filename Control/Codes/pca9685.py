import time
import sys

if sys.platform.startswith("linux"):
    import smbus
else:
    class _FakeSMBus:
        def __init__(self, bus=1): pass
        def write_byte_data(self, addr, reg, val): pass
        def write_i2c_block_data(self, addr, reg, data):
            print(f"[fake i2c] addr={hex(addr)} reg={hex(reg)} data={data}")
        def close(self): pass

    class smbus:
        SMBus = _FakeSMBus
# PCA9685 register addresses
MODE1 = 0x00
MODE2 = 0x01
PRESCALE = 0xFE
LED0_ON_L = 0x06 # channel n starts at 0x06 + 4*n (ON_L, ON_H, OFF_L, OFF_H)
ALL_LED_OFF_H = 0xFD # writing bit 4 here switches every channel full-off
class PCA9685:
# osc_hz = REAL oscillator speed of THIS chip (nominal 25 MHz, measured ~30.4 MHz on ours)
    def __init__(self, bus=1, address=0x40, freq_hz=50, osc_hz=30_400_000):
        self.bus = smbus.SMBus(bus) # bus 1 = header pins 3 (SDA) / 5 (SCL)
# Jetson Nano B01 + PCA9685 + U2 Mini thruster: team guide Page 4
        self.addr = address
        self.osc_hz = osc_hz
        self.prescale = int(round(osc_hz / (4096 * freq_hz))) - 1 # osc / (4096 ticks * freq) - 1
        self.tick_us = (self.prescale + 1) / osc_hz * 1e6 # tick length = (prescale+1) / osc
        self._w(MODE2, 0x04) # totem-pole (push-pull) outputs
        self._w(MODE1, 0x30) # sleep (0x10) + auto-increment (0x20)
        self._w(PRESCALE, self.prescale) # PRESCALE can only be written while asleep
        self._w(MODE1, 0x20) # wake up, keep auto-increment on (block writes)
        time.sleep(0.005) # oscillator needs ~500 us to settle
        self._w(MODE1, 0xA0) # restart (0x80) + auto-increment
    def _w(self, reg, val):
        self.bus.write_byte_data(self.addr, reg, val)
    def _set_ticks(self, ch, ticks):
        ticks = max(0, min(4096, ticks)) # 12-bit counter, 4096 means "always on"
        base = LED0_ON_L + 4 * ch
        if ticks >= 4096: # 100 %: "full on" flag (bit 4 of ON_H)
            data = [0, 0x10, 0, 0]
        elif ticks <= 0: # 0 %: "full off" flag, pin held low, no pulses
            data = [0, 0, 0, 0x10]
        else: # normal: on at tick 0, off at tick `ticks`
            data = [0, 0, ticks & 0xFF, ticks >> 8] # split 12-bit value into low/high byte
        self.bus.write_i2c_block_data(self.addr, base, data) # one transaction, 4 bytes together
    def set_duty(self, ch, fraction): # for LEDs, fraction 0.0 to 1.0
        self._set_ticks(ch, int(round(fraction * 4096))) # fraction of the period, in ticks
    def set_pulse_us(self, ch, us): # for ESCs, pulse width in microseconds
        if us <= 0:
            self._set_ticks(ch, 0) # 0 = no pulses at all
        else:
            self._set_ticks(ch, int(round(us / self.tick_us))) # ticks = pulse / tick length
    def all_off(self): # emergency stop: every channel held low
        self._w(ALL_LED_OFF_H, 0x10)
    def close(self):
        self.bus.close()