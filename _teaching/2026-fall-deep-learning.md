---
title: "Deep learning"
collection: teaching
type: "Graduate course"
permalink: /teaching/2026-fall-deep-learning
venue: "Ensias, Mohammed V University"
date: 2026-10-01
location: "Rabat, Morocco"
---
This deep learning course follows on from the machine learning course. It covers neural networks from the ground up, from the perceptron and backpropagation to convolutional networks, recurrent networks and transformers, with hands-on labs in TensorFlow/Keras.

# Welcome
The course is built around Jupyter notebooks so you can experiment with every model and training technique. You'll learn how deep networks work, how to train them reliably, and how to apply them to images, sequences and text.

## Prerequisites
- The [Machine learning course](/teaching/2014-spring-teaching-1) (model evaluation, regression, gradient descent)
- Python and NumPy
- Linear algebra, basic calculus and probability

## Lectures
Lectures are available as slides (PDF) and videos. Each lecture has a recommended reading from the free book *Dive into Deep Learning*.

|    | Course                                   | Slides | Video     | Reading |
|:---|:-----------------------------------------|--------|-----------|---------|
| 1  | Introduction to deep learning            | [PDF]  | [Youtube] | [D2L ch. 1](https://d2l.ai/chapter_introduction/index.html) |
| 2  | Perceptron and multilayer perceptrons    | [PDF]  | [Youtube] | [D2L ch. 5](https://d2l.ai/chapter_multilayer-perceptrons/index.html) |
| 3  | Backpropagation and automatic differentiation | [PDF] | [Youtube] | [D2L 5.3](https://d2l.ai/chapter_multilayer-perceptrons/backprop.html) |
| 4  | Optimization (SGD, momentum, Adam, learning rate schedules) | [PDF] | [Youtube] | [D2L ch. 12](https://d2l.ai/chapter_optimization/index.html) |
| 5  | Regularization (weight decay, dropout, batch normalization) | [PDF] | [Youtube] | [D2L 3.7](https://d2l.ai/chapter_linear-regression/weight-decay.html), [D2L 5.6](https://d2l.ai/chapter_multilayer-perceptrons/dropout.html) |
| 6  | Convolutional neural networks (CNN)      | [PDF]  | [Youtube] | [D2L ch. 7](https://d2l.ai/chapter_convolutional-neural-networks/index.html) |
| 7  | Modern CNN architectures and transfer learning | [PDF] | [Youtube] | [D2L ch. 8](https://d2l.ai/chapter_convolutional-modern/index.html) |
| 8  | Recurrent neural networks (RNN, LSTM, GRU) | [PDF] | [Youtube] | [D2L ch. 9](https://d2l.ai/chapter_recurrent-neural-networks/index.html), [ch. 10](https://d2l.ai/chapter_recurrent-modern/index.html) |
| 9  | Attention and transformers               | [PDF]  | [Youtube] | [D2L ch. 11](https://d2l.ai/chapter_attention-mechanisms-and-transformers/index.html) |
| 10 | Generative models (autoencoders, VAE, GAN) | [PDF] | [Youtube] | [D2L ch. 20](https://d2l.ai/chapter_generative-adversarial-networks/index.html) |


## Labs
Labs use TensorFlow 2 and its Keras API. Run the notebooks locally or launch them in Google Colab (a free GPU is available under *Runtime > Change runtime type*). Please review the relevant tutorial *before* the lab session.

|    | Course                       | Tutorials/Labs | Solutions |
|:---|:-----------------------------|----------------|-----------|
| 1  | TensorFlow basics: tensors and automatic differentiation | [Tensors](https://www.tensorflow.org/guide/tensor), [GradientTape](https://www.tensorflow.org/guide/autodiff) | [Sol] |
| 2  | MLP from scratch with NumPy, then with Keras | [Tutorial](https://www.tensorflow.org/tutorials/quickstart/beginner), [Lab] | [Sol] |
| 3  | Training a classifier (optimizers, regularization) | [Lab] | [Sol] |
| 4  | Image classification with a CNN | [Tutorial](https://www.tensorflow.org/tutorials/images/cnn) | [Sol] |
| 5  | Transfer learning | [Tutorial](https://www.tensorflow.org/tutorials/images/transfer_learning) | [Sol] |
| 6  | Sequence modelling with LSTM | [Tutorial](https://www.tensorflow.org/text/tutorials/text_classification_rnn) | [Sol] |
| 7  | Transformers and attention | [Tutorial](https://www.tensorflow.org/text/tutorials/transformer) | [Sol] |
| 8  | Autoencoders and generative models | [Tutorial](https://www.tensorflow.org/tutorials/generative/autoencoder) | [Sol] |


## Mini-project
In groups of 2–3, students apply deep learning to a dataset of their choice (images, text, time series or audio). Deliverables: a notebook with the full pipeline (data, model, training, evaluation) and a short presentation.


## Background materials
### Recommended books (free online)
1. [Dive into Deep Learning (A. Zhang et al.)](https://d2l.ai/)
2. [Deep Learning (I. Goodfellow, Y. Bengio, A. Courville)](https://www.deeplearningbook.org/)
3. [Understanding Deep Learning (S. Prince)](https://udlbook.github.io/udlbook/)
4. [Mathematics for Machine Learning (M.P. Deisenroth et al.)](https://mml-book.github.io/book/mml-book.pdf)

### Recommended resources
1. [The official TensorFlow Tutorials](https://www.tensorflow.org/tutorials)
2. [Keras code examples](https://keras.io/examples/)
3. [Stanford CS231n: CNNs for Visual Recognition (course notes)](https://cs231n.github.io/)
4. [Google Machine Learning crash course](https://developers.google.com/machine-learning/crash-course)
