from pynput import keyboard, mouse
from PIL import ImageGrab
from scipy.spatial import KDTree
from webcolors import CSS3_HEX_TO_NAMES
from webcolors import hex_to_rgb


def convert_rgb_to_names(rgb_tuple):
    
    # a dictionary of all the hex and their respective names in css3
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return f'closest match: {names[index]}'


def getHex(rgb):
    return '%02X%02X%02X'%rgb

def getColor(x,y):
    bbox = (int(x),int(y),int(x)+1,int(y)+1)
    im = ImageGrab.grab(bbox=bbox)
    rgbim = im.convert('RGB')
    r,g,b = rgbim.getpixel((0,0))
    color_name = convert_rgb_to_names(tuple([r,g,b]))
    print(color_name)


def onClick(x,y,button,pressed):
    if pressed and button == mouse.Button.left:
        getColor(x,y)



def onRel(key):
    if key == keyboard.Key.esc:
        mlstnr.stop()
        return False
    
    
    
    
if __name__ == '__main__':
    with keyboard.Listener(on_release = onRel) as klstnr:
        with mouse.Listener(on_click = onClick) as mlstnr:
            klstnr.join()
            mlstnr.join()