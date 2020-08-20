import os
from pathlib import Path
import subprocess

TASK_DIR = '/home/fadi/Desktop/wooga/tools-developer-task-master'


def crop_thumbnails():
    scene_directory = TASK_DIR + '/src/scenes'
    build_background_dir = TASK_DIR + '/build/background'
    background_images_dict = {}
    for entry in os.scandir(scene_directory):
        if 'background.png' in os.listdir(entry.path + '/scene/'):
            background_images_dict[entry.name] = entry.path + '/scene/background.png'
    if not os.path.exists(build_background_dir):
        os.makedirs(build_background_dir)
    for key in background_images_dict:
        # TODO run woogac on the image then append it as the keyname-background.jpg
        subprocess.call(['sh', './home/fadi/Desktop/wooga/tools-developer-task-master.sh'])
        os.system(TASK_DIR + 'bin/linux/')
        Path(build_background_dir + '/' + key + '-' + 'background.jpg').touch()


def main():
    crop_thumbnails()


if __name__ == "__main__":
    main()
