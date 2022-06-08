import numpy as np


from tensorflow.python.keras.models import load_model
from keras.utils.image_utils import load_img, img_to_array

# Rutas
model_dir = 'model/model.h5'
weights_dir = 'model/weights.h5'

# Parametros
img_height = 100
img_width = 100
class_names = ['Bottle gourd', 'Brinjal', 'Broccoli', 'Cabbage', 'Capsicum', 'Carrot',
               'Cauliflower', 'Cucumber']


model = load_model(model_dir)
model.load_weights(weights_dir)


def predict(file):
    x = load_img(file, target_size=(img_height, img_width))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    arr = model.predict(x)
    result = arr[0]
    response = np.argmax(result)

    return class_names[response]
