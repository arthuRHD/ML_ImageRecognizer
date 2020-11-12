import tensorflow as tf

dataset_name = "flower_photos"
dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"

batch_size = 32
img_height = 180
img_width = 180
num_classes = 5
num_training_runs = 10

AUTOTUNE = tf.data.experimental.AUTOTUNE
