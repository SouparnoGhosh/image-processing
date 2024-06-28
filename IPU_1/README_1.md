# Programming Assignment-1 on course CSL442_IVP
This repository contains solutions to the Programming Assignment-1 on course CSL442_IVP.

## Questions
### Q1
**(a)** A function is created that converts a color image to grayscale and determines the predominant intensity value by finding the one that occurs most frequently in the image. The image used for this is 'tq.jpg'.

**(b)** A function is created to merge the images 'foreground.jpg' and 'background.jpg' as per the result given below.

### Q2
A function called ImageBitQuantizer is created that accepts an 8-bit image (im) and an integer k representing the desired number of bits for image quantization. The function returns the image quantized to k bits. The function is demonstrated using the image named "pixel.jpg."

### Q3
The attached image ‘spine.tiff’ is enhanced using (a) The log transformation and (b) A power-law transformation. In (a) the only free parameter is c, but in (b) there are two parameters, c and r for which values have to be selected. The best visual enhancement possible with the methods in (a) and (b) is obtained by experimentation. The major differences between them are explained.

### Q4
A program is written to implement spatial domain averaging filter, weighted averaging filter, median filter of size 3X3, 5X5 and its blurring effect on the given 'noise.tiff' image is observed. The optimum size of the kernel for median filter for which the features in the image ‘noise.tif’ are the clearest with minimum noise and deformation of the features is found. The inbuilt spatial filtering function is not used.

### Q5
An edge detection program is written using the inbuilt canny edge detection function and the results with different parameters like threshold, smoothing variance etc., are observed. The Laplacian filter and Sobel filter are also implemented and the anomalies in their respective outputs are observed. The image used for this is 'clown.png'.

### Q6
A program is written to find the largest correlation spot in the given image (hills.jpg) using linear filtering-based template matching technique. A rectangular bounding box is drawn at the detected template (template.png) matched locations. The images used for this are 'hills.jpeg', 'template.png'.

### How to Run
Each question is solved in a separate Python file. To run any solution, navigate to the file and run the Python script.