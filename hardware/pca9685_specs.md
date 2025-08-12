# PCA9685 16-Channel PWM/Servo Driver — Quick Specs

## Overview
- ...

## Electrical Specifications
| Parameter      | Value        |
|----------------|--------------|
| Logic Supply (VCC) | 3–5 V   |
| Servo Supply (V+)  | 5–6 V (up to 12 V) |
| Max Output Current | ~25 mA/channel |
| PWM Resolution     | 12-bit (4096 steps) |
| PWM Frequency Range| 40–1600 Hz (shared across channels) |

## Connectivity & Ports
- I²C: SDA, SCL (with pull-ups), OE (active-low)
- 16 output ports (V+, GND, PWM)

## Addressing & Chaining
- Base I²C: 0x40
- Up to 62 boards via A0–A5 jumpers

## Power Recommendations
- External power supply required for servos
- Optional decoupling capacitor  

## Usage & Libraries
- **Arduino:** `Adafruit_PWMServoDriver`
- **Python/CircuitPython:** `adafruit_pca9685`, `adafruit_servokit`

## Advanced Control
- Set PWM frequency: `setPWMFreq(freq)`
- Control pulses: `setPWM(channel, on, off)`
- Fully ON/OFF: `setPWM(pin, 4096, 0)` / `setPWM(pin, 0, 4096)`
