
## Get the code


```bash
git clone https://github.com/charlesxwang/Image_Classifier.git
cd Image_Classifier
pip install -r requirements.txt
```

## Train a model

```bash
python train.py --img_dir <IMAGE_DIRECTORY> --model_dir <MODEL_DIRECTORY>
```

IMAGE_DIRECTORY is the directory where you have your images for training


```
    IMAGE_DIRECTORY
    │── class_1
    │       └── *.png
    │── class_2
    |      └── *.png
    │── ...
    |
    └── class_n
           └── *.png
```

An image dataset for test that contains images of different rooves can be downloaded here:
```
https://zenodo.org/record/3986721/files/Roof_Satellite_Images.zip
```

MODEL_DIRECTORY is the directory where the trained model will be saved. 

It is better to run the above code on a GPU machine.







## Predict


Now you can use the trained model to predict on given images.

```
python predict.py --image_dir <IMAGE_DIRECTORY> --model_dir <MODEL_DIRECTORY>
```

IMAGE_DIRECTORY is the directory of your images. 

MODEL_DIRECTORY is the folder where you have your trained model saved.

