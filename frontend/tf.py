import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import PIL.Image
from tensorflow.keras import datasets, layers, models

# with open("../media/images/cesi.png", "rb") as image:
ds = tfds.load('mnist', split="train", shuffle_files=True)

ds = ds.shuffle(1024).batch(32).prefetch(tf.data.experimental.AUTOTUNE)
for example in ds.take(1):
    image, label = example["image"], example["label"]
    print(image, label)
