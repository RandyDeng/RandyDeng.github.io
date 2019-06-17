---
layout: work_page
title: Nanoscale Barcode Identification
data: work
permalink: /work/barcode
---

As part of a graduate-level machine learning course, my group and I decided to classify nanoscale barcode images using a variety of classical and novel machine learning techniques. Using techniques such as Naive Bayes, Random Forest, Extreme Gradient Boosted Random Forest, Support Vector Machines with multiple kernels, and Convolutional Neural Networks (CNN), we were able to classify the images at around 75% accuracy with CNNs. Some of the challenges we faced included extremely noise data (some of the barcodes physically overlapped with each other) and efficiently training our models on an extremely large dataset.

A full project summary will be made available as soon as I am able.

<!--
### **Project Summary**
The identification and differentiation of a large number of distinct biological molecular compounds is a major challenge in biomedical science. In recent years, fluorescence microscopy has become an essential tool in biology due to its ability to tag nanometer and micrometer-sized entities using fluorophores. Unfortunately, limited availability of good, spectrally-differentiable, and biocompatible fluorophores have prevented practical large-scale multiplexing in fluorescence microscopy.

Our project attempts to classify 13 visually distinguishable fluorescent tags (barcodes) that arise from an assembly of 5 modular DNA origami monomers using standard machine learning techniques as well as deep learning approaches. Current methods generate multiple barcodes in a single image, have a lot of noise, and rely on either color or manual classification, which can be slow and cumbersome. Our system automates this process by segmenting data sample images using blob detection and classifying the individual barcodes using these models: Naive Bayes, Support Vector Machine, Random Forest, and Convolutional Neural Net (CNN). We evaluate each and use the most accurate classifier to identify the barcodes.

Our results show Adagrad CNN has the highest accuracy rate (85% during training, 75% during validation). The Support Vector Machine and Random Forest approaches also yielded similar, albeit slightly worse results and Naive Bayes yielded the lowest accuracy rate (55%).

The barcode image samples are provided to us by PhD Candidate Victor Pan, a student in the Department of Biomedical Engineering at Georgia Tech. 
-->