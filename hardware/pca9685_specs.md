# PCA9685 16-Channel PWM/Servo Driver — Specifications

## Overview
- I²C-based 16-channel, 12-bit PWM controller that allows independent control of up to 16 servos or LEDs using only two microcontroller pins.
- Supports chaining up to 62 driver boards for a maximum of 992 channels.
- Ideal for robotics, lighting control, and multi-servo applications.

## Electrical Specifications
| Parameter             | Value                        |
|-----------------------|------------------------------|
| Logic Supply Voltage (VCC) | 3 – 5 V                  |
| Servo Supply Voltage (V+)  | 5 – 6 V (up to 12 V max\*) |
| Max Output Current         | ~25 mA per channel       |
| PWM Resolution             | 12-bit (4096 steps)      |
| PWM Frequency Range        | 40 Hz – 1600 Hz (shared across channels) |

> \* Use caution above 6 V — suitable for LEDs or special motor drivers only, not standard hobby servos.

## Connectivity & Ports
- **I²C Control Pins:** SDA, SCL (with onboard pull-ups to VCC), OE (active-low output enable).
- **Output Ports:** 16 outputs, each with V+, GND, and PWM signal.
- **Power Inputs:** Separate pins for VCC (logic) and V+ (servo/LED power).

## Addressing & Chaining
- Factory default I²C address: `0x40`.
- Address configurable via A0–A5 jumpers.
- Up to 62 boards can be chained on the same I²C bus.

## PWM Frequency & Control
- Adjustable PWM frequency: 40 Hz to 1600 Hz.
- Typical servo control frequency: ~60 Hz.
- Duty cycle control via:
  - `setPWM(channel, on, off)` — sets exact on/off tick positions (0–4095).
  - Fully ON: `setPWM(pin, 4096, 0)`.
  - Fully OFF: `setPWM(pin, 0, 4096)`.

## Power Recommendations
- Use an external regulated power supply for servos to prevent microcontroller resets or noise.
- Recommended decoupling capacitor: ~100 µF per active servo to stabilize voltage under load.
- Do not power high-current servos directly from the logic supply.

## Supported Libraries
- **Arduino:** `Adafruit_PWMServoDriver` (simplifies setup and control).
- **Python / CircuitPython:** `adafruit_pca9685`, `adafruit_servokit`.

## References
- [Adafruit PCA9685 16-Channel PWM/Servo Driver Guide (PDF)](https://cdn-learn.adafruit.com/downloads/pdf/16-channel-pwm-servo-driver.pdf)
- NXP PCA9685 Datasheet
