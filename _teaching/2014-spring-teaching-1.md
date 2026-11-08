---
title: "Machine learning"
collection: teaching
order: 1
type: "Undergraduate course"
permalink: /teaching/2014-spring-teaching-1
venue: "Ensias, Mohammed V University"
date: 2021-01-01
location: "Rabat, Morocco"
---

This introductory machine learning course covers the main supervised methods (KNN, linear regression, SVM), how to validate and evaluate a model, and the main clustering methods (K-means, hierarchical agglomerative clustering, DBSCAN). Every lecture comes with a hands-on lab in Python and scikit-learn.



## Description

The course alternates between lectures and labs. Each algorithm is first worked out by hand on a small toy example from the slides (a few flowers, a screening test, a field yield as a function of temperature…), then re-implemented step by step with NumPy, checked against scikit-learn, and finally applied to a real dataset (Iris, Breast Cancer, Diabetes, Wine, `make_moons`). All lectures and labs are in French.

### Prerequisites

* Python programming (functions, lists, loops)
* Linear algebra, basic calculus and probability
* Basic statistics (mean, variance, distances)

### Tools

* Python 3 with [Jupyter](https://jupyter.org/) or [Google Colab](https://colab.research.google.com/)
* [NumPy](https://numpy.org/), [pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/)
* [scikit-learn](https://scikit-learn.org/) and [SciPy](https://scipy.org/)

## Objectives

By the end of the course, students will be able to:

1. Explain the machine learning workflow and tell supervised learning from unsupervised learning.
2. Evaluate a model properly: train/test split, k-fold cross-validation, confusion matrix, precision, recall, F1-score, ROC curve and AUC.
3. Fit a linear regression by least squares and by gradient descent, and assess it with the MSE and R².
4. Classify with the k-nearest neighbours algorithm and choose *k* by cross-validation.
5. Train a support vector machine (hard and soft margin, kernel trick) and tune its hyperparameters *C* and γ.
6. Group data with K-means, hierarchical agglomerative clustering and DBSCAN, and choose the number of clusters (elbow method, silhouette, dendrogram, k-distance plot).
7. Recognise under- and overfitting and the influence of hyperparameters and feature scaling.
8. Implement these algorithms from scratch with NumPy and use them in practice with scikit-learn.

## Course

Lectures are available as slides (in French), displayed in a read-only online viewer.

||Lecture|Slides|
|-|-|-|
|1|Introduction to machine learning|[Slides](/viewer/?d=bWx8TGVjdHVyZTFfSW50cm9kdWN0aW9ufHBkZnxMZWN0dXJlIDEg4oCUIEludHJvZHVjdGlvbiB0byBtYWNoaW5lIGxlYXJuaW5n)|
|2|Model validation and evaluation|[Slides](/viewer/?d=bWx8TGVjdHVyZTJfVmFsaWRhdGlvbnxwZGZ8TGVjdHVyZSAyIOKAlCBNb2RlbCB2YWxpZGF0aW9uIGFuZCBldmFsdWF0aW9u)|
|3|Linear regression|[Slides](/viewer/?d=bWx8TGVjdHVyZTNfUmVncmVzc2lvbnxwZGZ8TGVjdHVyZSAzIOKAlCBMaW5lYXIgcmVncmVzc2lvbg)|
|4|K-nearest neighbours (KNN)|[Slides](/viewer/?d=bWx8TGVjdHVyZTRfS05OfHBkZnxMZWN0dXJlIDQg4oCUIEstbmVhcmVzdCBuZWlnaGJvdXJzIChLTk4p)|
|5|Support vector machines (SVM)|[Slides](/viewer/?d=bWx8TGVjdHVyZTVfU1ZNfHBkZnxMZWN0dXJlIDUg4oCUIFN1cHBvcnQgdmVjdG9yIG1hY2hpbmVzIChTVk0p)|
|6|Clustering with K-means|[Slides](/viewer/?d=bWx8TGVjdHVyZTZfS01lYW5zfHBkZnxMZWN0dXJlIDYg4oCUIENsdXN0ZXJpbmcgd2l0aCBLLW1lYW5z)|
|7|Hierarchical agglomerative clustering (CAH)|[Slides](/viewer/?d=bWx8TGVjdHVyZTdfQ0FIfHBkZnxMZWN0dXJlIDcg4oCUIEhpZXJhcmNoaWNhbCBhZ2dsb21lcmF0aXZlIGNsdXN0ZXJpbmcgKENBSCk)|
|8|Density-based clustering (DBSCAN)|[Slides](/viewer/?d=bWx8TGVjdHVyZThfREJTQ0FOfHBkZnxMZWN0dXJlIDgg4oCUIERlbnNpdHktYmFzZWQgY2x1c3RlcmluZyAoREJTQ0FOKQ)|

## Labs

Labs are Jupyter notebooks (in French), displayed in a read-only online viewer. Each lab lasts about 2 hours and follows the same structure: learning objectives, theory reminder, a toy example worked out step by step, a case study on a real dataset, the influence of the hyperparameters, three exercises (easy, medium, challenge) with their solutions, and a summary.

||Lab|Notebook|
|-|-|-|
|1|Introduction to machine learning: NumPy basics, a toy model ŷ = w·x, exploring Iris, a first KNN and a first K-means|[Lab 1](/viewer/?d=bWx8VFBfMV9JbnRyb2R1Y3Rpb258bmJ8TGFiIDEg4oCUIEludHJvZHVjdGlvbiB0byBtYWNoaW5lIGxlYXJuaW5n)|
|2|Validation and evaluation: metrics by hand, imbalanced classes, ROC curve step by step, hold-out and k-fold on Breast Cancer, decision threshold|[Lab 2](/viewer/?d=bWx8VFBfMl9WYWxpZGF0aW9ufG5ifExhYiAyIOKAlCBWYWxpZGF0aW9uIGFuZCBldmFsdWF0aW9u)|
|3|Linear regression: least squares by hand, gradient descent, simple and multiple regression on Diabetes, residuals, polynomial overfitting|[Lab 3](/viewer/?d=bWx8VFBfM19SZWdyZXNzaW9ufG5ifExhYiAzIOKAlCBMaW5lYXIgcmVncmVzc2lvbg)|
|4|K-nearest neighbours: distances and vote, Iris, choosing *k* by cross-validation, decision boundaries, scaling on Wine|[Lab 4](/viewer/?d=bWx8VFBfNF9LTk58bmJ8TGFiIDQg4oCUIEstbmVhcmVzdCBuZWlnaGJvdXJz)|
|5|Support vector machines: hyperplane and margin, soft margin and *C*, kernel trick, RBF kernel on `make_moons`, Breast Cancer|[Lab 5](/viewer/?d=bWx8VFBfNV9TVk18bmJ8TGFiIDUg4oCUIFN1cHBvcnQgdmVjdG9yIG1hY2hpbmVz)|
|6|K-means: the algorithm step by step, local minima, elbow method and silhouette on Iris, `init` and `n_init`|[Lab 6](/viewer/?d=bWx8VFBfNl9LTWVhbnN8bmJ8TGFiIDYg4oCUIEstbWVhbnM)|
|7|Hierarchical agglomerative clustering: distance matrix, linkage criteria, dendrogram and cut, Iris|[Lab 7](/viewer/?d=bWx8VFBfN19DQUh8bmJ8TGFiIDcg4oCUIEhpZXJhcmNoaWNhbCBhZ2dsb21lcmF0aXZlIGNsdXN0ZXJpbmc)|
|8|DBSCAN: ε-neighbourhoods, core, border and noise points, choosing ε with the k-distance plot, non-convex clusters|[Lab 8](/viewer/?d=bWx8VFBfOF9EQlNDQU58bmJ8TGFiIDgg4oCUIERCU0NBTg)|

## References

### Books

1. A. Géron, *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow*, 3rd ed., O'Reilly, 2022
2. A. Müller, S. Guido, *Introduction to Machine Learning with Python*, O'Reilly, 2016
3. G. James, D. Witten, T. Hastie, R. Tibshirani, [*An Introduction to Statistical Learning*](https://www.statlearning.com/), 2nd ed., Springer, 2021 (free online)
4. M.P. Deisenroth, A.A. Faisal, C.S. Ong, [*Mathematics for Machine Learning*](https://mml-book.github.io/), Cambridge University Press, 2020 (free online)

### Online resources

1. [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html)
2. [Python basics (Automate the Boring Stuff)](https://automatetheboringstuff.com/3e/)
3. [Scientific Python Lectures (J.R. Johansson)](https://github.com/jrjohansson/scientific-python-lectures)
4. [Google Machine Learning crash course](https://developers.google.com/machine-learning/crash-course)

