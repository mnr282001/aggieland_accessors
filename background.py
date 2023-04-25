from pynput import keyboard, mouse
from os import remove, path
from PIL import ImageGrab
from scipy.spatial import KDTree
from webcolors import CSS3_HEX_TO_NAMES, hex_to_rgb
import gtts
from playsound import playsound


def getAudio(color_name):
    # Make a request to Google Text-to-Speech (gTTS) API to get audio synthesis
    tts = gtts.gTTS(color_name)

    # Save the audio file
    tts.save("hello.mp3")

    # Play the audio file
    playsound("hello.mp3")

    # Remove the temporary mp3 file
    if path.isfile("hello.mp3"):
        remove("hello.mp3")


def convert_rgb_to_names(rgb_tuple):
    # Create a dictionary of all the hexadecimal color codes and their respective names in CSS3
    css3_db = CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))

    # Create a KDTree for fast nearest neighbor search on RGB values
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return f'closest match: {names[index]}'


def getHex(rgb):
    # Convert RGB tuple to hexadecimal color code
    return '%02X%02X%02X' % rgb


def getColor(x, y):
    # Get color of a pixel at (x, y) on the screen
    bbox = (int(x), int(y), int(x)+1, int(y)+1)
    im = ImageGrab.grab(bbox=bbox)
    rgbim = im.convert('RGB')
    r, g, b = rgbim.getpixel((0, 0))
    color_name = str(convert_rgb_to_names(tuple([r, g, b])))
    getAudio(color_name)
    print(color_name)


def onClick(x, y, button, pressed):
    # Handle left mouse button click event
    if pressed and button == mouse.Button.left:
        getColor(x, y)


def onRel(key):
    # Handle key release event, specifically Esc key to stop the listeners
    if key == keyboard.Key.esc:
        mlstnr.stop()
        return False


if __name__ == '__main__':
    # Start the keyboard and mouse listeners
    with keyboard.Listener(on_release=onRel) as klstnr:
        with mouse.Listener(on_click=onClick) as mlstnr:
            klstnr.join()
            mlstnr.join()
