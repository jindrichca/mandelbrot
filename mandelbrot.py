# mandelbrot.py 
# version 1.0
# By: Charlie Jindrich
# Date: 6/24/2023

# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import cmath
import time

############################################################################
### PARAMS #################################################################

'''

 resolution:

 	Determines the resolution of the rendered image. Image dimensions will 
 	be equal to 'resolution'. It is suggested to start with a small value 
 	(256) and work up as rendering times increase as 'resolution' increases.

 	Accepts a positive integer.

 axis_stop:

 	Determines the positive and negative limits of the x and y values used in 
 	calculations. It is suggested to use a value between 1 and 2.

 	Accepts a positve rational number.

 cutoff:

 	Determines the value at which complex number 'z' is considered divergent.

 	Accepts a positive rational number.

 max_iterations:

 	Sets the max number of iterations in the while loop. Higher values result in
 	greater the detail in the rendered image and longer runtimes. It is suggested 
 	start at 40.

 	Accepts a positive integer.

'''

resolution = 8192
axis_stop = 1.5
cutoff = 30000
max_iterations = 100

#############################################################################
#############################################################################

# Start Time
st = time.time()

# Init image array
img = np.zeros((resolution, resolution))

# Define coordinate ranges
x_range = np.linspace(-axis_stop, axis_stop, num=resolution)
y_range = np.linspace(-axis_stop, axis_stop, num=resolution)

# Testing Values
c = 0+0j
x_index = 0
for x_val in x_range:
	y_index = 0
	for y_val in y_range:
		z = 0+0j
		
		c = complex(x_val, y_val)

		iteration = 0
		while (z.real < cutoff) and (z.imag < cutoff):
			z = (z*z) + c 
			#print('z =', z, '\nIter =', iteration)
			iteration += 1
			if iteration >= max_iterations:
				break

		img[x_index][y_index] = iteration
		y_index += 1

	x_index += 1

# End Time
et = time.time()

# Total Time
tt = et - st

plt.imshow(img)
plt.title('Mandelbrot Set || Elasped Time: ' + str(tt) + ' s')
plt.show()