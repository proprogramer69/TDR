import pygame
#import pywrap_tensorflow
import tensorflow as tf
from tensorflow import keras

#import pkg_resources.py2_warn
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle
#from keras import layers
#from keras import models
#from keras import optimizers
#from keras.preprocessing.image import ImageDataGenerator
import matplotlib.image as mpimg

print(keras)
pygame.init()
pygame.font.init()
block_size = 10
s_width = 600
s_height = 600

def main_menu(win):
    #model = models.load_model('bobo4.h5')#'bobo4.h5')#tf.keras.models.load_model('definitiubo.h5')
    model=tf.keras.models.load_model('bobo444.h5')
    model.summary()

    actualdir=os.getcwd()
    Size=100#plt.imshow(new_array, cmap="gray")
            #plt.show()
    peça="/S"
    mode="/test"
    win.fill((255, 255, 255))
    pygame.display.update()
    pulsat=0
    run=True
    Datadir="/Users\Pol51\Desktop\deep"+mode
    Categories=["S", "Z", "I", "O", "J", "L", "T"]
    os.chdir("img")
    while run:
        for event in pygame.event.get():
            if event.type ==pygame.MOUSEBUTTONDOWN:
                pulsat=1
            if event.type ==pygame.MOUSEBUTTONUP:
                pulsat=0
            if event.type == pygame.QUIT:
                 run=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pulsat=2
                else:
                    pulsat=0
                if event.key == pygame.K_SPACE:
                        #os.chdir(actualdir)
                        #class_names = ["S", "Z", "I", "O", "J", "L", "T"]
                        #di="/Users\Pol51\Desktop\predic"
                        #os.chdir(di)
                        #test_lose, test_acc = model.evaluate(test_images, test_labels, batch_size=128)
                        #print(test_acc)
                        pygame.image.save(win, "hola.png")
                        predict_array = cv2.imread("hola.png", cv2.IMREAD_GRAYSCALE)
                        predict_arrays = cv2.resize(predict_array, (Size, Size))
                        predict_arrays = np.array(predict_arrays).reshape(-1, Size, Size, 1)
                        predict=model.predict(predict_arrays)
                        plt.grid(False)
                        print(predict)

                        print(os.listdir()[np.argmax(predict)])
                        plt.imshow(mpimg.imread(os.listdir()[np.argmax(predict)]))
                        #plt.xlabel(class_names[np.argmax(predict)])
                        plt.show()
                        win.fill((255, 255, 255))
                        pygame.display.update()
        if pulsat == 1:
            mx, my = pygame.mouse.get_pos()
            pygame.draw.rect(win, (0, 0, 0), (mx, my, block_size, block_size), 0)
            pygame.display.update()
        if pulsat==2:
            mx, my = pygame.mouse.get_pos()
            pygame.draw.rect(win, (255, 255, 255), (mx, my, block_size*3, block_size*3), 0)
            pygame.display.update()


win=pygame.display.set_mode((s_width, s_height))

pygame.display.set_caption("Autoaprenentatge")
main_menu(win)





"""import pygame
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle
import pkg_resources.py2_warn
from keras import layers
from keras import models
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras_preprocessing import image
train_dir="/Users\Pol51\Desktop\deep"
train_dir_O="/Users\Pol51\Desktop\deep/2"
train_datagen=ImageDataGenerator(
    rescale=1./255,
    rotation_range=180,
    zoom_range=0.2
    )
test_datagen=ImageDataGenerator(rescale=1./255)
train_generator=train_datagen.flow_from_directory(
    train_dir,
    target_size=(100,100),
    batch_size=20,
    class_mode='categorical'
)
fnames= [os.path.join(train_dir_O,fname)for fname in os.listdir(train_dir_O)]
img_path=fnames[0]
img=image.load_img("/Users\Pol51\Desktop\deep/2/jardi.jpg", target_size=(100,100))
x=image.img_to_array(img)
x=x.reshape((1,) + x.shape)
i=0
for batch in datagen.flow(x,batch_size=1):
    plt.figure(i)
    imgplot=plt.imshow(image.array_to_img(batch[0]))
    i+=1
    if i%4==0:
        break
plt.show()"""