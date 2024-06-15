import tensorflow as tf
import tensorflow.keras as keras
import tensorflow.keras.utils as utils
import tensorflow.keras.layers as layers
import tensorflow.keras.losses as losses
import tensorflow.keras.optimizers as optimizers

model = keras.Sequential([
	layers.Conv2D(32, (3, 3), padding='same', input_shape=(256, 256, 3)),
	layers.Activation('relu'),
	layers.BatchNormalization(),
	layers.MaxPooling2D(pool_size=(4, 4)),
	layers.Dropout(0.3),

	layers.Conv2D(32, (3, 3), padding='same'),
	layers.Activation('relu'),
	layers.BatchNormalization(),
	layers.MaxPooling2D(pool_size=(4, 4)),
	layers.Dropout(0.3),

	layers.Conv2D(32, (3, 3), padding='same'),
	layers.Activation('relu'),
	layers.BatchNormalization(),
	layers.MaxPooling2D(pool_size=(4, 4)),
	layers.Dropout(0.3),

	layers.Conv2D(32, (3, 3), padding='same'),
	layers.Activation('relu'),
	layers.BatchNormalization(),
	layers.MaxPooling2D(pool_size=(4, 4)),
	layers.Dropout(0.3),

	layers.Conv2D(32, (3, 3), padding='same'),
	layers.Activation('relu'),
	layers.BatchNormalization(),

	layers.Conv2D(32, (3, 3), padding='same'),
	layers.Activation('relu'),
	layers.BatchNormalization(),

	layers.Flatten(),
	layers.Dense(512, kernel_regularizer='l1'),
	layers.Activation('relu'),
	layers.BatchNormalization(),

	layers.Dense(11, kernel_regularizer='l1'),
	layers.Activation('softmax')
])

model.load_weights("arise_weights.h5")

model.save("arise_fullsave_2-9")