---
title: "Edge AI: artificial intelligence on embedded devices"
collection: teaching
order: 6
type: "Graduate course"
permalink: /teaching/2026-fall-edge-ai
venue: "Ensias, Mohammed V University"
date: 2026-11-01
location: "Rabat, Morocco"
---

This project-based course teaches how to run artificial intelligence directly on microcontrollers and embedded boards, close to the sensors, instead of in the cloud. Over the semester, each team builds one complete system: **EcoTri 4.0**, a smart waste-sorting station that recognises materials, monitors its conveyor motor and alerts the operator, without a permanent cloud connection.

## Description

The course follows a project-based learning approach. Teams of 3 or 4 students build a single system throughout the semester. Each session is a **sub-project** that ends with a **milestone** the team demonstrates. The theory follows the needs of the project: Edge computing → TinyML → optimisation → deployment → industrialisation. All course material is in French.

**Format:** 7 sessions of 4 hours (2 h lecture + 2 h lab). A typical session:

* 15 min: a trigger problem ("the station must do X, how?")
* 1 h 45: lecture, with theory focused on the problem
* 1 h 45: lab, building the sub-project
* 15 min: milestone review and self-assessment with a rubric

### The EcoTri 4.0 station

A sorting centre receives waste on a conveyor belt. The station must recognise the material (plastic, glass, cardboard, metal), check the state of the belt and motor, count and trace the flows, and alert the operator and produce statistics, all without a permanent cloud connection.

| Node | Board | Role in the station |
|:-----|:------|:--------------------|
| Belt eye | XIAO ESP32-S3 Sense | Detects arriving items, captures images, sends them over BLE |
| Supervision camera | ESP32-CAM AI-Thinker | Wi-Fi overview, counting, batch QR codes |
| Decision unit | Portenta H7 + Vision Shield (OpenMV) | Material classification, motor audio, decision fusion, gateway |
| Operator | Smartphone (nRF Connect / Flutter) | Alerts and statistics |

### Prerequisites

* The [Machine learning](/teaching/2014-spring-teaching-1) and [Deep learning](/teaching/2026-fall-deep-learning) courses (CNNs, training, transfer learning)
* Programming in C/C++ (Arduino) and Python
* Basics of embedded systems (see the [AVR microcontrollers](/teaching/2026-fall-embedded-systems-avr) course)

### Tools

* [OpenMV IDE](https://openmv.io/pages/download) (MicroPython on the Portenta H7)
* [Arduino IDE](https://www.arduino.cc/en/software) (XIAO ESP32-S3 and ESP32-CAM)
* [Edge Impulse](https://edgeimpulse.com/) (data collection, training, optimisation and deployment)
* [nRF Connect](https://www.nordicsemi.com/Products/Development-tools/nRF-Connect-for-mobile) on a smartphone

## Objectives

By the end of the course, students will be able to:

1. Explain the Cloud / Fog / Edge / TinyML continuum and justify where computation should run (latency, bandwidth, energy, privacy).
2. Identify the resources of a microcontroller (Flash, SRAM, PSRAM, FPU, DSP) and compare embedded boards.
3. Apply embedded image processing (thresholding, blobs, contours, QR codes) and recognise its limits.
4. Design a BLE communication protocol (GATT service, fragmentation) and compare IoT protocols.
5. Build a quality dataset and an audio TinyML model (FFT, MFE, MFCC, anomaly detection).
6. Train an embedded CNN and optimise it (INT8 quantisation, pruning, distillation, transfer learning) to fit the memory of a microcontroller.
7. Deploy models on several targets, measure end-to-end performance and fuse vision and audio decisions.
8. Assess an Edge AI architecture and propose a path to production (embedded MLOps, security, Industry 4.0).

## Course

Each session combines a lecture and a lab around one sub-project (SP) of the EcoTri 4.0 station. Slides (in French) will be available in a read-only online viewer.

|    | Session | Main theory | Milestone | Slides |
|:---|:--------|:------------|:----------|:-------|
| 1  | SP1 "Understanding the station": scoping and getting started | Edge computing | Team specifications | *coming soon* |
| 2  | SP2 "Seeing without learning": rule-based vision | Embedded vision | Rule-based baseline | *coming soon* |
| 3  | SP3 "Making the station talk": communication | IoT / BLE | Protocol | *coming soon* |
| 4  | SP4 "Listening to the machine": TinyML and data | TinyML, DSP, data | Dataset + audio model | *coming soon* |
| 5  | SP5 "Recognising the material": learning and optimisation | Embedded DL, optimisation | Optimisation report | *coming soon* |
| 6  | SP6 "Assembling the station": deployment and integration | Deployment, energy, fusion | Demonstrator | *coming soon* |
| 7  | SP7 "Industrialise and defend": synthesis and assessment | MLOps, security, Industry 4.0 | Defence + exam | *coming soon* |

### Session contents

1. **Understanding the station** — *Why not send every image to the cloud?* The Cloud / Fog / Edge / TinyML continuum; computing a budget (latency, bandwidth = images/s × size, energy, privacy); anatomy of a microcontroller (Flash, SRAM, PSRAM, FPU, DSP) and comparison of the three boards; project methodology (requirements, architecture, milestones).
2. **Seeing without learning** — *Can simple thresholds tell a can from a cardboard box?* Image formats and memory cost; LAB thresholding, blobs, contours, Hough transform, QR codes; influence of lighting and calibration; why learning becomes necessary when real objects vary.
3. **Making the station talk** — *How does the XIAO send an image to the Portenta over a 20-byte link?* BLE (GAP, GATT, notify, MTU); BLE, Wi-Fi, MQTT and OPC-UA compared; energy cost of communication versus computation: "send the decision, not the image".
4. **Listening to the machine** — *Is the belt motor about to fail?* TinyML and its ecosystem (TFLite Micro, CMSIS-NN, Edge Impulse); signal processing (FFT, spectrogram, MFE, MFCC); supervised classification versus anomaly detection; data quality (class balance, bias, data leakage, train/test split).
5. **Recognising the material** — *The model is 3 MB and the Portenta has only 1 MB of RAM. What now?* Lightweight CNNs (separable convolutions, MobileNet, FOMO); cost metrics (parameters, MACs, peak RAM, Flash); optimisation: post-training INT8 quantisation and QAT, pruning, distillation, transfer learning and width α, NAS (MCUNet), EON Compiler and CMSIS-NN; reading a Pareto front (accuracy versus latency).
6. **Assembling the station** — *From a model in the browser to real-time sorting on the belt.* Inference engines and on-device preprocessing; profiling (latency, memory, energy), low power, model cascades; decision fusion (vision and audio), confidence thresholds, handling uncertainty.
7. **Industrialise and defend** — Embedded MLOps (OTA updates, versioning, data drift); security (encrypted BLE, secure boot, adversarial attacks); MES integration and indicators (KPI, OEE); outlook (NPUs, on-device learning, federated learning). Team defence and individual practical exam.

## Labs

|    | Lab | Link |
|:---|:----|:-----|
| 1  | Bringing up the Portenta H7 with OpenMV, then capture on the XIAO and the ESP32-CAM; FPS and memory versus resolution | *coming soon* |
| 2  | Portenta: detecting and tracking items on the belt by colour and shape. ESP32-CAM: reading the batch QR code and Wi-Fi stream | *coming soon* |
| 3  | BLE service on the Portenta with commands and LEDs; sending a fragmented, indexed image from the XIAO and rebuilding it; throughput measurement | *coming soon* |
| 4  | Audio recording on microSD; collecting normal / abnormal / stopped motor classes; Edge Impulse model with an anomaly-detection block | *coming soon* |
| 5  | TrashNet and images collected on the station; comparing three models (simple CNN, MobileNetV2 α = 0.35, the same model in INT8); confusion matrix; comparison with the rule-based baseline | *coming soon* |
| 6  | OpenMV deployment on the Portenta; XIAO capture → BLE → inference; JSON alert to the smartphone; comparison with an Arduino deployment on the XIAO | *coming soon* |

## Assessment

* Milestones J1 to J6 (formative and graded): 35%
* Team defence with a live demonstration: 25%
* Individual practical exam on a variant of the project: 40%

A rubric comes with each milestone: the system works, measurements, justification of choices, code quality.

## References

### Books

1. P. Warden, D. Situnayake, *TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontrollers*, O'Reilly, 2019
2. D. Situnayake, J. Plunkett, *AI at the Edge: Solving Real-World Problems with Embedded Machine Learning*, O'Reilly, 2023
3. G. M. Iodice, *TinyML Cookbook*, 2nd ed., Packt, 2023

### Online resources

1. [Edge Impulse documentation](https://docs.edgeimpulse.com/)
2. [OpenMV documentation](https://docs.openmv.io/)
3. [TensorFlow Lite for Microcontrollers](https://www.tensorflow.org/lite/microcontrollers)
4. [Harvard CS249r: Machine Learning Systems (free online book)](https://mlsysbook.ai/)
5. [MIT 6.5940: TinyML and Efficient Deep Learning Computing](https://efficientml.ai/)
6. [Arduino Portenta H7 documentation](https://docs.arduino.cc/hardware/portenta-h7/)
