'Script that renames files and directories in specified path'
import os

# Desired directory
MY_DIR = os.path.join('/home', os.getenv('USER'), 'Downloads')
# Desired object
MY_OBJ = '[SW.BAND]'
# '1' = add, '0' = remove
TO_DO = 0


def rename_files(path, move):
    'This function renames all filenames in path'
    flag = False  # determine if no such files
    counter = 0  # amount of all desired files
    for pathname in os.walk(path):
        for filename in pathname[2]:
            if move:  # if TO_DO = 1
                if MY_OBJ not in filename:
                    flag = True
                    new_filename = f'{MY_OBJ} {filename}'
                    os.rename(os.path.join(pathname[0], filename),
                              os.path.join(pathname[0], new_filename))

                    if counter < 4:  # print only 3, not all
                        print(filename, '-->', new_filename)

                    counter += 1

            else:
                if MY_OBJ in filename:
                    flag = True
                    new_filename = filename.replace(MY_OBJ, '').strip()
                    os.rename(os.path.join(pathname[0], filename),
                              os.path.join(pathname[0], new_filename))

                    if counter < 4:
                        print(filename, '-->', new_filename)

                    counter += 1

    return flag, counter


def rename_dirs(path, move):
    'This function renames all dirnames in path'
    flag = False
    counter = 0
    for pathname in list(os.walk(path))[::-1]:
        for dirname in pathname[1]:
            if move:
                if MY_OBJ not in dirname:
                    flag = True
                    new_dirname = f'{MY_OBJ} {dirname}'
                    os.rename(os.path.join(pathname[0], dirname),
                              os.path.join(pathname[0], new_dirname))

                    if counter < 4:
                        print(dirname, '-->', new_dirname)

                    counter += 1

            else:
                if MY_OBJ in dirname:
                    flag = True
                    new_dirname = dirname.replace(MY_OBJ, '').strip()
                    os.rename(os.path.join(pathname[0], dirname),
                              os.path.join(pathname[0], new_dirname))

                    if counter < 4:
                        print(dirname, '-->', new_dirname)

                    counter += 1

    return flag, counter


def main():
    'This function is the main part of the script'
    res_files, res_dirs = rename_files(MY_DIR, TO_DO), rename_dirs(MY_DIR, TO_DO)

    if res_files[0] or res_dirs[0]:

        if res_files[1] > 5 or res_dirs[1] > 5:
            print('...')

        print('Renamed successfully!')
        print(f'Total files renamed: {res_files[1]}, Total dirs renamed: {res_dirs[1]}')

    else:
        print('Renamed nothing!')


if __name__ == '__main__':
    main()
