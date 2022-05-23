"""
CP1404 Practical
Demos of various os module examples
Tianhui Shi
"""

import os
import shutil

def main():

    # folder for file
    # folder directory
    folder = []
    directory = []

    os.chdir('FilesToSort')
    dir_reader(folder)


    for f in folder:

        # ask the input
        directory_name = input("Sort {} files into:".format(f))

        # store directory as list
        if directory_name not in directory:
            os.mkdir(directory_name)
            directory.append(directory_name)


        # Scan directory to find match
        for file in os.listdir('.'):
            filenames = file.split('.')
            if os.path.isdir(file):
                continue
            if f == filenames[1]:
                shutil.move(file, directory_name)


def dir_reader(folders):

    for file in os.listdir('.'):
        filenames = file.split('.')
        if os.path.isdir(file):
            continue
        if filenames[1] not in folders:
            folders.append(filenames[1])
    print(folders)


main()