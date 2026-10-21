---
title: "Embedded systems: AVR microcontrollers"
collection: teaching
type: "Undergraduate course"
permalink: /teaching/2026-fall-embedded-systems-avr
venue: "Ensias, Mohammed V University"
date: 2026-09-10
location: "Rabat, Morocco"
---
This course introduces embedded systems through the programming of 8-bit AVR microcontrollers (ATmega328P, the chip on the Arduino Uno). Students write bare-metal C, working directly with registers, to control peripherals, handle interrupts and build a complete embedded application.

## Prerequisites
- C programming
- Digital electronics basics (logic, binary/hexadecimal, simple circuits)

## Tools
- [Microchip Studio](https://www.microchip.com/en-us/tools-resources/develop/microchip-studio) or avr-gcc with a text editor
- An Arduino Uno board (or a simulator), breadboard and basic components

## Lectures

|    | Course                                           | Slides | Video     |
|:---|:-------------------------------------------------|--------|-----------|
| 1  | Introduction to embedded systems and microcontrollers | [PDF] | [Youtube] |
| 2  | AVR architecture: CPU, memory, registers, clock  | [PDF]  | [Youtube] |
| 3  | Bare-metal C for AVR and the build toolchain     | [PDF]  | [Youtube] |
| 4  | Digital I/O ports (DDRx, PORTx, PINx)            | [PDF]  | [Youtube] |
| 5  | Interrupts (external and pin change)             | [PDF]  | [Youtube] |
| 6  | Timers/counters and PWM                          | [PDF]  | [Youtube] |
| 7  | Analog-to-digital converter (ADC)                | [PDF]  | [Youtube] |
| 8  | Serial communication: UART, SPI, I2C             | [PDF]  | [Youtube] |
| 9  | Low power modes and watchdog                     | [PDF]  | [Youtube] |
| 10 | Designing an embedded application                | [PDF]  | [Youtube] |

## Labs

|    | Lab                                         | Labs  | Solutions |
|:---|:--------------------------------------------|-------|-----------|
| 1  | Toolchain setup, blinking LED with registers | [Lab] | [Sol] |
| 2  | Push buttons, debouncing and 7-segment display | [Lab] | [Sol] |
| 3  | External interrupts                         | [Lab] | [Sol] |
| 4  | Timers: precise delays and PWM motor/LED control | [Lab] | [Sol] |
| 5  | Reading sensors with the ADC                | [Lab] | [Sol] |
| 6  | UART communication with a PC                | [Lab] | [Sol] |
| 7  | I2C sensor and LCD display                  | [Lab] | [Sol] |

## Project
In pairs, students design and build a small embedded system (e.g. a temperature monitor, a smart parking counter or a line-following robot), from specification to a working prototype.

## Background materials
1. [AVR Libc user manual](https://www.nongnu.org/avr-libc/user-manual/)
2. ATmega328P datasheet (Microchip): the reference for every register used in the course
3. [Arduino documentation](https://docs.arduino.cc/)
