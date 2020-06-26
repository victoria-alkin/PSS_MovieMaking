import math
import numpy as np
import pandas as pd
import pickle
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

# Read data for all 1000 points from file and create dataframe
labels_file = open(r"data\labels.pkl","rb")
labels_db = pickle.load(labels_file)
labels_file.close()
labels_df = pd.DataFrame(labels_db)

# Read data for selected movie points from file and create dataframe
points_df = pd.read_csv(r"data\moviepoints.csv")

# Create movie
fig, ax = plt.subplots()

# Plot all 1000 points in color corresponding to label
ax.clear()
def make_frame(t):
    ax.clear()
    for i in range(len(labels_df)):
        ptcolor = ""
        if labels_df.iloc[i,4] == '1':
            ptcolor = "red"
        if labels_df.iloc[i,4] == '2':
            ptcolor = "limegreen"
        if labels_df.iloc[i,4] == '3':
            ptcolor = "gold"
        if labels_df.iloc[i,4] == '4':
            ptcolor = "orange"
        if labels_df.iloc[i,4] == '5':
            ptcolor = "lightcoral"
        if labels_df.iloc[i,4] == '6':
            ptcolor = "palegreen"
        if labels_df.iloc[i,4] == '7':
            ptcolor = "maroon"
        if labels_df.iloc[i,4] == '8':
            ptcolor = "darkgreen"
        if labels_df.iloc[i,4] == '9':
            ptcolor = "slategrey"
        x = labels_df.iloc[i,0]
        y = labels_df.iloc[i,1]
        ax.scatter(x, y, color = ptcolor, s=25, alpha = 0.1)

    # Create legend of colors corresponding to labels
    spine_patch = mpatches.Patch(color = "red", label = "spine")
    shaft_patch = mpatches.Patch(color = "limegreen", label = "shaft")
    soma_patch = mpatches.Patch(color = "gold", label = "soma")
    ais_patch = mpatches.Patch(color = "orange", label = "proximal process")
    partialspine_patch = mpatches.Patch(color = "lightcoral", label = "partial spine")
    partialshaft_patch = mpatches.Patch(color = "palegreen", label = "partial shaft")
    mergedspine_patch = mpatches.Patch(color = "maroon", label = "merged spine")
    mergedshaft_patch = mpatches.Patch(color = "darkgreen", label = "merged shaft")
    unknown_patch = mpatches.Patch(color = "slategrey", label = "unknown")
    plt.legend(handles = [spine_patch, shaft_patch, soma_patch, ais_patch, partialspine_patch, partialshaft_patch, mergedspine_patch, mergedshaft_patch, unknown_patch], fontsize = 'x-small')

    # Plot one selected movie point at a time in color corresponding to label
    ptcolor2=""
    if points_df.iloc[math.trunc(int(t/3)),5] == 1:
        ptcolor2 = "red"
    if points_df.iloc[math.trunc(int(t/3)),5] == 2:
        ptcolor2 = "limegreen"
    if points_df.iloc[math.trunc(int(t/3)),5] == 3:
        ptcolor2 = "gold"
    if points_df.iloc[math.trunc(int(t/3)),5] == 4:
        ptcolor2 = "orange"
    if points_df.iloc[math.trunc(int(t/3)),5] == 5:
        ptcolor2 = "lightcoral"
    if points_df.iloc[math.trunc(int(t/3)),5] == 6:
        ptcolor2 = "palegreen"
    if points_df.iloc[math.trunc(int(t/3)),5] == 7:
        ptcolor2 = "maroon"
    if points_df.iloc[math.trunc(int(t/3)),5] == 8:
        ptcolor2 = "darkgreen"
    if points_df.iloc[math.trunc(int(t/3)),5] == 9:
        ptcolor2 = "slategrey"
    curX = points_df.iloc[math.trunc(int(t/3)),1]
    curY = points_df.iloc[math.trunc(int(t/3)),2]
    ax.scatter(curX, curY, color = ptcolor2, s=40)
    return mplfig_to_npimage(fig)

# Create video clip
animation = VideoClip(make_frame,duration=87)
animation.write_videofile('moviept1.mp4', fps=1)