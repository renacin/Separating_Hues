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
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")

# ----------------------------------------------------------------------------------------------------------------------

"""
Purpose:

    Using a K-Means algorithm, an image will be classified by R, G, B channels, in accordance to K number of clusters
    Using the cluster memberships, the average colour will be replaced, and an image will be produced where only K
    colours are shown. 
"""
# ----------------------------------------------------------------------------------------------------------------------

# Path To The Image
path = ''

# Get Image Dimensions
image_ = Image.open(path)
dimensions = list(image_.size)
columns = dimensions[0]
rows = dimensions[1]

# Open Image & Convert To List, Then To Numpy Array
img = Image.open(path, "r")
img = list(img.getdata())
X = np.array(img)

# Loop Through & Perform K-Means For An Increasing Number Of Clusters
counter_x = 1
for segments in range(1, 300):

    # Define Classifier
    k = segments
    clf = KMeans(n_clusters=k, max_iter=150)
    clf.fit(X)

    # Get Data From Classifier
    centroids = clf.cluster_centers_
    labels = clf.labels_

    # Reorganize To Pandas Dataframe
    df = pd.DataFrame(X)
    df.columns = ["Red", "Green", "Blue"]

    # Add New Labels
    df["Cluster_Membership"] = labels

    # Find Average Values
    df1 = pd.DataFrame()
    df1["Red"] = df.groupby('Cluster_Membership')['Red'].agg(["mean"])
    df1["Green"] = df.groupby('Cluster_Membership')['Green'].agg(["mean"])
    df1["Blue"] = df.groupby('Cluster_Membership')['Blue'].agg(["mean"])

    # Temporary Lists To Hold Values, Trying To Avoid O(n^2) At All Costs
    r_temp = []
    g_temp = []
    b_temp = []

    # Replace Original Pixel Values With Cluster Membership Average Value
    counter_df = 0
    for index, row in df.iterrows():
        cluster_mem = int(df["Cluster_Membership"][counter_df])

        r_temp.append(int(df1["Red"][cluster_mem]))
        g_temp.append(int(df1["Green"][cluster_mem]))
        b_temp.append(int(df1["Blue"][cluster_mem]))

        counter_df += 1

    # New RGB Field
    df3 = pd.DataFrame()
    df3["N_R"] = r_temp
    df3["N_G"] = g_temp
    df3["N_B"] = b_temp

    # Covert To List, Then Chunk & Append To Final List, Note Pixels Must Be In A Tuple
    raw_pixels_tuple = []
    raw_pixels = df3.values.tolist()

    for pixel in raw_pixels:
        pixel = tuple(pixel)
        raw_pixels_tuple.append(pixel)

    # Create Temp Image Skeleton
    background = (0, 0, 0, 255)
    final_image = Image.new("RGB", (columns, rows), background)
    final_image.putdata(raw_pixels_tuple)
    final_image.save('_' + str(counter_x) + '.jpg')
    counter_x += 1
