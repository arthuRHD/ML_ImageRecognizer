# Testing model here
import tensorflow as tf
import numpy as np
from lib.config import (img_height, img_width, export_dir, classnames, tested_picture_path)
import sys


tested_picture_path = sys.argv[1]

img = tf.keras.preprocessing.image.load_img(
    tested_picture_path, target_size=(img_height, img_width)
)
img_array = tf.keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0)

model = tf.keras.models.load_model(export_dir)
predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

classname_predicted = classnames[np.argmax(score)]
resultat = f"Cette image appartient à la catégorie {classname_predicted} ({100 * np.max(score)})"
print(resultat)