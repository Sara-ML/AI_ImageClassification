# AI_ImageClassification
ㅇ Image Classification through the Transfer Learning
  - Inception V3 model, one of the efficient classification model is used for the image classification between the real and fake images.
- The model is also pretrained for Imagenet that can differentiate 1000 different classes. The program applies the Transfer learning to this existing model and re-trains it to classify a new set of images.

ㅇMachince Learning : Neural Network with Transfer Learning
ㅇModel : Inception model 
Transfer learning utilizes a pre-trained neural network to gain knowledge of the layers
Inception V3 layer has two part:
  •	Feature extraction part with a Convolution neural network.
  •	Classification part with fully-connected and softmax layers.
ㅇHow it works:
  - In order to identify multiple faces in the photo, the distortion method is used that crops the faces and get rid of any angle differences.
  - The bottleneck features are extracted with the labelled real and fake images.
  - Both the images are trained through the Convolution neural network.
  - The output layer consists of the softmax that holds the probability value for classification.
ㅇHow it is done:
  -The dataset needs to be created in the root of the project folder. This folder will contain the image data sets for all the subjects, for whom the classification is to be performed.
  - The structure of the data should be as follows, 

![alt text](AI_ImageClassification/img.PNG)
The folder name act as the label of the images, which is trained along with the images.

The classification is done with respect to the real images. and therefore, the probabilities represent the real images

Similarly, for the challenge 2, the classification is done with respect to the real images.

