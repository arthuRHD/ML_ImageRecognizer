import tensorflow as tf
from os.path import dirname, abspath, join


dataset_name = "dataset"
classnames = ["Animaux", "Humains", "PersoFictifs", "Plantes", "Vehicules"]

batch_size = 32
img_height = 180
img_width = 180

num_training_runs = 10
export_dir = abspath(join(dirname(__file__), dataset_name))

AUTOTUNE = tf.data.experimental.AUTOTUNE
