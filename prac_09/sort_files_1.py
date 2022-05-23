"""
CP1404 Practical
Demos of various os module examples
Tianhui Shi
"""

import os
import shutil

def main():

    # set the folder name
    os.chdir("FilesToSort")

    # loop to sort file
    for file in os.listdir('.'):

        # print(file)
        file_name = file.split('.')
        try:
            os.mkdir(file_name[1])
            shutil.move(file, file_name[1])
        except FileExistsError:
            shutil.move(file, file_name[1])

main()