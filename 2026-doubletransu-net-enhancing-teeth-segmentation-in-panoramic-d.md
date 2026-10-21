---
title: "DoubleTransU-Net: Enhancing Teeth Segmentation in Panoramic Dental X-Ray Images"
collection: publications
category: manuscripts
permalink: /publication/2026-doubletransu-net-enhancing-teeth-segmentation-in-panoramic-d
date: 2026-01-01
venue: 'Algorithms'
paperurl: 'https://doi.org/10.3390/a19080685'
citation: 'Touahri, Manal, <b>Berrahou, Aissam</b> (2026). &quot;DoubleTransU-Net: Enhancing Teeth Segmentation in Panoramic Dental X-Ray Images.&quot; <i>Algorithms</i>, 19(8).'
---
Accurate teeth segmentation in panoramic dental radiographs remains a challenging task due to high image noise, low contrast, the similarity in intensity between teeth and surrounding tissues, and blurred tooth boundaries. To address these challenges, we propose DoubleTransU-Net, a dual-stage hybrid CNN–Transformer architecture that combines progressive segmentation refinement with global contextual feature learning. The first stage generates an initial tooth segmentation, while the second stage progressively refines ambiguous tooth regions to improve boundary delineation and segmentation accuracy. In addition, Atrous Spatial Pyramid Pooling (ASPP) modules capture multi-scale contextual information, whereas squeeze-and-excitation (SE) blocks enhance discriminative feature representations through channel-wise feature recalibration. The proposed model was evaluated on two public panoramic dental X-ray datasets, UFBA-UESC (1500 images) and Tufts (1000 images), and compared against several state-of-the-art segmentation models, including U-Net, DoubleU-Net, Attention U-Net, TransUNet, and DeepLabv3+. On the UFBA-UESC dataset, DoubleTransU-Net achieved an Accuracy of 95.54%, a Dice coefficient of 93.72%, an Intersection over Union (IoU) of 88.18%, a Precision of 93.57%, and a Recall of 94.24%. On the Tufts dataset, it achieved an Accuracy of 91.83%, a Dice coefficient of 92.93%, an IoU of 86.80%, a Precision of 92.27%, and a Recall of 93.97%. These results demonstrate that DoubleTransU-Net consistently outperforms existing state-of-the-art segmentation methods while exhibiting strong robustness and generalization across different panoramic dental datasets, highlighting its effectiveness for tooth semantic segmentation in panoramic dental X-ray images.

[Read the paper](https://doi.org/10.3390/a19080685)
