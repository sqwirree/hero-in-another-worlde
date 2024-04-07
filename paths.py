import os

sprites_folder = os.path.join("sprites")
player_sprites_folder = os.path.join(sprites_folder, "player")
bg_sprites_folder = os.path.join(sprites_folder, "bg")
static_sprites_folder = os.path.join(sprites_folder, "static")

sounds_folder = os.path.join("sounds")

sprites = {
    "PLAYER": {
        "idle": [""],
        "walk_left": [""],
        "walk_right": [""],
        "walk_forward": [""],
        "walk_back": [""]
    },
    "ENEMY": {
        "idle": "",
        "walk_left": "",
        "walk_right": "",
        "walk_forward": "",
        "walk_back": ""
    }
}
