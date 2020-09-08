import os
import shutil

TASK_DIR = os.path.abspath(os.curdir) + '/tools-developer-task-master'
SCENE_DIR = TASK_DIR + '/src/scenes'
BUILD_BACKGROUND_DIR = TASK_DIR + '/build/backgrounds'
BUILD_THUMBS_DIR = TASK_DIR + '/build/thumbs'
BUILD_TEX_DIR = TASK_DIR + '/build/textures'
BUILD_LOCALE_DIR = TASK_DIR + '/build/locales'


def crop_thumbnails():
    background_images_dict = {}
    for entry in os.scandir(SCENE_DIR):
        if 'background.png' in os.listdir(entry.path + '/scene/'):
            background_images_dict[entry.name] = entry.path + '/scene/background.png'

    if os.path.exists(BUILD_BACKGROUND_DIR):
        shutil.rmtree(BUILD_BACKGROUND_DIR)
    os.makedirs(BUILD_BACKGROUND_DIR)
    for key, value in background_images_dict.items():
        call_with_args = "./woogac crop --width 200 --height 200 --output-dir %s -p %s --format jpg %s " % (BUILD_BACKGROUND_DIR, key + "-background.jpg", value)
        os.system(call_with_args)


def generate_thumbnails():
    item_images_dict = {}
    for entry in os.scandir(SCENE_DIR):
        item_images_dict[entry.name] = []
        scene_files = os.listdir(entry.path + '/scene/')
        for scene in scene_files:
            if "_item" in scene:
                item_images_dict[entry.name].append(entry.path + "/scene/" + scene)
    if os.path.exists(BUILD_THUMBS_DIR):
        shutil.rmtree(BUILD_THUMBS_DIR)
    os.makedirs(BUILD_THUMBS_DIR)
    for key, values in item_images_dict.items():
        file_path = BUILD_THUMBS_DIR + "/" + key
        if os.path.exists(file_path):
            shutil.rmtree(file_path)
        os.makedirs(file_path)
        for value in values:
            call_with_args = "./woogac resize --width 100 --height 100 --output-dir %s -p %s --format jpg %s " % (file_path, os.path.basename(value).replace("_item", ""), value)
            os.system(call_with_args)


def generate_texture():
    texture_atlas_dict = {}
    for entry in os.scandir(SCENE_DIR):
        texture_atlas_dict[entry.name] = []
        scene_files = os.listdir(entry.path + '/scene/')
        for scene in scene_files:
            if scene == "background.png" or "items.json" == scene or "preview.png" == scene:
                continue
            texture_atlas_dict[entry.name].append(entry.path + "/scene/" + scene)
        if os.path.exists(BUILD_TEX_DIR):
            shutil.rmtree(BUILD_TEX_DIR)
        os.makedirs(BUILD_TEX_DIR)
        for key, values in texture_atlas_dict.items():
            call_with_args = "./woogac pack --output-dir %s --file-name %s --format png %s " % (BUILD_TEX_DIR, key + "-atlas.png", " ".join(values))
            os.system(call_with_args)


def collect_locales():
    valid_keys = ["en", "de", "fr", "es"]
    locales_images_dict = {}
    for entry in os.scandir(SCENE_DIR):
        locales_images_dict[entry.name] = []
        locales = os.listdir(entry.path + '/locales/')
        for locale in locales:
            if locale.split("-")[0].split(".json")[0] in valid_keys:
                locales_images_dict[entry.name].append(entry.path + "/locales/" + locale)
    if os.path.exists(BUILD_LOCALE_DIR):
        shutil.rmtree(BUILD_LOCALE_DIR)
    os.makedirs(BUILD_LOCALE_DIR)
    for key, values in locales_images_dict.items():
        file_path = BUILD_LOCALE_DIR + "/" + key
        if os.path.exists(file_path):
            shutil.rmtree(file_path)
        os.makedirs(file_path)
        for value in values:
            shutil.copy(value, file_path)


def main():
    collect_locales()
    crop_thumbnails()
    generate_thumbnails()
    generate_texture()


if __name__ == "__main__":
    main()
