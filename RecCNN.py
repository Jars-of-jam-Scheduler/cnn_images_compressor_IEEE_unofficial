from tensorflow.python.keras.layers import Conv2D, ReLU, BatchNormalization, Add, UpSampling2D

from ImageCodec import ImageCodec


class RecCNN:

    def __init__(self):
        decoded_image = ImageCodec.decode_for_training()  # It automatically loads the adequate image file (the compact
        # representation image)
        ImageCodec.image_name += 1  # For next image input, we increase the image's name (to counter the latency of
        # the Google Drive)
        self.upscaled_image = UpSampling2D(2)(decoded_image)

    def __set_first_block(self):
        conv2d = Conv2D(filters=64, kernel_size=3, padding="same")(self.upscaled_image)
        relu = ReLU()(conv2d)
        return relu

    @staticmethod
    def __get_atomized_second_block(previous_block):
        conv2d = Conv2D(filters=64, kernel_size=3, padding="same")(previous_block)
        batch_normalization = BatchNormalization()(conv2d)
        relu = ReLU()(batch_normalization)
        return relu

    def __set_second_block(self):
        second_block_repetitions = self.__get_atomized_second_block(self.__set_first_block())()
        for _ in range(0, 17):
            second_block_repetitions = self.__get_atomized_second_block(second_block_repetitions)
        conv2d = Conv2D(filters=64, kernel_size=3, padding="same")(second_block_repetitions)
        return conv2d

    def set_residual_block(self):
        second_block = self.__set_second_block()
        residual = Add()([second_block, self.upscaled_image])
        return residual, second_block, self.upscaled_image
