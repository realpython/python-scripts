import fnmatch
import os

# pip install Wand
from wand.image import Image
# pip install http://pypi.python.org/packages/source/h/hurry.filesize/hurry.filesize-0.9.tar.gz
from hurry.filesize import size


# constants
PATH = '/../../../..'
PATTERN = '*.jpg'


def get_image_file_names(filepath, pattern):
    matches = []
    if os.path.exists(filepath):
        for root, dirnames, filenames in os.walk(filepath):
            for filename in fnmatch.filter(filenames, pattern):
                matches.append(os.path.join(root, filename))  # full path
        if matches:
            print("Found {} files, with a total file size of {}.".format(
                len(matches), get_total_size(matches)))
            return matches
        else:
            print("No files found.")
    else:
        print("Sorry that path does not exist. Try again.")


def get_total_size(list_of_image_names):
    total_size = 0
    for image_name in list_of_image_names:
        total_size += os.path.getsize(image_name)
    return size(total_size)


def resize_images(list_of_image_names):
    print("Optimizing ... ")
    for index, image_name in enumerate(list_of_image_names):
        with open(image_name) as f:
            image_binary = f.read()
        with Image(blob=image_binary) as img:
            if img.height >= 600:
                img.transform(resize='x600')
                img.save(filename=image_name)
    print("Optimization complete.")


if __name__ == '__main__':
    all_images = get_image_file_names(PATH, PATTERN)
    resize_images(all_images)
    get_image_file_names(PATH, PATTERN)
