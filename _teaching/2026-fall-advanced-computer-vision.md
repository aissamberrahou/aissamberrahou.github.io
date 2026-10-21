---
title: "Advanced computer vision"
collection: teaching
type: "Graduate course"
permalink: /teaching/2026-fall-advanced-computer-vision
venue: "Ensias, Mohammed V University"
date: 2026-09-15
location: "Rabat, Morocco"
---
This course goes beyond image classification to the main tasks of modern computer vision: object detection, segmentation, 3D vision, video and generative models. Labs use Python, OpenCV and TensorFlow/Keras.

## Prerequisites
- The [Deep learning course](/teaching/2026-fall-deep-learning) (CNNs, training, transfer learning)
- Python, NumPy, linear algebra

## Lectures

|    | Course                                              | Slides | Video     |
|:---|:----------------------------------------------------|--------|-----------|
| 1  | Image formation, filtering and features (OpenCV refresher) | [PDF] | [Youtube] |
| 2  | CNN architectures for vision (ResNet, EfficientNet) | [PDF]  | [Youtube] |
| 3  | Object detection (R-CNN family, YOLO, SSD)          | [PDF]  | [Youtube] |
| 4  | Semantic and instance segmentation (U-Net, Mask R-CNN) | [PDF] | [Youtube] |
| 5  | Vision transformers and self-supervised learning    | [PDF]  | [Youtube] |
| 6  | Video analysis and action recognition               | [PDF]  | [Youtube] |
| 7  | 3D vision: geometry, depth, point clouds and 3D shape descriptors | [PDF] | [Youtube] |
| 8  | Generative models for vision (GAN, diffusion)       | [PDF]  | [Youtube] |
| 9  | Efficient vision on edge devices (quantization, pruning, TensorFlow Lite) | [PDF] | [Youtube] |
| 10 | Medical image analysis: a case study                | [PDF]  | [Youtube] |

## Labs

|    | Lab                                        | Tutorials/Labs | Solutions |
|:---|:-------------------------------------------|----------------|-----------|
| 1  | Image processing with OpenCV               | [Tutorial](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html) | [Sol] |
| 2  | Transfer learning and fine-tuning          | [Tutorial](https://www.tensorflow.org/tutorials/images/transfer_learning) | [Sol] |
| 3  | Object detection                           | [Lab] | [Sol] |
| 4  | Image segmentation with U-Net              | [Tutorial](https://www.tensorflow.org/tutorials/images/segmentation) | [Sol] |
| 5  | Vision transformer                         | [Examples](https://keras.io/examples/vision/) | [Sol] |
| 6  | Deploying a vision model with TensorFlow Lite | [Lab] | [Sol] |

## Mini-project
In groups, students build an end-to-end vision application (detection, segmentation or 3D analysis) on a real dataset and present their results.

## Background materials
1. [Computer Vision: Algorithms and Applications (R. Szeliski, free online)](https://szeliski.org/Book/)
2. [Stanford CS231n course notes](https://cs231n.github.io/)
3. [OpenCV documentation](https://docs.opencv.org/)
4. [Keras computer vision examples](https://keras.io/examples/vision/)
