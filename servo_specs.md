# MG996R High-Torque Servo Specifications

## Overview
The **MG996R** is a high-torque, metal-geared digital servo motor widely used in robotics, RC vehicles, and automation projects.  
In this project, it is used for precise joint actuation in the 6DOF robotic arm, controlled via the **PCA9685 16-Channel PWM driver**.

---

## Technical Specifications

| Parameter           | Value                                  |
|---------------------|----------------------------------------|
| **Type**            | Digital, high-torque                   |
| **Weight**          | ~55 g                                  |
| **Dimensions**      | 40.7 × 19.7 × 42.9 mm                   |
| **Operating Voltage**| 4.8 V – 7.2 V                          |
| **Stall Torque**    | 9.4 kg·cm @ 4.8 V<br>11 kg·cm @ 6.0 V   |
| **Operating Speed** | 0.19 s/60° @ 4.8 V<br>0.14 s/60° @ 6.0 V|
| **Rotation Range**  | ~120° effective (mechanical ~180°)      |
| **Gear Material**   | Metal                                  |
| **Dead Band Width** | 5 μs                                   |
| **Signal Type**     | PWM (50 Hz)                            |
| **Connector**       | 3-pin (Brown = GND, Red = V+, Orange = Signal) |

---

## PWM Control (PCA9685)

The MG996R operates at **50 Hz** PWM frequency.  
For the PCA9685 (12-bit resolution, 0–4095 steps), typical control values are:

| Angle | Pulse Width (ms) | PCA9685 Value |
|-------|------------------|---------------|
| 0°    | 1.0              | ~205          |
| 90°   | 1.5              | ~307          |
| 180°  | 2.0              | ~410          |

> ⚠️ These values are approximate. Each servo should be **calibrated** to prevent mechanical strain.

---

## Wiring Reference

PCA9685 Pin → Servo Wire
GND → Brown
V+ → Red
PWM Channel → Orange


- Power MG996R servos with a **dedicated 5V–6V supply**.  
- Each servo can draw up to **2.5 A at stall**.  
- Do **not** power servos directly from the Raspberry Pi’s 5V pin.

---

## Operational Notes

1. **Power Supply:** Use a regulated 5V–6V power source rated for total servo load.  
2. **Startup Behavior:** Servos may twitch on power-up before receiving a stable PWM signal.  
3. **Angle Limits:** Restrict travel in software to avoid forcing the mechanical stops.  
4. **Heat Management:** Avoid prolonged stall conditions to prevent overheating.

---

## Revision History
- **v1.0 (2025-08-09)** – Initial professional documentation.
