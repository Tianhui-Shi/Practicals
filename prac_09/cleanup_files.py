"""
CP1404 Practical
cleanup files
"""

import os

def main():
    print("Current directory is: {}".format(os.getcwd()))
    os.chdir("Lyrics/Christmas")


    # store name in a list
    name = []

    for files in os.listdir('.'):
        if " " not in files:
            file_names = files.split('.')
            name_string = file_names[0]
            for character in enumerate(name_string):
                if character[0] == 0 or character[1].islower():
                    name.append(character[1])
                if character[1].isupper() and character[0] != 0:
                    name.append(" ")
                    name.append(character[1])
                file_names[0] = "".join(name)
            name.clear()
            new_file = file_names[0] + "." + file_names[1]

            os.rename(files, new_file)
    for filename in os.listdir('.'):
        new_name = get_fixed_filename(filename)
        os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name

def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))


#main()
demo_walk()