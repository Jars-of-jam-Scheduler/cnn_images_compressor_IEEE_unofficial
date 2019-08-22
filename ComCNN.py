from tensorflow.python.keras import Input
from tensorflow.python.keras.layers import Conv2D, ReLU, BatchNormalization

from ImageCodec import ImageCodec


class ComCNN:

    def __init__(self, the_shape):
        self.the_shape = the_shape
        self.input_layer = Input(the_shape)

    def __set_first_block(self):
        conv2d = Conv2D(filters=64, kernel_size=3, padding="same")(self.input_layer())
        relu = ReLU()(conv2d)
        return relu

    def __set_second_block(self):
        conv2d = Conv2D(filters=64, kernel_size=3, strides=2, padding="same")(self.__set_first_block())
        batch_normalization = BatchNormalization()(conv2d)
        relu = ReLU()(batch_normalization)
        return relu

    def __set_third_block(self):
        conv2d = Conv2D(filters=64, kernel_size=3, padding="same")(self.__set_second_block())
        return conv2d

    def encode_the_compact_representation_of_the_original_image(self):
        image_codec = ImageCodec.encode(self.__set_third_block())
        return image_codec
