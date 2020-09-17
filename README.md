
## Get the code


```bash
git clone https://github.com/charlesxwang/Image_Classifier.git
cd Image_Classifier
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
Charles Wang. (2019). Random satellite images of buildings (Version v1.0) [Data set]. Zenodo. http://doi.org/10.5281/zenodo.3521067
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

