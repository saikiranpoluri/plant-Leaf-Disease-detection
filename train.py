import cv2  # working with, mainly resizing, images
import numpy as np  # dealing with arrays
import os  # dealing with directories
from random import shuffle  # mixing up or currently ordered data that might lead our network astray in training.
from tqdm import tqdm  # a nice pretty percentage bar for task

TRAIN_DIR = 'train'
TEST_DIR = 'test'
IMG_SIZE = 50
LR = 1e-3
MODEL_NAME = 'healthyvsunhealthy3-{}-{}.model'.format(LR, '2conv-basic')


def label_img(img):
    word_label = img[0]

    if word_label == 'a':
        return [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif word_label == 'b':
        return [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    elif word_label == 'c':
        return [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
    elif word_label == 'd':
        return [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    elif word_label == 'e':
        return [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    elif word_label == 'f':
        return [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
    elif word_label == 'g':
        return [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
    elif word_label == 'h':
        return [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
    elif word_label == 'i':
        return [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    elif word_label == 'j':
        return [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]


def create_train_data():
    training_data = []
    for img in tqdm(os.listdir(TRAIN_DIR)):
        label = label_img(img)
        path = os.path.join(TRAIN_DIR, img)
        # Join one or more path components intelligently. The return value is the concatenation of TRAIN_DIR and any members of img with exactly one directory separator following each non-empty part except the last, meaning that result will only end in a separator if the last part is empty.
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        # cv2.imread() method loads an image from the specified file
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        training_data.append([np.array(img), np.array(label)])
    shuffle(training_data)
    np.save('train_data.npy', training_data)
    return training_data


def process_test_data():
    testing_data = []
    for img in tqdm(os.listdir(TEST_DIR)):
        path = os.path.join(TEST_DIR, img)
        img_num = img.split('.')[0]
        # used to split the image into individual bands .....returns a tuple of individual image bands from an image...splitting to RGB
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        testing_data.append([np.array(img), img_num])

    shuffle(testing_data)
    np.save('test_data.npy', testing_data)
    return testing_data


train_data = create_train_data()
# If you have already created the dataset:
# train_data = np.load('train_data.npy')


import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import tensorflow as tf

tf.reset_default_graph()

convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 3], name='input')

convnet = conv_2d(convnet, 32, 3, activation='relu')
convnet = max_pool_2d(convnet, 3)

convnet = conv_2d(convnet, 64, 3, activation='relu')
convnet = max_pool_2d(convnet, 3)

convnet = conv_2d(convnet, 128, 3, activation='relu')
convnet = max_pool_2d(convnet, 3)

convnet = conv_2d(convnet, 32, 3, activation='relu')
convnet = max_pool_2d(convnet, 3)

convnet = conv_2d(convnet, 64, 3, activation='relu')
convnet = max_pool_2d(convnet, 3)

convnet = fully_connected(convnet, 1024, activation='relu')
convnet = dropout(convnet, 0.8)

convnet = fully_connected(convnet, 10, activation='softmax')
convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

model = tflearn.DNN(convnet, tensorboard_dir='log')

if os.path.exists('{}.meta'.format(MODEL_NAME)):
    model.load(MODEL_NAME)
    print('model loaded!')

train = train_data[:-500]
test = train_data[-500:]

X = np.array([i[0] for i in train]).reshape(-1, IMG_SIZE, IMG_SIZE, 3)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1, IMG_SIZE, IMG_SIZE, 3)
test_y = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch=8, validation_set=({'input': test_x}, {'targets': test_y}),snapshot_step=40, show_metric=True, run_id=MODEL_NAME)

model.save(MODEL_NAME)

