import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
from moviepy.editor import VideoFileClip, clips_array, vfx

# Create video from two video components previously created
clip1 = VideoFileClip("moviept1.mp4").resize(width=800)
clip2 = VideoFileClip("moviept2.mp4").resize(width=1100)
final_clip = clips_array([[clip1,clip2]])
final_clip.write_videofile("PSSmovie.mp4")