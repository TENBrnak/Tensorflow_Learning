import os
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

File = "C:\\Users\\tomik\\Downloads\\dogs-vs-cats.zip"
zip_dir = tf.keras.utils.get_file("dogs-vs-cats.zip", origin="C:\\Users\\tomik\\Downloads\\dogs-vs-cats.zip", extract=True)

base_dir = os.path.join(os.path.dirname(zip_dir), 'cats_and_dogs_filtered')
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

train_cats_dir = os.path.join(train_dir, 'cats')  # directory with our training cat pictures
train_dogs_dir = os.path.join(train_dir, 'dogs')  # directory with our training dog pictures
validation_cats_dir = os.path.join(validation_dir, 'cats')  # directory with our validation cat pictures
validation_dogs_dir = os.path.join(validation_dir, 'dogs')  # directory with our validation dog pictures