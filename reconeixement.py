import pygame
import tensorflow as tf
from tensorflow.python import keras
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle
#import pkg_resources.py2_warn
from keras import layers
from keras import models
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
pygame.init()
pygame.font.init()
block_size = 10
s_width = 600
s_height = 600



def main_menu(win):
    actualdir=os.getcwd()
    X=[]
    Y=[]
    training_data=[]
    pantalla=2
    Size=100#plt.imshow(new_array, cmap="gray")
            #plt.show()
    peça="/I"
    mode="/train"
    win.fill((255, 255, 255))
    pygame.display.update()
    pulsat=0
    run=True
    Datadir="/Users\Pol51\Desktop\deep"+mode
    Categories=["S", "Z", "I", "O", "J", "L", "T"]
    if pantalla==3:
        for category in Categories:
            path=os.path.join(Datadir, category)
            os.chdir(path)
            for i in os.listdir():
                img = cv2.imread(i)
                (h, w) = img.shape[:2]
                center = (w / 2, h / 2)
                for j in range(3):
                    rand= 90*(j+1)
                    M = cv2.getRotationMatrix2D(center, rand, 1.0)
                    foto = cv2.warpAffine(img, M, (h, w))
                    nom=len(os.listdir())+1
                    cv2.imwrite(str(nom)+".png", foto)
    if pantalla==1:
        Datadir = "/Users\Pol51\Desktop\deep/train"
        for category in Categories:
            path=os.path.join(Datadir, category)
            class_num=Categories.index(category)
            for img in os.listdir(path):
                try:
                    img_array=cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                    new_array=cv2.resize(img_array,(Size,Size))
                    training_data.append([new_array,class_num])
                except Exception as e:
                    print(e)
                    pass
        random.shuffle(training_data)
        for features, label in training_data:
            X.append(features)
            Y.append(label)
        #print(X)
        #print(Y)
        X=np.array(X).reshape(-1,Size,Size,1)
        pickle_out=open("X.pickle","wb")
        pickle.dump(X, pickle_out)
        pickle_out.close()
        pickle_out = open("Y.pickle", "wb")
        pickle.dump(Y, pickle_out)
        pickle_out.close()
        X = []
        Y = []
        training_data = []
        Datadir = "/Users\Pol51\Desktop\deep/test"

        for category in Categories:
            path=os.path.join(Datadir, category)
            class_num=Categories.index(category)
            for img in os.listdir(path):
                try:
                    img_array=cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                    new_array=cv2.resize(img_array,(Size,Size))
                    training_data.append([new_array,class_num])
                except Exception as e:
                    print(e)
                    pass
        random.shuffle(training_data)
        for features, label in training_data:
            X.append(features)
            Y.append(label)
        X=np.array(X).reshape(-1,Size,Size,1)
        pickle_out=open("X_test.pickle","wb")
        pickle.dump(X, pickle_out)
        pickle_out.close()
        pickle_out = open("Y_test.pickle", "wb")
        pickle.dump(Y, pickle_out)
        pickle_out.close()

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
                    if pantalla==0:
                       os.chdir(Datadir + peça)
                       name=len(os.listdir())+1000
                       pygame.image.save(win, str(name)+".png")
                       win.fill((255, 255, 255))
                       pygame.display.update()
                       print(name)
                    if pantalla ==2:
                        os.chdir(actualdir)
                        P=pickle.load(open("X.pickle","rb"))
                        O=pickle.load(open("Y.pickle","rb"))
                        L = pickle.load(open("X_test.pickle", "rb"))
                        R = pickle.load(open("Y_test.pickle", "rb"))
                        P=P/255.0
                        L=L/255.0
                        #hola = len(P) * 10 // 12
                        train_images=P##[:-400]
                        test_images =L
                        train_labels =O##[:-400]
                        test_labels =R
                        ##val_images=P[-400:]
                        ##val_labels=O[-400:]
                        #train_images=P[:hola]
                        #test_images=P[hola:]
                        hey = np.array(test_images).reshape(-1, Size, Size)
                        #train_labels = O[:hola]
                        #test_labels = O[hola:]
                        class_names = ["S", "Z", "I", "O", "J", "L", "T"]#trerure
                        model=models.Sequential()
                        """model.add(layers.Conv2D(32, kernel_size=(5, 5), strides=(1, 1), activation='relu', input_shape=(Size,Size,1)))
                        model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
                        model.add(layers.Conv2D(64, (5, 5), activation='relu'))
                        model.add(layers.MaxPooling2D(pool_size=(2, 2)))"""
                        model.add(layers.Conv2D(32,(3,3),activation='relu', input_shape=(Size,Size,1)))
                        model.add(layers.MaxPooling2D((2,2)))
                        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
                        model.add(layers.MaxPooling2D((2, 2)))
                        model.add(layers.Conv2D(128, (3, 3), activation='relu'))
                        model.add(layers.MaxPooling2D((2, 2)))
                        model.add(layers.Conv2D(128, (3, 3), activation='relu'))
                        model.add(layers.MaxPooling2D((2, 2)))
                        """model.add(layers.Conv2D(128, (5, 5), activation='relu'))
                        model.add(layers.MaxPooling2D((2, 2)))
                        model.add(layers.Conv2D(256, (3, 3), activation='relu'))
                        model.add(layers.MaxPooling2D((2, 2)))"""
                        model.add(layers.Flatten())
                        #model.add(layers.Dropout(0.5))
                        model.add(layers.Dense(256, activation='relu'))#512
                        model.add(layers.Dense(512, activation='relu'))
                        """model.add(layers.Dense(1024, activation='relu'))
                        model.add(layers.Dense(1024, activation='relu'))"""
                        model.add(layers.Dense(7, activation='softmax'))
                        model.compile(optimizer="adam",# adam/rmsprop   keras.optimizers.SGD(lr = 0.01)-canviar de versio
                                      loss='sparse_categorical_crossentropy',#,keras.losses.categorical_crossentropy
                                      metrics=['acc'])
                        history=model.fit(train_images,
                                          train_labels,
                                          batch_size=64,
                                          epochs=15,
                                          #verbose=1,
                                          validation_data=(test_images, test_labels)##val_images,val_labels)
                                          #callbacks=[histrory]
                                          )
                        model.summary()
                        model.save('bobo444.h5')
                        history_dict=history.history
                        loss_values=history_dict['loss']
                        val_loss_values=history_dict['val_loss']
                        acc=history.history['acc']
                        val_acc = history.history['val_acc']
                        epochs=range(1,len(acc)+1)
                        plt.plot(epochs,acc,'bo',label='model acc')
                        plt.plot(epochs, val_acc, 'b', label='test acc')
                        plt.xlabel('Epochs')
                        plt.ylabel('Loss')
                        plt.legend()
                        plt.show()
                        di="/Users\Pol51\Desktop\predic"
                        os.chdir(di)
                        #model=keras.models.load_model('definitiubo5.h5')

                        test_lose, test_acc = model.evaluate(test_images, test_labels)#, batch_size=128
                        print(test_acc)
                        pygame.image.save(win, "hola.png")
                        predict_array = cv2.imread(os.path.join(di, "hola.png"), cv2.IMREAD_GRAYSCALE)
                        predict_arrays = cv2.resize(predict_array, (Size, Size))
                        predict_arrays = np.array(predict_arrays).reshape(-1, Size, Size, 1)
                        predict=model.predict(predict_arrays)
                        plt.grid(False)
                        plt.xlabel(class_names[np.argmax(predict)])
                        plt.show()
        if pulsat == 1:
            mx, my = pygame.mouse.get_pos()
            pygame.draw.rect(win, (0, 0, 0), (mx-block_size/2, my-block_size/2, block_size, block_size), 0)
            pygame.display.update()
        if pulsat==2:
            mx, my = pygame.mouse.get_pos()
            pygame.draw.rect(win, (255, 255, 255), (mx-block_size*3/2, my-block_size*3/2, block_size*3, block_size*3), 0)
            pygame.display.update()


win=pygame.display.set_mode((s_width, s_height))

pygame.display.set_caption("Autoaprenentatge")
main_menu(win)

"""
                       model = keras.Sequential([
                           keras.layers.Flatten(input_shape=(100, 100)),
                           keras.layers.Dense(128, activation='relu'),
                           keras.layers.Dense(128, activation='relu'),
                           keras.layers.Dense(7, activation='softmax')
                       ])

                       model.compile(optimizer='adam',
                                     loss='sparse_categorical_crossentropy',
                                     metrics=['accuracy'])
                       model.fit(train_images, train_labels, epochs=10)
                       test_lose,test_acc=model.evaluate(test_images,test_labels)"""

"""prediction=model.predict(test_images)
                        print(prediction)
                        for i in range(len(prediction)):
                            plt.grid(False)
                            #plt.imshow(test_images[i], cmap=plt.cm.binary)
                            plt.imshow(hey[i], cmap=plt.cm.binary)
                            plt.xlabel("actual:"+ class_names[test_labels[i]])
                            plt.title(class_names[np.argmax(prediction[i])])
                            plt.show()"""


#havia d'haver duplicat despres

#