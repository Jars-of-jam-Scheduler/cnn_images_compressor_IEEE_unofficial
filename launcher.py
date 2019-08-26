import numpy as np
import tensorflow
from keras.optimizers import Adam
from tensorflow.python.keras import Model
from tensorflow.python.keras.backend import mean, square

from ComCNN import ComCNN
from RecCNN import RecCNN
from Scaler import Scaler

np.random.seed(10)

# <!--- THE OPTIMIZER --->
the_optimizer = Adam()
# <!--- /THE OPTIMIZER --->


# <!--- COST FUNCTION --->
def the_cost_function(final_image, residual_image, upscaled_image, original_image):
    com_cnn_loss = mean(square(final_image - original_image))
    rec_cnn_loss = mean(square(residual_image - (upscaled_image - original_image)))
    return com_cnn_loss + rec_cnn_loss


tensorflow.keras.losses.the_cost_function = the_cost_function  # For TensorFlow CLI "tflite_convert"
# <!--- /COST FUNCTION --->


# <!--- TRAINING -->
def train(number_of_epochs, batch_size):
<<<<<<< HEAD
    com_cnn = ComCNN(Scaler.original_image_size)  # Loading in RAM the networks
    com_cnn.encode_the_compact_representation_of_the_original_image()  # An image file is written, containing the CROI
    rec_cnn = RecCNN()  # Loads the CROI, which will be used by the RecCNN
=======
    com_cnn = ComCNN(Scaler.original_image_size)
    com_cnn_third_block = com_cnn.encode_the_compact_representation_of_the_original_image()

    rec_cnn = RecCNN(com_cnn_third_block)
>>>>>>> 8e1373364d4e0fd4ca5cc4d935d319980aba3473
    returned_tuple = rec_cnn.set_residual_block()

    model = Model(com_cnn.input_layer, returned_tuple[0])
    model.compile(
        loss=[the_cost_function],
        optimizer=the_optimizer
    )
    model.trainable = True

    batch_count = int(images.shape[0] / batch_size)
    for epoch in range(0, number_of_epochs):
        print('-' * 15, 'Epoch %d' % epoch, '-' * 15)
        for _ in range(0, batch_count):
            loss = model.train_on_batch(batch_)
# <!--- /TRAINING -->


# <!--- ENTRY POINT -->
train(50, 128)
# <!--- /ENTRY POINT -->
