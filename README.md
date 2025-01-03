Some practical ComfyUI image/mask process nodes make you earn some real money! (Yuan means chinese currency).


UPDATE

v1.0.1
add a mask preprocess node by morpholog：Mask Preprocess Morphology,
Fixed the issue with the processing of masks in this project (https://github.com/BadCafeCode/masquerade-nodes-comfyui), which would have caused the mask to be output in image format and not be used directly in subsequent generation processes

v1.0.0
add a node which allows load random image(s) form Local directory.

NODES INSTRUCTION

black and white: a Gray level map generator, generating greyscale image.
photoshop transfer: Transfer like photoshot, such as 'hard light, multiply' and so on...You can use this node to preserve artwork details such as text.
Image Minus Mask: using original image and mask generates the segmented image. You can choose the color type of the fill area. As example shows:
![Yuan nodes](https://github.com/user-attachments/assets/873565b0-5c3c-4e2a-96c7-ea03aa85f288)


you can download the default workflow from 'examples' or from this url:
https://github.com/Cyber-Blacat/ComfyUI-Yuan/blob/main/examples/Yuan%20example%20workflow.json


by Cyber_BCat
