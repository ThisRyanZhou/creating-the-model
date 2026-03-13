# Training

Trains the CV model on the given dataset of handwritten letters.

Part of [ChickenScratch](https://github.com/kennething/chickenscratch).

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

Running the program.
Right now this code is edited for a pc with 32gb ram and a RTX 5070. It will take approximately 1 hour to run as well. If you are at anything lower please change the train.py file so we dont break your ram or your graphics card.
There are 3 main settings to change:
epochs=500,
imgsz=1024,
batch=8,
Normal computer (16gb ram, no graphics/built in graphics) should be able to able to run fine at
epochs=50;
imgsz=256;
batch=2;
Slightly higher would be 
epochs=100;
imgsz=512;
batch=3;
The better the settings the more accurate the model will end up being the best way to check accuracy is dependent on the _loss it should be really low under 0.2 for a fully accurate model. The setting that we ran all the way at the top ended with a 0.3 which is fine for our use case.
The place you would find the result would be in \runs\detect\train\weights. There are two files best.pt and last.pt where last is the one that is trained the most while best is the one that scored the highest on accuracy.

Adding more training data.
This will be split into two section setting up labelImg and using labelImg

setting up:
I will be showing one way to do this but as long as your python version is exactly 3.8 (fuckin labelImg dev get better) and you have labelImg downloaded you should be able to skip this part.
download anaconda though any trusted site mine will be based on this https://www.anaconda.com/download
once you have anaconda downloaded set it as your default python interpreter and your default terminal prompt either do it while its downloading or do it manually.
To do it manually:
windows: go to settings then apps then Default apps, set the current default app to your exe C:\Users\YourName\anaconda3\python.exe
macos: (please stop using a mac it hurts my soul and for punishment yall need to find your own guide) just run conda init and it should work fine you might want to open a venv source path-to-conda/bin/activate
Once your down downloading anaconda please activate a virtual enviroment with python 3.8 
conda create -n labelimg python=3.8 -y
acivate the venv
conda activate labelimg
then download labelImg
conda install -c conda-forge labelimg
once all this is downloaded you should be able to type labelimg and it should run

using labelImg
I recomend creating a file with all of your raw photos so you can edit them all at once with labelImg.
Once your in labelImg just open a file and select the file with all your raw images. On the right there should be a button that allow you to choose the version to save as change that version to YOLO. 
To label the images click w select the image and give it a name. Do this with all of your images.
Now you should click save and it should save one copy of each image. One as a png and one as a txt. You will need to move the png to the images tab and the txt to the labels tab. Then choose which images you would like the model to be trained on and which images you would like the model to be validated/tested on. Move the png to the respective tab and the counterpart txt file to the same tab in the labels directory. You should create a 80/20 split with 80% going into training and 20% going into validating. Next you will need to edit the class.txt. You should see an extra file in your raw that is called class.txt copy all information inside it (do it however you like i normally cat class.txt and shift control c whatever comes out) and then add it to the class.txt file already in the dataset_root/labels/train.

once this is done you should be able to run the train.py once you exit anaconda using conda deactivate.
