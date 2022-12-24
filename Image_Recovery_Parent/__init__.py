import os

from image_recovery_main import *
from scalability_vs_metrics_plot import run_scalability_vs_metrics_plot_2d_and_3d
from complexity_plots import get_comp_complexity_both_plots
from plot_distortion_from_file import plot_all_dist_lines_fig3

# Scripts that contain executables


### START


# Create folders:
code_dir = os.getcwd()  # Code directory
os.chdir("..")  # Parent directory where data folders are
parent_dir = os.getcwd()
create_folder_structure(parent_dir)


# Timers:
first_initial_time = time.time()  # Set timer for all process
start_time = time.time()  # Set timer for each iteration (will change on iteration)




### Notebook 1 - Synthetic Data

# Simple reconstruction
args_obj = Im_Rec_Arguments()
args_obj.plot_mode = True
args_obj.pixel_art = "mario"
default_params = args_obj.__dict__
recover_image(default_params)  # returns quality metrics

# # Trying out different algorithms
# args_obj = Im_Rec_Arguments()
# args_obj.plot_mode = True
# args_obj.embedding_mode = "spring_relaxation"
# default_params = args_obj.__dict__
# recover_image(default_params)
#
# # Trying out different algorithms
# args_obj = Im_Rec_Arguments()
# args_obj.plot_mode = True
# args_obj.embedding_mode = "landmark_isomap"
# default_params = args_obj.__dict__
# recover_image(default_params)

# # Simple medium 3D reconstruction - Distortion plot (can take a while to align)
# args_obj = Im_Rec_Arguments()
# args_obj.density = 1000
# args_obj.mode_3D = True
# args_obj.plot_mode = True
# args_obj.align_to_original = True  # Compute distortion plot
# default_params = args_obj.__dict__
# recover_image((default_params))

# # Simple medium 3D reconstruction - Animation gif (can take a while to align)
# args_obj = Im_Rec_Arguments()
# args_obj.density = 2000
# args_obj.mode_3D = True
# args_obj.plot_mode = True
# args_obj.mode_anim = True  # Leave for last
# #args_obj.align_to_original = True  # Compute distortion plot
# default_params = args_obj.__dict__
# recover_image((default_params))




# # Notebook 2 - Experimental
# args_obj = Im_Rec_Arguments()
# args_obj.mode_3D = True
# args_obj.align_to_original = True
# args_obj.plot_mode = True
# args_obj.density = 1000 # Suggested value 1000 for quicker reconstructions
# args_obj.title_edge_list_experimental = "edge_list_knn_1000.csv"  # format IDnode1 IDnode2, e.g. "1 2\n1 6\n1 8\n..."
# args_obj.embedding_mode = "node2vec"
# default_params = args_obj.__dict__
# recover_image(default_params)
# os.chdir(code_dir)  # Parent directory where data folders are



print("Total time --- %s seconds ---" % (time.time() - first_initial_time))