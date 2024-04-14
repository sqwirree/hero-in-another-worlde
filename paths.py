import os

sprites_folder = os.path.join("sprites")
player_sprites_folder = os.path.join(sprites_folder, "player")
bg_sprites_folder = os.path.join(sprites_folder, "bg")
static_sprites_folder = os.path.join(sprites_folder, "static")

sounds_folder = os.path.join("sounds")

sprites = {
    "PLAYER": {
        "idle": ["back1.png"],
        "walk_left": ["left1.png", "left2.png", "left3.png"],
        "walk_right": ["right1.png", "right2.png", "right3.png"],
        "walk_forward": ["back1.png", "back2.png", "back3.png"],
        "walk_back": ["up1.png", "up2.png", "up3.png"]
    },
    "ENEMY": {
        "walk_left": "",
        "walk_right": "",
        "walk_forward": "",
        "walk_back": ""
    },
    "bg1": ["bg1.png"] 
}
