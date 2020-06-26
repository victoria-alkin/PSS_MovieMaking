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
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Compile one video from the videos created for each point
clips_list = []
for i in range (29):
    clip_name = r"pss" + str(i+1) + ".mp4"
    clip = VideoFileClip(clip_name)
    clips_list.append(clip)

final_clip = concatenate_videoclips(clips_list)
final_clip.write_videofile("moviept2.mp4")