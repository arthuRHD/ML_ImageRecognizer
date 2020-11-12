import tensorflow as tf
from os import path

dataset_name = "Data"
dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
num_classes = 5
classnames = ["Animaux", "Humains", "PersoFictifs", "Plantes", "Vehicules"]

batch_size = 32
img_height = 180
img_width = 180

num_training_runs = 10
export_dir = path.abspath(path.join(path.dirname(__file__), dataset_name))

AUTOTUNE = tf.data.experimental.AUTOTUNE
