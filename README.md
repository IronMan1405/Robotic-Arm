# 6DOF Robotic Arm Project 🤖

A modular, Raspberry Pi-controlled 6DOF robotic arm designed for multi-modal control: web interface, voice commands, and computer vision.

---

## 🚧 Project Status

✅ Hardware assembled and control tests with PCA9685 + servos completed.  
✅ Version 1 (Web-controlled robotic arm using PCA9685 + Arduino/ESP8266) – Completed on [Date]  
🚧 Version 2 (Vision integration) – In Progress

---

## 📁 Directory Structure

- [`hardware/`](hardware/) – Circuit diagrams, wiring, and specifications  
  - [MG996R Servo Specifications](hardware/specs/servo_specs.md)  
  - [PCA9685 Servo Driver Specifications](hardware/specs/pca9685_specs.md)  
  - [PCA9685 Datasheet (PDF)](hardware/datasheets/PCA9685_Datasheet.pdf)  
  - [Wiring Diagram (PNG)](hardware/wiring/6%20DOF%20Robotic%20Arm_bb.png)  
  - [Wiring Diagram (Fritzing Source)](hardware/wiring/6%20DOF%20Robotic%20Arm.fzz)  
- [`firmware/`](firmware/) – Servo calibration and control scripts  
- [`software/`](software/) – Voice control, Flask dashboard, YOLOv5 object detection  
- [`tests/`](tests/) – Calibration, angle limits, smooth movement  
- [`docs/`](docs/) – Guides, pinouts, architecture diagrams  
  - [Build Guide](docs/BUILD.md)  
  - [Roadmap](docs/roadmap.md)  
- [`media/`](media/) – Photos, renders, demo videos  

---

## 🔧 Hardware

- Raspberry Pi 3 B+
- PCA9685 16-channel Servo Driver
- MG996R / SG90 servos
- 6DOF mechanical arm frame
- 5V 10A power supply
- Breadboard, jumper wires, etc.

---

## 🔌 Setup Instructions

For full assembly and wiring instructions, see the [**Build Guide**](docs/BUILD.md).  
For detailed assembly steps, refer to the [6DOF Arm Assembly Guide (PDF)](docs/references/6DOF_Arm_Assembly_Guide.pdf).
For servo and PCA9685 details, see the [**Specifications**](hardware/pca9685_specs.md) and [**Datasheet**](hardware/datasheets/PCA9685_Datasheet.pdf).

---

## 🗺️ Roadmap

- [x] **Version 1:** Web-based servo control (PCA9685 + Raspberry Pi)
- [ ] **Version 2:** Live camera feed integration
- [ ] **Version 3:** Voice commands (Google Assistant / Offline STT)
- [ ] **Version 4:** Computer vision with YOLOv5 / MobileNet SSD
- [ ] **Version 5:** Autonomous mode + JARVIS-style integration

---

## 🤝 Contributing

Pull requests are welcome! 
For major changes, please open an issue first to discuss what you’d like to change.
See [`CONTRIBUTING.md`](CONTRIBUTING.md) if available.

---

## 📬 Contact

Created by [Dakshesh Nankani](https://github.com/DaksheshNankani) – feel free to reach out!

---

## 📜 License

MIT License

