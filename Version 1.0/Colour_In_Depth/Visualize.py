# Name:                                             Renacin Matadeen
# Student Number:                                         N/A
# Date:                                               03/29/2018
# Course:                                                 N/A
# Title                                       Image Clustering - K Means
#
#
#
#
#
# ----------------------------------------------------------------------------------------------------------------------

from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")

# ----------------------------------------------------------------------------------------------------------------------

"""
Purpose:
    Separate an image via its Red, Green, Blue channels; plot the subsequent points in a 3D space, an 
    make a simple animation
"""
# ----------------------------------------------------------------------------------------------------------------------

# Path To The Image
path = 'C:/Users/renac/Documents/Documents/Programming/Python/Image_Clustering/Images/Image.jpg'

# Open Image & Convert To List, Then To Numpy Array
img = Image.open(path, "r")
img = list(img.getdata())

# Create Separate Channels
r_list = []
g_list = []
b_list = []

# Append Values To List
for value in img:
    r_list.append(value[0])
    g_list.append(value[1])
    b_list.append(value[2])


# Save Images Of Rotated Axis, Reinstate To Clear/Save Memory
counter_x = 1
for angle in range(0, 360):

    # Instantiate Figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Display Data
    ax.scatter(r_list, g_list, b_list, c=(1, 0.3, 0.3, 0.3), s=0.2)
    ax.set_xlabel("Red")
    ax.set_ylabel("Green")
    ax.set_zlabel("Blue")

    # Remove Numbers
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_zticklabels([])

    # ax = plt.gca(projection='3d')
    # ax._axis3don = False

    ax.view_init(30, angle)
    plt.savefig('D:/Images/plot_' + str(counter_x) + '.png', dpi=200)
    counter_x += 1
    plt.close()
