
import argparse
import os
import tensorflow as tf
import numpy as np
from glob import glob
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

parser = argparse.ArgumentParser(description='Train a classifier')

parser.add_argument('--image_dir',help='The path of a folder containing images',type=str)
parser.add_argument('--image_list',help='A list of image paths', nargs='+')

parser.add_argument('--model_dir',help='The path of a folder where the model (h5) resides',type=str,required=True)
parser.add_argument('--model_file',default='classifier.h5',help='The name of the model file (*.h5)',type=str)

parser.add_argument('--class_names',help='List of class names', nargs='+')

args = parser.parse_args()

img_dir = args.image_dir
img_list = args.image_list
model_dir = args.model_dir
model_file = args.model_file
class_names = args.class_names

if img_list is None:
    if img_dir is None:
        print("You need to provide --image_dir or --image_list")
        exit()
    else:
        img_list = []
        img_list += glob(os.path.join(img_dir, "*.png"))
        img_list += glob(os.path.join(img_dir, "*.jpg"))
        img_list += glob(os.path.join(img_dir, "*.jpeg"))

print(os.path.join(model_dir, model_file))
model = load_model(os.path.join(model_dir, model_file))


predictions = []
for img_path in img_list:
  img = image.load_img(img_path, target_size=(256, 256))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  prediction = model.predict(x)
  prediction = np.argmax(prediction[0])
  predictions.append(prediction)
  #class_names[prediction]

if class_names:
    for i,p in enumerate(predictions):
        predictions[i] = class_names[p]

for img, pred in zip(img_list, predictions): 
    print ("Image :  %s     Class : %s" %(img, pred)) 
