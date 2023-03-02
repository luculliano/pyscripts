import os
import shutil

name_dir, name_file = 'a_m_podcasts', 'podcast_'

MY_PATH = os.path.join('/home', os.getenv('USER'), 'Desktop') + name_dir

catalog_names = []

os.chdir(os.path.join('/home', os.getenv('USER'), 'Downloads'))


def unpack_archive():
    for obj in os.listdir():
        if obj.startswith('[Boominfo.ORG]') and obj.endswith('.zip'):
            catalog_name = name_dir + obj[-7:-4]
            catalog_names.append(catalog_name)
            os.mkdir(catalog_name)
            shutil.unpack_archive(obj, catalog_name)
            os.remove(obj)


def movin_files(path):
    last = max(os.listdir(path),
               key=lambda x: int(x[x.index('_') + 1:-4]))[:-4]
    strt = int(last[last.index('_') + 1:])
    for obj in os.listdir():
        if obj in catalog_names:
            for pathname, dirnames, filenames in os.walk(obj):
                for index, filename in enumerate(sorted(filenames),
                                                 start=strt + 1):
                    os.rename(os.path.join(pathname, filename),
                              path + '/' + name_file + str(index) + '.mp3')
                    strt += 1

            os.rmdir(obj)


def main():
    unpack_archive()
    if len(catalog_names) > 0:
        movin_files(MY_PATH)


if __name__ == '__main__':
    main()
