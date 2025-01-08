# Driver Fatigue Detection with Vision Transformer Models

This repository demonstrates a **Driver Fatigue Detection System** using various Vision Transformer (ViT) models. By comparing the performance of different ViT variants, we aim to build a robust system that can accurately detect driver drowsiness.

---

## Table of Contents
- [Introduction](#introduction)  
- [Models Used](#models-used)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Results and Comparison](#results-and-comparison)  
- [Contributing](#contributing)  
- [License](#license)

---

## Introduction
Fatigue is one of the leading causes of road accidents. This project leverages state-of-the-art Vision Transformer models to detect drowsiness in drivers. By using multiple models such as **DeiT**, **LeViT**, **Swin Transformer**, **BEiT**, and others, we explore their performance on the driver fatigue detection task.

---

## Models Used
This repository includes the implementation and evaluation of the following models:

1. **DeiT (Data-efficient Image Transformer)**  
   - A lightweight Vision Transformer optimized for high accuracy with smaller datasets.  
   
2. **LeViT**  
   - A fast and efficient Vision Transformer designed for low-latency applications, making it ideal for real-time fatigue detection.  
   
3. **Vision Transformer (ViT)**  
   - The standard Vision Transformer architecture, offering high accuracy for a variety of vision tasks.  

4. **Swin Transformer**  
   - A hierarchical Vision Transformer that processes images at multiple scales, improving performance on dense prediction tasks such as object detection and segmentation.  
   - Due to its efficiency and high accuracy, it’s well-suited for real-time driver fatigue detection in complex environments.

5. **BEiT (Bidirectional Encoder representation from Image Transformers)**  
   - A self-supervised Vision Transformer model that learns visual representations by treating image patches as tokens, similar to language models.  
   - BEiT’s pretraining approach allows it to achieve high performance on downstream tasks with minimal labeled data.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/fa7ih/surucuyorgunluk.git
   cd surucuyorgunluk
