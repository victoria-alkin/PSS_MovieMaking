import sys
import vtk
#from PyQt5 import QtCore, QtGui
#from PyQt5 import Qt
#from PyQt5.QtWidgets import QShortcut ,  QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QGridLayout, QMessageBox
#from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import csv
import json
import os
import pickle
import pandas as pd
import numpy as np
#import moviepy
import trimesh
import meshparty
from meshparty import trimesh_io, trimesh_vtk

# Create a set of 120 png images vizualizing the full rotation of each mesh
# Change mesh filename manually
spinemesh1 = trimesh.exchange.load.load_mesh(r'data\PSS_meshes\27.off')
spinemesh1_actor = trimesh_vtk.mesh_actor(spinemesh1, color=(0,1,0), opacity=0.6)
locmesh1 = trimesh.exchange.load.load_mesh(r'data\local_meshes\27.off')
locmesh1_actor = trimesh_vtk.mesh_actor(locmesh1, color=(1,1,1), opacity=0.1)
renderer1 = trimesh_vtk.render_actors(actors=[spinemesh1_actor,locmesh1_actor],do_save=False)

# When vtk window appears with PSS and local mesh actors, manually rotate meshes to desired orientation
cam = renderer1.GetActiveCamera()
trimesh_vtk.render_actors_360(actors=[spinemesh1_actor,locmesh1_actor],camera_start=cam,directory='pss_images\pt27',nframes=120,do_save=True)