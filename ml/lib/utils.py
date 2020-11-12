import tensorflow as tf
from tensorflow.keras import layers
from .config import (batch_size, img_height, img_width, AUTOTUNE, export_dir, num_classes)
import pathlib


def download_dataset(dataset_url: str, dataset_name: str):
    data_directory = tf.keras.utils.get_file(origin=dataset_url, 
                                   fname=dataset_name, 
                                   untar=True)
    data_directory_path = pathlib.Path(data_directory)
    return data_directory_path


def create_model():
    model = tf.keras.Sequential([
        layers.experimental.preprocessing.Rescaling(1./255),
        layers.Conv2D(32, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes)
    ])
    model.compile(
        optimizer='adam',
        loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy']
    )
    return model


def get_model():
    if tf.saved_model.contains_saved_model(export_dir):
        model = tf.keras.models.load_model(export_dir)
    else:
        raise FileNotFoundError(f"{export_dir} does not contain models")
    return model


def launch_training(model_to_train: tf.keras.Sequential, runs: int, training_dataset, validation_dataset):
    print("Training model")
    model_to_train.fit(
        training_dataset,
        validation_data=validation_dataset,
        epochs=runs
    )
    print("Saving model")
    tf.saved_model.save(model_to_train, export_dir)


def create_image_dataset(data_dir: pathlib.Path, dataset_subset: str):
    return tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset=dataset_subset,
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size
    ).cache().prefetch(buffer_size=AUTOTUNE)


def get_normalization_layer():
    return tf.keras.layers.experimental.preprocessing.Rescaling(1./255)


def create_normalized_dataset(training_dataset):
    normalized_ds = training_dataset.map(
        lambda x, y: (get_normalization_layer()(x), y)
    )
    return normalized_ds
    