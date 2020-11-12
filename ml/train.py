from lib.utils import launch_training, create_model, create_image_dataset, download_dataset
from lib.config import (dataset_name, dataset_url, num_training_runs)


data_dir = download_dataset(dataset_url, dataset_name)
train_ds = create_image_dataset(data_dir, "training")
val_ds = create_image_dataset(data_dir, "validation")

if __name__ =='__main__':
    launch_training(
        model_to_train=create_model(),
        runs=num_training_runs,
        training_dataset=train_ds,
        validation_dataset=val_ds
    )
