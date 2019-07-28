#%%
import numpy as np
import tensorflow as tf
import math
import h5py
import matplotlib.pyplot as plt
import scipy
from scipy import ndimage
from PIL import Image
from tensorflow.python.framework import ops
from cnn_utils import *
#%%
X_train_orig, Y_train_orig, X_test_orig, Y_test_orig, classes = load_dataset()