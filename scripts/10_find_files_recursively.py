import fnmatch
import os

# constants
PATH = './'
PATTERN = '*.md'


def get_file_names(filepath, pattern):
    matches = []
    if os.path.exists(filepath):
        for root, dirnames, filenames in os.walk(filepath):
            for filename in fnmatch.filter(filenames, pattern):
                # matches.append(os.path.join(root, filename))  # full path
                matches.append(os.path.join(filename))  # just file name
        if matches:
            print("Found {} files:".format(len(matches)))
            output_files(matches)
        else:
            print("No files found.")
    else:
        print("Sorry that path does not exist. Try again.")


def output_files(list_of_files):
    for filename in list_of_files:
        print(filename)


if __name__ == '__main__':
    get_file_names(PATH, PATTERN)
