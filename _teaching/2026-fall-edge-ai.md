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

The course follows a project-based learning approach. Teams of 3 or 4 students build a single system throughout the semester. Each session is a **sub-project** that ends with a **milestone** the team demonstrates. The theory follows the needs of the project: Edge computing → TinyML → optimisation → deployment → industrialisation. All course material is in French. Labs and tutorials are co-authored with Pr. Hassan Berbia.

**Format:** 8 sessions of 4 hours (2 h lecture + 2 h lab), each with a lecture, a step-by-step tutorial on the Portenta H7 with OpenMV, and a lab. A typical session:

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
9. Use Edge Impulse as an MLOps platform to rebuild, optimise and redeploy a model on several boards.

## Course

Each session combines a lecture, a tutorial and a lab around one sub-project (SP) of the EcoTri 4.0 station. Slides and tutorials (in French) are displayed in a read-only online viewer. The tutorials guide you step by step on the Portenta H7 with OpenMV and prepare the lab.

|    | Session | Main theory | Milestone | Slides | Tutorial |
|:---|:--------|:------------|:----------|:-------|:---------|
| 1  | SP1 "Understanding the station": Edge computing and TinyML | Edge computing | Team specifications | [PDF](/viewer/?d=ZWRnZS1jb3Vyc2V8TGVjdHVyZTFfSW50cm9fRWRnZUFJfHBkZnxMZWN0dXJlIDEg4oCUIFVuZGVyc3RhbmRpbmcgdGhlIHN0YXRpb24) | [Tutorial 1](/viewer/?d=ZWRnZS10dXRvcmlhbHxUdXRvcmlhbDFfTGVjdHVyZTFfUHJpc2VFbk1haW5fUG9ydGVudGFfT3Blbk1WfHBkZnxUdXRvcmlhbCAxIOKAlCBVbmRlcnN0YW5kaW5nIHRoZSBzdGF0aW9u) |
| 2  | SP2 "Seeing without learning": rule-based vision | Embedded vision | Rule-based baseline | [PDF](/viewer/?d=ZWRnZS1jb3Vyc2V8TGVjdHVyZTJfU2xpZGVzX1Zpc2lvblJlZ2xlc3xwZGZ8TGVjdHVyZSAyIOKAlCBTZWVpbmcgd2l0aG91dCBsZWFybmluZw) | [Tutorial 2](/viewer/?d=ZWRnZS10dXRvcmlhbHxUdXRvcmlhbDJfTGVjdHVyZTJfVmlzaW9uUmVnbGVzX09wZW5NVnxwZGZ8VHV0b3JpYWwgMiDigJQgU2VlaW5nIHdpdGhvdXQgbGVhcm5pbmc) |
| 3  | SP3 "Making the station talk": BLE and IoT protocols | IoT / BLE | Protocol | [PDF](/viewer/?d=ZWRnZS1jb3Vyc2V8TGVjdHVyZTNfU2xpZGVzX0NvbW11bmljYXRpb25fQkxFfHBkZnxMZWN0dXJlIDMg4oCUIE1ha2luZyB0aGUgc3RhdGlvbiB0YWxr) | [Tutorial 3](/viewer/?d=ZWRnZS10dXRvcmlhbHxUdXRvcmlhbDNfTGVjdHVyZTNfQkxFX1BvcnRlbnRhX09wZW5NVnxwZGZ8VHV0b3JpYWwgMyDigJQgTWFraW5nIHRoZSBzdGF0aW9uIHRhbGs) |
| 4  | SP4 "Listening to the machine": TinyML and audio | TinyML, DSP, data | Dataset + audio model | [PDF](/viewer/?d=ZWRnZS1jb3Vyc2V8TGVjdHVyZTRfU2xpZGVzX1RpbnlNTF9BdWRpb3xwZGZ8TGVjdHVyZSA0IOKAlCBMaXN0ZW5pbmcgdG8gdGhlIG1hY2hpbmU) | [Tutorial 4](/viewer/?d=ZWRnZS10dXRvcmlhbHxUdXRvcmlhbDRfTGVjdHVyZTRfQXVkaW9fUG9ydGVudGFfT3Blbk1WfHBkZnxUdXRvcmlhbCA0IOKAlCBMaXN0ZW5pbmcgdG8gdGhlIG1hY2hpbmU) |
| 5  | SP5 "Recognising the material": embedded CNNs and optimisation | Embedded DL, optimisation | Optimisation report | [PDF](/viewer/?d=ZWRnZS1jb3Vyc2V8TGVjdHVyZTVfU2xpZGVzX09wdGltaXNhdGlvbl9UaW55TUx8cGRmfExlY3R1cmUgNSDigJQgUmVjb2duaXNpbmcgdGhlIG1hdGVyaWFs) | [Tutorial 5](/viewer/?d=ZWRnZS10dXRvcmlhbHxUdXRvcmlhbDVfTGVjdHVyZTVfVEZMaXRlX0lOVDhfUG9ydGVudGFfT3Blbk1WfHBkZnxUdXRvcmlhbCA1IOKAlCBSZWNvZ25pc2luZyB0aGUgbWF0ZXJpYWw) |
| 6  | SP6 "Assembling the station": deployment and integration | Deployment, energy, fusion | Demonstrator | [PDF](/viewer/?d=ZWRnZS1jb3Vyc2V8TGVjdHVyZTZfU2xpZGVzX0RlcGxvaWVtZW50X0ludGVncmF0aW9ufHBkZnxMZWN0dXJlIDYg4oCUIEFzc2VtYmxpbmcgdGhlIHN0YXRpb24) | [Tutorial 6](/viewer/?d=ZWRnZS10dXRvcmlhbHxUdXRvcmlhbDZfTGVjdHVyZTZfUGlwZWxpbmVfUG9ydGVudGFfT3Blbk1WfHBkZnxUdXRvcmlhbCA2IOKAlCBBc3NlbWJsaW5nIHRoZSBzdGF0aW9u) |
| 7  | SP7 "Industrialise and defend": MLOps, security, Industry 4.0 | MLOps, security, Industry 4.0 | Defence + exam | [PDF](/viewer/?d=ZWRnZS1jb3Vyc2V8TGVjdHVyZTdfU2xpZGVzX0luZHVzdHJpYWxpc2VyfHBkZnxMZWN0dXJlIDcg4oCUIEluZHVzdHJpYWxpc2UgYW5kIGRlZmVuZA) | [Tutorial 7](/viewer/?d=ZWRnZS10dXRvcmlhbHxUdXRvcmlhbDdfTGVjdHVyZTdfRXhwbG9pdGF0aW9uX1BvcnRlbnRhX09wZW5NVnxwZGZ8VHV0b3JpYWwgNyDigJQgSW5kdXN0cmlhbGlzZSBhbmQgZGVmZW5k) |
| 8  | Edge Impulse, an MLOps platform for TinyML | Edge Impulse, FOMO, EON | Multi-board deployment | [PDF](/viewer/?d=ZWRnZS1jb3Vyc2V8TGVjdHVyZThfU2xpZGVzX0VkZ2VJbXB1bHNlfHBkZnxMZWN0dXJlIDgg4oCUIEVkZ2UgSW1wdWxzZSwgYW4gTUxPcHMgcGxhdGZvcm0gZm9yIFRpbnlNTA) | [Tutorial 8](/viewer/?d=ZWRnZS10dXRvcmlhbHxUdXRvcmlhbDhfTGVjdHVyZThfRWRnZUltcHVsc2VfUG9ydGVudGFfT3Blbk1WfHBkZnxUdXRvcmlhbCA4IOKAlCBFZGdlIEltcHVsc2UsIGFuIE1MT3BzIHBsYXRmb3JtIGZvciBUaW55TUw) |

### Session contents

1. **Understanding the station** — *Why not send every image to the cloud?* The Cloud / Fog / Edge / TinyML continuum; computing a budget (latency, bandwidth = images/s × size, energy, privacy); anatomy of a microcontroller (Flash, SRAM, PSRAM, FPU, DSP) and comparison of the three boards; project methodology (requirements, architecture, milestones).
2. **Seeing without learning** — *Can simple thresholds tell a can from a cardboard box?* Image formats and memory cost; LAB thresholding, blobs, contours, Hough transform, QR codes; influence of lighting and calibration; why learning becomes necessary when real objects vary.
3. **Making the station talk** — *How does the XIAO send an image to the Portenta over a 20-byte link?* BLE (GAP, GATT, notify, MTU); BLE, Wi-Fi, MQTT and OPC-UA compared; energy cost of communication versus computation: "send the decision, not the image".
4. **Listening to the machine** — *Is the belt motor about to fail?* TinyML and its ecosystem (TFLite Micro, CMSIS-NN, Edge Impulse); signal processing (FFT, spectrogram, MFE, MFCC); supervised classification versus anomaly detection; data quality (class balance, bias, data leakage, train/test split).
5. **Recognising the material** — *The model is 3 MB and the Portenta has only 1 MB of RAM. What now?* Lightweight CNNs (separable convolutions, MobileNet, FOMO); cost metrics (parameters, MACs, peak RAM, Flash); optimisation: post-training INT8 quantisation and QAT, pruning, distillation, transfer learning and width α, NAS (MCUNet), EON Compiler and CMSIS-NN; reading a Pareto front (accuracy versus latency).
6. **Assembling the station** — *From a model in the browser to real-time sorting on the belt.* Inference engines and on-device preprocessing; profiling (latency, memory, energy), low power, model cascades; decision fusion (vision and audio), confidence thresholds, handling uncertainty.
7. **Industrialise and defend** — Embedded MLOps (OTA updates, versioning, data drift); security (encrypted BLE, secure boot, adversarial attacks); MES integration and indicators (KPI, OEE); outlook (NPUs, on-device learning, federated learning). Team defence and individual practical exam.
8. **Edge Impulse, an MLOps platform for TinyML** — *A new customer, new waste: can we rebuild and redeploy the model in one day?* What costs the most in a TinyML project beyond the model; ingesting and labelling data, a reproducible impulse; transfer learning, FOMO object detection and anomaly detection; EON Tuner and EON Compiler under a RAM / Flash / latency budget; one impulse, several targets, versions and an API.

## Labs

Lab handouts (in French) are displayed in a read-only online viewer. Each lab ends with the team's milestone (J1 to J6).

|    | Lab | Handout |
|:---|:----|:--------|
| 1  | Understanding the station: bringing up and characterising the three nodes of EcoTri 4.0 (J1) | [Lab 1](/viewer/?d=ZWRnZS10cHxUUDFfU2VhbmNlMV9DYXJhY3RlcmlzYXRpb25fTm9ldWRzfHBkZnxMYWIgMSDigJQgRWNvVHJpIDQuMA) |
| 2  | Detecting, tracking and rule-based classification on the station's belt (J2) | [Lab 2](/viewer/?d=ZWRnZS10cHxUUDJfTGVjdHVyZTJfQ2xhc3NpZmlldXJfUmVnbGVzfHBkZnxMYWIgMiDigJQgRWNvVHJpIDQuMA) |
| 3  | A BLE protocol to transfer an image from the XIAO to the Portenta (J3) | [Lab 3](/viewer/?d=ZWRnZS10cHxUUDNfTGVjdHVyZTNfUHJvdG9jb2xlX0ltYWdlX0JMRXxwZGZ8TGFiIDMg4oCUIEVjb1RyaSA0LjA) |
| 4  | A dataset and a first audio model to monitor the belt motor (J4) | [Lab 4](/viewer/?d=ZWRnZS10cHxUUDRfTGVjdHVyZTRfRGF0YXNldF9BdWRpb19FZGdlSW1wdWxzZXxwZGZ8TGFiIDQg4oCUIEVjb1RyaSA0LjA) |
| 5  | Recognising the material: training, optimising and trading off three models for the Portenta H7 (J5) | [Lab 5](/viewer/?d=ZWRnZS10cHxUUDVfTGVjdHVyZTVfT3B0aW1pc2F0aW9uX1BhcmV0b3xwZGZ8TGFiIDUg4oCUIEVjb1RyaSA0LjA) |
| 6  | Assembling EcoTri 4.0: multi-target deployment and end-to-end demonstrator (J6) | [Lab 6](/viewer/?d=ZWRnZS10cHxUUDZfTGVjdHVyZTZfU3RhdGlvbl9JbnRlZ3JhdGlvbl9KNnxwZGZ8TGFiIDYg4oCUIEVjb1RyaSA0LjA) |
| 7  | Industrialising and defending the station: defence, individual practical exam and written reflection | [Lab 7](/viewer/?d=ZWRnZS10cHxUUDdfTGVjdHVyZTdfRXZhbHVhdGlvbl9Tb3V0ZW5hbmNlfHBkZnxMYWIgNyDigJQgRWNvVHJpIDQuMA) |
| 8  | Detecting, counting and deploying on two boards with Edge Impulse (FOMO, EON Tuner, EON Compiler) | [Lab 8](/viewer/?d=ZWRnZS10cHxUUDhfTGVjdHVyZThfRk9NT19NdWx0aUNpYmxlc19FZGdlSW1wdWxzZXxwZGZ8TGFiIDgg4oCUIEVjb1RyaSA0LjA) |

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
