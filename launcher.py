import numpy as np
import tensorflow
from keras.optimizers import Adam
from tensorflow.python.keras import Model
from tensorflow.python.keras.backend import mean, square

from ComCNN import ComCNN
from ImageCodec import ImageCodec
from RecCNN import RecCNN
from Scaler import Scaler
from Util import Util

np.random.seed(10)


# <!--- THE OPTIMIZER --->
the_optimizer = Adam()
# <!--- /THE OPTIMIZER --->


# <!--- COST FUNCTION --->
def com_cnn_cost_function(rec_predicted_without_encoder, original_image):
    com_cnn_loss = mean(square(rec_predicted_without_encoder - original_image))
    return com_cnn_loss

def rec_cnn_cost_function(rec_predicted_with_encoder, original_image):
    rec_cnn_loss = mean(square(rec_predicted_with_encoder - original_image))
    return rec_cnn_loss
# <!--- /COST FUNCTION --->


# <!--- MODELS -->
def define_rec_model(rec_cnn):
    returned_tuple = rec_cnn.set_residual_block()
    model_rec_cnn = Model(rec_cnn.upscaled_image, returned_tuple)
    model_rec_cnn.compile(
        loss=[rec_cnn_cost_function],
        optimizer=the_optimizer
    )
    return model_rec_cnn

def define_com_cnn_model(com_cnn):
    com_cnn.encode_the_compact_representation_of_the_original_image()
    model_com_cnn = Model(com_cnn.input_layer, com_cnn.set_third_block())
    model_com_cnn.compile(
        loss=[com_cnn_cost_function],
        optimizer=the_optimizer
    )
    return model_com_cnn

rec_cnn = RecCNN()
com_cnn = ComCNN(Scaler.original_image_size)
com_cnn_model = define_com_cnn_model(com_cnn)
rec_cnn_model = define_rec_model(rec_cnn)
# <!--- /MODELS -->

# <!--- TRAINING -->
def get_decoded_compact_representation(training_image):
    compact_representation = com_cnn_model.predict(training_image)
    ImageCodec.encode_for_training(compact_representation)
    decoded_compact_representation = ImageCodec.decode_for_training()
    return decoded_compact_representation

def train_rec_cnn(number_of_batches, images):
    decoded_compact_representations = []
    rec_cnn_model.trainable = True
    com_cnn_model.trainable = False
    for current_batch_number in range(0, number_of_batches):
        decoded_compact_representation = get_decoded_compact_representation(images[current_batch_number])
        decoded_compact_representations.append(decoded_compact_representation)
    rec_cnn_model.train_on_batch(decoded_compact_representations, images)

def train_com_cnn(number_of_batches, images):
    rec_cnn_model.trainable = False
    com_cnn_model.trainable = True
    for current_batch_number in range(0, number_of_batches):
        com_cnn_model.train_on_batch(images[current_batch_number], images[current_batch_number])

def train(number_of_epochs, batch_size):
    test()
    print("TRAINING")
    images = Util.fetch_training_image()
    number_of_batches = len(images) // batch_size
    for epoch in range(0, number_of_epochs):
        print('-' * 15, 'Epoch %d' % epoch, '-' * 15)
        train_rec_cnn(number_of_batches, images)
        train_com_cnn(number_of_batches, images)
        if(epoch % 1 == 0):
            test()
    print("/TRAINING")
# <!--- /TRAINING -->


# <!--- TESTING -->
def test():
    print("TESTING")
    predicted_images = []
    images = Util.fetch_testing_image()
    for idx in range(0, len(images)):
        original_image = images[idx]
        compact_representation_of_the_tested_image = com_cnn_model.predict(original_image)
        ImageCodec.encode_for_testing(compact_representation_of_the_tested_image)
        decoded = ImageCodec.decode_for_testing()
        reconstructed = rec_cnn_model.predict(decoded)
        ImageCodec.save_predicted_image_for_testing(reconstructed)
        predicted_images.append(reconstructed)
    print("/TESTING")
# <!--- /TESTING -->


# <!--- ENTRY POINT -->
train(50, 128)
# <!--- /ENTRY POINT -->
