# Robotic Arm — Build Guide

This document provides step-by-step instructions for assembling, wiring, and calibrating the 6 DOF robotic arm using the PCA9685 servo driver.

---

## 1. Required Components

### Electronics
- 1 × PCA9685 16-Channel PWM Servo Driver
- 1 × Microcontroller (Arduino, ESP8266, or compatible)
- 6 × Servo motors (compatible with arm design)
- Power supply for servos (5–6 V regulated, sufficient current capacity)
- External power supply for logic (if required)
- Jumper wires (male-to-male, male-to-female)
- Optional: 100 µF capacitors (per active servo for stability)

### Mechanical
- 6 DOF robotic arm frame kit
- Screws, nuts, and bolts (as per kit)
- Servo mounting brackets
- Base plate for stability

### Tools
- Screwdriver set
- Allen key set (if required by kit)
- Soldering iron (optional, for permanent wiring)
- Wire cutter/stripper

---

## 2. Assembly Order

1. **Base Assembly**  
   - Secure the base plate.
   - Mount the first servo (base rotation) to the base.

2. **Lower Arm**  
   - Attach the lower arm frame to the base servo horn.
   - Secure with screws and check smooth rotation.

3. **Upper Arm**  
   - Mount the upper arm servo to the lower arm bracket.
   - Attach the upper arm segment.

4. **Forearm & Wrist**  
   - Install the forearm servos (lower and upper) sequentially.
   - Mount the wrist servo.

5. **Claw/Gripper**  
   - Attach the claw servo.
   - Install the gripper mechanism and check for free movement.

---

## 3. Wiring

Refer to the wiring diagram:  
[**6 DOF Robotic Arm — Breadboard View**](../hardware/wiring/6%20DOF%20Robotic%20Arm_bb.png)  
Fritzing source file: [`6 DOF Robotic Arm.fzz`](../hardware/wiring/6%20DOF%20Robotic%20Arm.fzz)

**Wiring Steps:**
1. Connect PCA9685 `VCC` to microcontroller 3.3 V or 5 V (logic level).  
2. Connect `GND` between PCA9685, microcontroller, and servo power supply.  
3. Connect `SDA` and `SCL` from PCA9685 to microcontroller I²C pins.  
4. Connect servo power (`V+`) to external power supply (5–6 V).  
5. Connect each servo signal wire to PCA9685 channel outputs (CH0–CH5).  

---

## 4. Calibration

Run each calibration script before operating the arm fully:  

| Servo Position | Script |
|----------------|--------|
| Claw           | [`claw_servo_max_angle.py`](../firmware/calibration/claw_servo_max_angle.py) |
| Elbow          | [`elbow_servo_setup.py`](../firmware/calibration/elbow_servo_setup.py) |
| Lower Forearm  | [`lower_forearm_servo_setup.py`](../firmware/calibration/lower_forearm_servo_setup.py) |
| Shoulder       | [`shoulder_servo_setup.py`](../firmware/calibration/shoulder_servo_setup.py) |
| Upper Forearm  | [`upper_forearm_servo_setup.py`](../firmware/calibration/upper_forearm_servo_setup.py) |
| Wrist          | [`wrist_servo_setup.py`](../firmware/calibration/wrist_servo_setup.py) |

**Calibration Tips:**
- Ensure servos start at their neutral (90°) position before attaching arms.
- Adjust horn alignment carefully to avoid mechanical strain.
- Test movement slowly to prevent over-rotation.

---

## 5. Troubleshooting

| Issue | Possible Cause | Solution |
|-------|----------------|----------|
| Servo not moving | Incorrect wiring, insufficient power | Check connections, ensure proper voltage/current |
| Arm jittering | Electrical noise from servos | Add decoupling capacitors, use a stable power supply |
| PCA9685 not detected | Wrong I²C address or wiring | Check address jumpers, verify SDA/SCL wiring |
| Limited movement | Mechanical blockage | Check servo horn alignment and screw tension |

---

## 6. References
- [Servo Specifications](../hardware/specs/servo_specs.md)
- [PCA9685 Specifications](../hardware/specs/pca9685_specs.md)
- [PCA9685 Datasheet (PDF)](../hardware/datasheets/PCA9685_Datasheet.pdf)

---
