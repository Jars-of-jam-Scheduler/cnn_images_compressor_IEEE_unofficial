import os

from PIL import Image


class ImageCodec:

    image_name = 0

    def __init__(self):
        pass

    @staticmethod
    def encode_for_training(the_image):
        the_path = "/content/drive/My Drive/Informatique/Projets_Informatiques/Projets_Python/images_compressor" \
                   "/tmp_training_images/" + str(ImageCodec.image_name) + ".j2k "
        image = Image.fromarray(the_image)
        image.save(the_path, "JPEG2000")

    @staticmethod
    def decode_for_training():
        the_path = "/content/drive/My Drive/Informatique/Projets_Informatiques/Projets_Python/images_compressor" \
                   "/tmp_training_images/" + str(ImageCodec.image_name) + ".j2k "
        jpeg_image = Image.open(the_path)
        os.remove(the_path)
        return jpeg_image


    @staticmethod
    def encode_for_testing(the_image):
        the_path = "/content/drive/My Drive/Informatique/Projets_Informatiques/Projets_Python/images_compressor" \
                   "/tmp_testing_images/" + str(ImageCodec.image_name) + ".j2k "
        image = Image.fromarray(the_image)
        image.save(the_path, "JPEG2000")

    @staticmethod
    def decode_for_testing():
        the_path = "/content/drive/My Drive/Informatique/Projets_Informatiques/Projets_Python/images_compressor" \
                   "/tmp_testing_images/" + str(ImageCodec.image_name) + ".j2k "
        jpeg_image = Image.open(the_path)
        os.remove(the_path)
        return jpeg_image

    @staticmethod
    def save_predicted_image_for_testing(the_image):
        the_path = "/content/drive/My Drive/Informatique/Projets_Informatiques/Projets_Python/images_compressor" \
                   "/testing_predicted_images/" + str(ImageCodec.image_name) + ".bmp "
        image = Image.fromarray(the_image)
        image.save(the_path, "BMP")