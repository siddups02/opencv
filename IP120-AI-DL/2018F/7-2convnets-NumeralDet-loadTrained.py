#----------------------------------------------------------*
# program : 7-12onvnets-NumeralDet-loadTrained.py;         * 
# date    : Oct 18, 2018                                   *
# version : x0.10;                    status: tested;      * 
# ref: https://github.com/fchollet/deep-learning-with-python-notebooks/blob/96d58b5727fcf76106f929f5ce24c40fc9b46d75
#                                                          *
# purpose : demo of loading trained mnist net              *  
#----------------------------------------------------------*
import keras
keras.__version__

#----------load trained model--------------------*
from keras import layers
from keras import models

from keras.models import load_model  
model = load_model('harryTest.h5')
model.summary() #check the model 

#-----------get NIST image data-------------------*
from keras.datasets import mnist
from keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28, 28, 1))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

#-------------train----------------------*
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5, batch_size=64)

test_loss, test_acc = model.evaluate(test_images, test_labels)
test_acc

#-------------save trained model---------* 
import h5py 
model.save('harryTest.h5')
#-end 


