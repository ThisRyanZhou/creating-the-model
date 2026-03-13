# Training

Trains the CV model on the given dataset of handwritten letters.

Part of [ChickenScratch](https://github.com/kennething/chickenscratch).

## Creating Training Data

First:

1. Create a dataset of handwritten letters.
2. Scan the handwritten letters using a document scanner, like CamScanner.
3. Crop each letter into its own square image.
4. Use LabelImg, a tool that allows you to label your images for training the
   model.

### Setting Up LabelImg

If you already have LabelImg set up, you can skip this section.

1. Ensure your Python version is exactly 3.8, as LabelImg does not work with
   other versions of Python.
2. Download Anaconda from [here](https://www.anaconda.com/download) and set it
   as your default Python interpreter.

   For help downloading and setting up Anaconda, refer to their
   [install instructions](https://www.anaconda.com/docs/getting-started/anaconda/install#basic-install-instructions).

3. Activate a virtual environment with Python 3.8:

   ```sh
   conda create -n labelimg python=3.8 -y
   conda activate labelimg
   conda install -c conda-forge labelimg
   ```

4. Once all of this is downloaded, you should be able to run `labelimg` in your
   terminal.

### Using LabelImg

1. Create a folder for all of your raw images that you want to label.
2. Open LabelImg and select the folder with your raw images.
3. On the right, there should be a button that allows you to choose the version
   to save as. Change that version to YOLO.
4. To label the images, click and select the image and give it a name. Do this
   with all of your images.

   Once you are done labeling, click the save button. This will save a copy of
   each image as a `png` and a `txt` file. The `png` file is the image itself, while
   the `txt` file contains the labels for that image.

5. Move the `png` files to the `images` tab and the `txt` files to the `labels`
   tab.
6. Next, choose which images the model should be trained on, and which images
   the model should be validated/tested on. Move the `png` files to the
   respective tab and their counterpart `txt` files to the same tab in the
   `labels` directory.

   You should create an 80/20 split with 80% of the images+labels going into
   training, and 20% into validating.

7. You should see an extra file in your raw, called `class.txt`.

   Copy all information inside it and add it to the `class.txt` file already in
   the `dataset_root/labels/train` directory.

8. Deactivite Anaconda with `conda deactivate` once you're done.

## Setup Instructions

1. Ensure Python and pip are installed on your machine.

2. Select this directory:

   ```sh
   cd training
   ```

3. Install dependencies:

   ```sh
   python -m venv venv
   source venv/bin/activate # on windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Training the Model

Create a `.env` file in the same directory as `train.py` and add the following
values:

```sh
EPOCHS=500 # number of times the training is run for
IMAGE_SIZE=1024 # resolution of image, >= 256 is recommended for better results
BATCH=8 # number of images processed at once
```

The values above are set up to run on a computer with an RTX 5070 and 32gb of
RAM. With these specs and options, we were able to train the model in
approximately one hour.

However, you likely have different specs, so you may need to adjust some of
these options so your computer doesn't spontaneously combust.

> \[!NOTE\]
> With 16gb of RAM and no graphics/built-in graphics, we recommend:

> ```sh
> EPOCHS=50
> IMAGE_SIZE=256
> BATCH=2
> ```

> With better specs, you can increase these values to get a more accurate
> model, like:

> ```sh
> EPOCHS=100
> IMAGE_SIZE=512
> BATCH=3
> ```

> The higher the values, the more accurate the model will be.

The best way to check the accuracy of the model is to look at the `_loss`
value. An accurate model should have a loss value under `0.2`, but for our use
case, we were able to get away with a loss of `0.3`.

After training, you should see two new files in `/runs/detect/train/weights`
called `best.pt` and `last.pt`. `last.pt` is the model that was trained the
most, while `best.pt` is the model that scored the highest on accuracy.
