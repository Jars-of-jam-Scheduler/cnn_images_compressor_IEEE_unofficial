class ImageCodec:

    def __init__(self):
        pass

    @staticmethod
    def encode(the_image):
        rgb_im = the_image.convert('RGB')
        return rgb_im.save('test.jpg', 'JPEG2000', quality=50)

    @staticmethod
    def decode(the_image):
        return 'test.jpeg2000' + the_image
