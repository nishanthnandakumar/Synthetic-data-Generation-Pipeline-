# A Synthetic Image Generation Pipeline for Vision-Based AI in Industrial Applications

The original paper is available here [here](https://www.mdpi.com/2076-3417/15/23/12600)..

Collecting and annotating large-scale image datasets continues to pose a major obstacle for training vision-based AI models, particularly in industrial automation. This challenge becomes even more critical in quality inspection tasks within Flexible Manufacturing Systems and Batch-Size-of-One production, where the high variability of components limits the availability of suitable datasets.

This work introduces a pipeline designed to generate photorealistic synthetic images to support automated visual inspection. Synthetic renderings created from geometric models of manufactured parts are refined using a Cycle-Consistent Adversarial Network (CycleGAN), which transfers pixel-level characteristics from real camera images. The pipeline is demonstrated in two use cases:

1. Domain transfer between similar objects to augment existing data, and

2. Domain transfer between dissimilar objects to generate images prior to actual production.

The generated images are evaluated using mean Average Precision (mAP) in the first scenario and the Turing test in the second. The pipeline is additionally validated in two industrial setups: object detection for a Niryo robot performing a pick-and-place task, and anomaly detection in items produced by a FESTO machine.

The results show that the proposed pipeline effectively generates high-quality training data for vision-based AI in industrial environments, underscoring the importance of improving domain realism in synthetic data workflows.

## Getting started
Please follow the instructions provided in the respective repositories to implement the code.

## External Dependencies

The following are required to run the project successfully,

1. docker
2. docker compose
3. nvidia docker
4. Ubuntu

## Authors

Nishanth Nandakumar 
Jörg Eberhardt

## Project Status

Completed

## Citation

If you use any part of this code, please make sure to cite this paper.

'''
@article{nandakumar2025synthetic,
  title={A Synthetic Image Generation Pipeline for Vision-Based AI in Industrial Applications},
  author={Nandakumar, Nishanth and Eberhardt, J{\"o}rg},
  journal={Applied Sciences},
  volume={15},
  number={23},
  pages={12600},
  year={2025},
  publisher={MDPI}
}
'''

