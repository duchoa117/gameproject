import game_object
import json
from addict import Dict
from map_titles.wall import Wall
def load_map(json_file_url):
    # 1 load js >> text
    text = open(json_file_url, "r").read()
    # 2 convert text into dictionary
    map_dict = json.loads(text)
    map = Dict(map_dict)
    data = map.layers[0].data
    width = map.width
    height = map.height
    print(width, height, data)
    # 3 convert dic to object
    return data, width, height

def generate_map(json_file_url):
    data, width, height = load_map(json_file_url)
    for index, title in enumerate(data):
        title_x = (index % width)*16
        title_y = (index // width)*16
        if title == 0:
            pass
        elif title == 1:
            pass

        elif title == 2:
            pass

        elif title == 3:
            pass

        elif title == 4:
            pass

        elif title == 5:
            pass

        elif title == 6:
            pass

        elif title == 7:
            pass

        elif title == 8:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wal11.png"))

        elif title == 9:
            game_object.add(Wall(title_x, title_y, "assets/images/sprite/flood1.png"))

        elif title == 10:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall11.png"))

        elif title == 11:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall10.png"))

        elif title == 12:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall12.png"))

        elif title == 13:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall2.png"))

        elif title == 14:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall3.png"))


        elif title == 15:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall4.png"))

        elif title == 16:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall5.png"))

        elif title == 17:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall6.png"))

        elif title == 18:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall7.png"))

        elif title == 19:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall8.png"))

        elif title == 20:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall9.png"))

        elif title == 21:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall14.png"))

        elif title == 22:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall15.png"))

        elif title == 23:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall16.png"))

        elif title == 24:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall 13.png"))

        elif title == 25:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall 1-1.png"))

        elif title == 26:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall17.png"))

        elif title == 27:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall1-3.png"))

        elif title == 28:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall1-4.png"))

        elif title == 29:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall1-5.png"))

        elif title == 30:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall1-6.png"))

        elif title == 31:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall1-7.png"))

        elif title == 32:
            game_object.add(Wall(title_x,title_y,"assets/images/sprite/wall1-2.png"))


if __name__ == "__main__":
    generate_map("../assets/maps/map.json")
    # pip install -r requirements
    # pip frezze