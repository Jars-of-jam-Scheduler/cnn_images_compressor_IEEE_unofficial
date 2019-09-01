import os

from numpy.ma import array
from skimage import data


class Util:

    def __init__(self):
        pass

    @staticmethod
    def __load_data_from_dirs(dirs, ext):
        files = []
        file_names = []
        count = 0
        for d in dirs:
            for f in os.listdir(d):
                if f.endswith(ext):
                    image = data.imread(os.path.join(d, f))
                    if len(image.shape) > 2:
                        files.append(image)
                        file_names.append(os.path.join(d, f))
                    count = count + 1
        return files

    @staticmethod
    def __load_path(path):
        directories = []
        if os.path.isdir(path):
            directories.append(path)
        for elem in os.listdir(path):
            if os.path.isdir(os.path.join(path, elem)):
                directories = directories + Util.__load_path(os.path.join(path, elem))
                directories.append(os.path.join(path, elem))
        return directories

    @staticmethod
    def __load_data(directory, ext):
        files = Util.__load_data_from_dirs(Util.__load_path(directory), ext)
        return files

    @staticmethod
    def fetch_training_image():
        print("Loading training images...")
        training_images_wrapper = []
        training_images = Util.__load_data(
            "/content/drive/My Drive/Informatique/Projets_Informatiques/Projets_Python/images_compressor/training",
            ".jpg")
        for img in range(len(training_images)):
            training_images_wrapper.append(training_images[img])
        training_images_wrapper_wrapper = array(training_images_wrapper)
        print("/Loading training images...")
        return training_images_wrapper_wrapper

    @staticmethod
    def fetch_testing_image():
        print("Loading testing images...")
        testing_images_wrapper = []
        testing_images = Util.__load_data(
            "/content/drive/My Drive/Informatique/Projets_Informatiques/Projets_Python/images_compressor/testing",
            ".jpg")
        for img in range(len(testing_images)):
            testing_images_wrapper.append(testing_images[img])
        testing_images_wrapper_wrapper = array(testing_images_wrapper)
        print("/Loading testing images...")
        return testing_images_wrapper_wrapper