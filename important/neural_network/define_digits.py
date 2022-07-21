import os
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import numpy as np

mnist = tf.keras.datasets.mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Printing the shapes
print("train_images shape: ", train_images.shape)
print("train_labels shape: ", train_labels.shape)
print("test_images shape: ", test_images.shape)
print("test_labels shape: ", test_labels.shape)

fig = plt.figure(figsize=(10, 10))

nrows = 3
ncols = 3

for i in range(9):
    fig.add_subplot(nrows, ncols, i+1)
    plt.imshow(train_images[i])
    plt.title(f"Digit: {train_labels[i]}")
    plt.axis(False)

plt.show()

train_images = train_images / 255
test_images = test_images / 255

train_labels = tf.keras.utils.to_categorical(train_labels)
test_labels = tf.keras.utils.to_categorical(test_labels)

# model = tf.keras.Sequential([
#     tf.keras.layers.Flatten(),
#     tf.keras.layers.Dense(units=512, activation='relu'),
#     tf.keras.layers.Dense(units=10, activation='softmax')
# ])
#
# model.compile(
#     loss='categorical_crossentropy',
#     optimizer='adam',
#     metrics=['accuracy']
# )
#
# history = model.fit(
#     x=train_images,
#     y=train_labels,
#     epochs=10
# )
# model.save("digits.model")

# plt.plot(history.history['loss'])
# plt.xlabel('epochs')
# plt.legend(['loss'])
# plt.show()
#
# plt.plot(history.history['accuracy'], color='orange')
# plt.xlabel('epochs')
# plt.legend(['accuracy'])
# plt.show()

# test_loss, test_accuracy = model.evaluate(
#     x=test_images,
#     y=test_labels
# )
#
# print("Test Loss: %.4f" % test_loss)
# print("Test Accuracy: %.4f" % test_accuracy)

model = tf.keras.models.load_model('digits.model')

for index in range(len([f for f in os.listdir("digits")])):
    try:
        img = cv2.imread(f"digits/digit{index}.png")[:, :, 0]
        img = np.invert(np.array([img]))
        predict = model.predict(img)
        print("In image is displayed number -> ", np.argmax(predict))
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
    except Exception as ex:
        print("Error!")

