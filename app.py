import numpy as np
import os
from tensorflow import keras
#from keras.preprocessing import image
import keras.utils as image
#import tensorflow_hub as hub
from flask import Flask, render_template, request

app = Flask(__name__)
model = keras.models.load_model('mobilenet_v3_large_final.h5')


@app.route('/')
def demo():
    return render_template('index.html')


# @app.route('/login', methods=['GET', 'POST'])
# def log():
#     user = request.form['name']
#     password = request.form['pass']
#     op = user, password
#     print(op)
#     return render_template('index.html', output=op)


@app.route('/predict', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':
        print("hello")
        f = request.files['image']
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(basepath, 'Uploads', f.filename)
        f.save(filepath)
        img = image.load_img(filepath, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        pred = np.argmax(model.predict(x), axis=1)
        print("hello2")
        index = ["Apple pie", 'Baby back ribs', 'Baklava', 'Beef carpaccio',
                 'Beef tartare',
                 'Beet salad',
                 'Beignets',
                 'Bibimbap',
                 'Bread pudding',
                 'Breakfast burrito',
                 'Bruschetta',
                 'Caesar salad',
                 'Cannoli',
                 'Caprese salad',
                 'Carrot cake',
                 'Ceviche',
                 'Cheesecake',
                 'Cheese plate',
                 'Chicken curry',
                 'Chicken quesadilla',
                 'Chicken wings',
                 'Chocolate cake',
                 'Chocolate mousse',
                 'Churros',
                 'Clam chowder',
                 'Club sandwich',
                 'Crab cakes',
                 'Creme brulee',
                 'Croque madame',
                 'Cup cakes',
                 'Deviled eggs',
                 'Donuts',
                 'Dumplings',
                 'Edamame',
                 'Eggs benedict',
                 'Escargots',
                 'Nachos',
                 'Filet mignon',
                 'Fish and chips',
                 'Foie gras',
                 'French fries',
                 'French onion soup',
                 'French toast',
                 'Fried calamari',
                 'Fried rice',
                 'Frozen yogurt',
                 'Garlic bread',
                 'Gnocchi',
                 'Greek salad',
                 'Grilled cheese sandwich',
                 'Grilled salmon',
                 'Guacamole',
                 'Gyoza',
                 'Hamburger',
                 'Ice Cream',
                 'Hot dog',
                 'Huevos rancheros',
                 'Hummus',
                 'Ice cream',
                 'Lasagna',
                 'Lobster bisque',
                 'Lobster roll sandwich',
                 'Macaroni and cheese',
                 'Macarons',
                 'Miso soup',
                 'Mussels',
                 'Nachos',
                 'Omelette',
                 'Onion rings',
                 'Oysters',
                 'Pad thai',
                 'Paella',
                 'Pancakes',
                 'Panna cotta',
                 'Peking duck',
                 'Pho',
                 'Pizza',
                 'Pork chop',
                 'Poutine',
                 'Prime rib',
                 'Pulled pork sandwich',
                 'Ramen',
                 'Ravioli',
                 'Red velvet cake',
                 'Risotto',
                 'Samosa',
                 'Sashimi',
                 'Scallops',
                 'Seaweed salad',
                 'Shrimp and grits',
                 'Spaghetti bolognese',
                 'Spaghetti carbonara',
                 'Spring rolls',
                 'Steak',
                 'Strawberry shortcake',
                 'Sushi',
                 'Tacos',
                 'Takoyaki',
                 'Tiramisu',
                 'Tuna tartare',
                 'Waffles']
        print(pred)
        print(len(index))
        text = "Food Identified is: " + str(index[pred[0]])
        print(text)
        return render_template('Predict.html', answer = text, user_img = filepath)


if __name__ == "__main__":
    app.run()
