# Real time fire Detection Using CNN Framework

Fire detection is an essential aspect of ensuring safety in various domains, including homes, factories, and commercial buildings. Traditional fire detection methods have limitations, and therefore, this project proposes an alternative fire detection method using a cost-effective CNN framework for flame detection in surveillance videos.

## Objective
The primary objective of this project is to develop a CNN-based flame detection model that can accurately and efficiently detect fires in surveillance videos. The approach aims to reduce the cost and complexity of fire detection systems and provide a more reliable and efficient solution.

## Methodology
The project utilizes a camera and computer to analyze the camera's output. The MobileNet CNN architecture was chosen as the base model due to its lightweight and efficient design, making it suitable for deployment in resource-constrained environments. The MobileNet architecture was modified and trained on a dataset consisting of 3GB of fire and non-fire images extracted from real-time footage. Transfer learning techniques were employed to leverage the pre-trained model's features and fine-tune them to the specific dataset.

The implementation was done in Python using the Keras deep learning library. The model was trained on a Kaggle CPU, achieving an overall accuracy of 99.3%. The flame detection process takes approximately 5-10 seconds per frame.

## Results
The model was tested on surveillance videos, and it demonstrated accurate flame detection with high precision. When fire detection occurred consecutively for 20 frames, the notification system was triggered, and a fire alarm was raised. This approach provides a cost-effective and efficient solution for flame detection in surveillance videos.

## Conclusion
In conclusion, we have proposed a CNN-based flame detection model that uses a cost-effective and efficient approach to detect fires in surveillance videos. The MobileNet CNN architecture used in the project is lightweight and efficient, making it suitable for deployment in resource-constrained environments. The model achieved an overall accuracy of 99.3% and can detect flames in videos with high precision. Our approach offers a reliable and cost-effective solution to fire detection and can be deployed in various domains, including homes, factories, and commercial buildings.
