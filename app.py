from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
import tensorflow as tf
from keras.utils import load_img
from PIL import Image

app = Flask(__name__)

# Load the pre-trained model and weights
model = load_model('models/my_model.h5')
model.load_weights('models/model_weights.h5')

# Define the class names
class_names = ['apple', 'banana', 'beetroot', 'bell pepper', 'cabbage', 'capsicum', 'carrot',
 'cauliflower', 'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic',
 'ginger', 'grapes', 'jalepeno', 'kiwi', 'lemon', 'lettuce', 'mango', 'onion',
 'orange', 'paprika', 'pear', 'peas', 'pineapple', 'pomegranate', 'potato',
 'raddish', 'soy beans', 'spinach', 'sweetcorn', 'sweetpotato', 'tomato',
 'turnip', 'watermelon']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(filename)
        
        img_height = 224
        img_width = 224

        def preprocess_image(image_path):
            # Load the image and resize it to match the input shape of your model
            img = tf.keras.utils.load_img(image_path, target_size=(img_height, img_width))

            img_array = tf.keras.utils.img_to_array(img)
            img_array = tf.expand_dims(img_array, 0) 
            predictions = class_names[model.predict(img_array).argmax()]
    
            return predictions

        result = preprocess_image(filename)
        
        return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)