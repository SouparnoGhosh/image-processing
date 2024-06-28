# Programming Assignment-2 on course CSL506_IVP_S24
This repository contains solutions to the Programming Assignment-2 on course CSL506_IVP_S24. 

## Questions
### Q1
In the image 'line.bmp', only the circular objects are counted by assigning a different label to a disconnected circular object. Appropriate morphological operations are used and the corresponding output image is shown with a brief description of the algorithm.

### Q2
A function Myrgb2hsi is implemented to convert RGB to HSI. It takes an image 'ball.bmp' and returns normalized hue, saturation, and intensity values. The function's results are compared with OpenCV/Matlab's conversion function. Differences between the results are displayed and explained.

### Q4
A program is written to match the given two images based on Feature Matching technique. SIFT algorithm is used for feature detection and brute-force approach is used for feature matching. The images 'query.jpg' and 'train.jpg' are used to test the program. NOTE: install "pip install opencv-contrib-python" to use builtin SIFT descriptor.

### Q5
A program is implemented to detect moving vehicles by using mean and median differencing background subtraction techniques. Observations and comparisons on the result are mentioned. The video clip 'traffic.3gp' is used to test the code.

### Q6
An image ‘city.jpg’ depicting a city block is given. Superpixel based thresholding is applied to perform segmentation of the buildings.

### How to Run
Each question is solved in a separate Python file in the 'IPU_2' folder. To run any solution, navigate to the file and run the Python script. Make sure you have the necessary images or video clips in the same directory as the Python script.