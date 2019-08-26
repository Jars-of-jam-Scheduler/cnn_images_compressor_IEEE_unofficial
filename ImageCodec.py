<<<<<<< HEAD
import os

from PIL import Image


class ImageCodec:

    image_name = 0

=======
class ImageCodec:

>>>>>>> 8e1373364d4e0fd4ca5cc4d935d319980aba3473
    def __init__(self):
        pass

    @staticmethod
    def encode(the_image):
<<<<<<< HEAD
        the_path = "/content/drive/My Drive/Informatique/Projets_Informatiques/Projets_Python/images_compressor" \
                   "/tmp_images/" + str(ImageCodec.image_name) + ".j2k "
        image = Image.fromarray(the_image)
        image.save(the_path, "JPEG2000")

    @staticmethod
    def decode():
        the_path = "/content/drive/My Drive/Informatique/Projets_Informatiques/Projets_Python/images_compressor" \
                   "/tmp_images/" + str(ImageCodec.image_name) + ".j2k "
        jpeg_image = Image.open(the_path)
        os.remove(the_path)
        return jpeg_image
=======
        rgb_im = the_image.convert('RGB')
        return rgb_im.save('test.jpg', 'JPEG2000', quality=50)

    @staticmethod
    def decode(the_image):
        return 'test.jpeg2000' + the_image
>>>>>>> 8e1373364d4e0fd4ca5cc4d935d319980aba3473
