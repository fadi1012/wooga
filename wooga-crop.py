import os
from pathlib import Path

TASK_DIR = os.path.abspath(os.curdir) + '/tools-developer-task-master'


def crop_thumbnails():
    scene_directory = TASK_DIR + '/src/scenes'
    build_background_dir = TASK_DIR + '/build/background'
    background_images_dict = {}
    for entry in os.scandir(scene_directory):
        if 'background.png' in os.listdir(entry.path + '/scene/'):
            background_images_dict[entry.name] = entry.path + '/scene/background.png'
    if not os.path.exists(build_background_dir):
        os.makedirs(build_background_dir)
    for key, value in background_images_dict.items():
        call_with_args = "./woogac crop --width 200 --height 200 --format jpg %s " % value
        #os.system(call_with_args)
        # TODO might not be needed after solving the issue with running woogac and understanding how export works
        # # --output-dir export
        Path(build_background_dir + '/' + key + '-' + 'background.jpg').touch()


def main():
    crop_thumbnails()


if __name__ == "__main__":
    main()
