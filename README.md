# PSS-Movie
Creating a video highlighting different post-synaptic shapes. The left half of the video shows a plot of all the dataset points associated with a post-synaptic shape, and highlights one selected point at a time. The right half of the video shows a visualization of a rotation of the mesh of the post-synaptic shape and local region associated with the highligted selected points.

The movie is made by subsequently running five python files. This is so that if an edit is made in one component of the movie, the user doesn't have to wait for the other components of the movie to be re-rendered as well (for instance, if an edit is made in the left half of the video, the user doesn't have to wait for the right half of the video to be re-rendered).

To make the left half of the video:
1. Run moviept1.py with the desired points stored in moviepoints.csv in the data folder to create the video.

To make the right half of the video:
1. Run PSSimages.py with the desired PSS meshes and local meshes in data\PSS_meshes and data\local_meshes to create a set of 120 png images vizualizing the full rotation of each mesh.
2. Run PSSmovies.py to create a video for each set of 120 images visualizing the rotation of the PSS and local region meshes.
3. Run moviept2.py to compile one video from the videos created for each point.

To make the full video: 
1. Run fullmovie.py (after moviept1.mp4 and moviept2.mp4 are made).
