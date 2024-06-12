import keras
import keras.models

def load_model(path):
    model = keras.models.load_model(path)
    print(model.summary())
    return model