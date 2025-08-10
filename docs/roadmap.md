# 6DOF Robotic Arm — Project Roadmap

## 1. Phase 1 — Core Setup & Control
**Goal:** Get the robotic arm physically built and controlled via PCA9685 + Python.  
- ✅ Assemble 6DOF robotic arm hardware  
- ✅ Wire all servos to PCA9685 driver  
- ✅ Create servo calibration scripts for each joint (`firmware/Calibration/`)  
- ✅ Test basic movements with `servo_controller.py`  
- ⬜ Integrate web-based manual control UI (`app.py` + Flask)

---

## 2. Phase 2 — Enhanced Control & Automation
**Goal:** Add more flexible and precise control options.  
- ⬜ Create pre-defined movement sequences (pick/place, wave, rotate)  
- ⬜ Add position presets in UI  
- ⬜ Implement smooth motion control with acceleration profiles  
- ⬜ Save & load movement sequences from file

---

## 3. Phase 3 — Vision Integration
**Goal:** Enable camera-based object detection and positioning.  
- ⬜ Connect USB webcam or ESP32-CAM to PC  
- ⬜ Implement object tracking (MobileNet SSD / YOLO Tiny)  
- ⬜ Link detection output to arm movement commands  
- ⬜ Add mode toggle: **Manual / Vision-assisted**

---

## 4. Phase 4 — Voice & AI Control
**Goal:** Allow natural language commands.  
- ⬜ Integrate offline voice recognition (Vosk)  
- ⬜ Map voice commands to movement sequences  
- ⬜ Add voice status feedback (pyttsx3 / PicoTTS)  
- ⬜ Enable JARVIS-style conversational control

---

## 5. Phase 5 — Advanced Features & Final Build
**Goal:** Create a polished, fully autonomous robotic arm system.  
- ⬜ Build autonomous pick-and-place routine with object classification  
- ⬜ Optimize servo power usage  
- ⬜ Design custom PCB for servo control + power distribution (`hardware/electronics/`)  
- ⬜ 3D print custom end-effectors (claw, gripper, suction, etc.)  
- ⬜ Full integration into personal JARVIS assistant

---

## Timeline (Tentative)
| Phase   | Estimated Duration |
|---------|--------------------|
| Phase 1 | ✅ Completed |
| Phase 2 | 2–3 weeks |
| Phase 3 | 3–4 weeks |
| Phase 4 | 3 weeks |
| Phase 5 | Ongoing |

---

## Notes
- Testing scripts are in `tests/`  
- Hardware documentation in `hardware/`  
- PCB design files in `hardware/electronics/robotic_arm/`  
- Keep backup snapshots for all `.kicad_pcb` changes  
