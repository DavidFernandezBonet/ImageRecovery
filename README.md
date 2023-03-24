# Image Recovery

<img src="image_recovery_scheme.png" width="500" height="500" />





This is a companion repository to our [paper](https://www.biorxiv.org/content/10.1101/2022.09.29.510142v1) (Fernandez Bonet & Hoffecker 2023, Image recovery from unknown network mechanisms for DNA sequencing-based microscopy).

See [`demo.ipynb`](https://github.com/DavidFernandezBonet/ImageRecovery/blob/master/Code/Tutorials/demo.ipynb) for a step-by-step guide.

The other notebooks generate figures that we have in the paper:

* [`Distortion plots`](https://github.com/DavidFernandezBonet/ImageRecovery/blob/master/Code/Tutorials/Distortion%20plots%20.ipynb)
* [`Computational Complexity`](https://github.com/DavidFernandezBonet/ImageRecovery/blob/master/Code/Tutorials/Computational%20Complexity.ipynb)
* [`Scalability and Accuracy`](https://github.com/DavidFernandezBonet/ImageRecovery/blob/master/Code/Tutorials/Scalability%20and%20Accuracy.ipynb)

# Installation Guide

It is reccomended to clone this repository and play around with our Jupyter Notebook tutorial: [`demo.ipynb`](https://github.com/DavidFernandezBonet/ImageRecovery/blob/master/Code/Tutorials/demo.ipynb). However, it is possible to easily install ImageRecovery using 'pip': 

   `pip install ImageRecovery`

This command will install the latest version of the package.

Once the installation is complete, you can start using the package by importing it in your Python code:

   `import ImageRecovery`

# Minimum Working Example

Here's an example Python code that uses the `ImageRecovery` package. It recovers a 3D image and creates an animation of the result.

```python
import ImageRecovery
import os

parent_dir = os.getcwd()
ImageRecovery.create_folder_structure(parent_dir)
args = ImageRecovery.Im_Rec_Arguments()
args.mode_3D = True
args.plot_mode = True
args.mode_anim = True
params = args.__dict__
ImageRecovery.recover_image(params)
```

![Image Recovery](recov_image_animated.gif)
