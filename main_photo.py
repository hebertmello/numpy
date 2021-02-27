import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from PIL import Image

photo = io.imread('recife.jpg')
print(photo.shape)
# rows, columns, channels of RGB
# (365, 650, 3)

# revers the image (revers the rows)
img = Image.fromarray(photo[::-1], 'RGB')
img.save('recife1.jpg')

# a mirror image (revers the columns)
img = Image.fromarray(photo[:, ::-1], 'RGB')
img.save('recife2.jpg')

# a section of the image
img = Image.fromarray(photo[50:350, 150:280], 'RGB')
img.save('recife3.jpg')

# halv the size of the image
img = Image.fromarray(photo[::2, ::2], 'RGB')
img.save('recife4.jpg')

photo2 = io.imread('recife4.jpg')
print(photo2.shape)
# rows, columns, channels of RGB
# (183, 325, 3)

