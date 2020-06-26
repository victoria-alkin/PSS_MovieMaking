import sys
import vtk
from PyQt5 import QtCore, QtGui
from PyQt5 import Qt
from PyQt5.QtWidgets import QShortcut ,  QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QGridLayout, QMessageBox
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import csv
import os
import pandas as pd
import numpy as np
import trimesh
import meshparty
from meshparty import trimesh_io, trimesh_vtk
import moviepy
from moviepy.editor import ImageSequenceClip

# Create video for each set of 120 images visualizing rotation of PSS and local meshes
for i in range(29):
    images_list = []
    video_name = "pss" + str(i+1) + ".mp4"
    directory = r"pss_images\pt" + str(i+1) + "\\"
    for i in range (90):
        if i < 10:
            filename = "000" + str(i) + ".png"
        elif i < 100:
            filename = "00" + str(i) + ".png"
        else:
            filename = "0" + str(i) + ".png"
        curFile = directory + filename
        images_list.append(curFile)
    clip = ImageSequenceClip(images_list, fps=30)
    clip.write_videofile(video_name)