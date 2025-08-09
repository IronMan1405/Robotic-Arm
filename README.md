# 6DOF Robotic Arm Project 🤖

A modular, Raspberry Pi-controlled 6DOF robotic arm designed for multi-modal control: web interface, voice commands, and computer vision.

---

## 🚧 Project Status

✅ Hardware assembled and control tests with PCA9685 + servos completed.  
🔜 Moving on to **Version 1: Web Control** implementation.

---

## 📁 Directory Structure

- [`hardware/`](hardware/): Circuit diagrams, PCA9685 wiring, [MG996R servo specifications](hardware/servo_specs.md)
- [`firmware/`](firmware/): Servo control code (e.g., Python scripts using RPi + PCA9685)
- [`software/`](software/): Voice control, Flask dashboard, YOLOv5 object detection
- [`tests/`](tests/): Calibration, angle limits, smooth movement
- [`docs/`](docs/): Setup guides, pinouts, flowcharts, and architecture diagrams
- [`media/`](media/): Photos, renders, demo videos

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

_(Coming soon)_

---

## 🗺️ Roadmap

- [ ] **Version 1:** Web-based servo control (PCA9685 + Raspberry Pi)
- [ ] **Version 2:** Live camera feed integration
- [ ] **Version 3:** Voice commands (Google Assistant / Offline STT)
- [ ] **Version 4:** Computer vision with YOLOv5 / MobileNet SSD
- [ ] **Version 5:** Autonomous mode + JARVIS-style integration

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📬 Contact

Created by [Dakshesh Nankani](https://github.com/DaksheshNankani) – feel free to reach out!

---

## 📜 License

MIT License

