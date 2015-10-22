# Kenny Sprite Sheet Slicer
# KennySpriteSlice.py
# Copyright Will Blankenship 2015

# This will attempt to correctly slice sprite sheets from the Kenny Donation Collection

import xml.etree.ElementTree
from PIL import Image
import shutil
import os

from .Sprite import Sprite
from .Error import Error
from .SpriteMetaFileData import create_meta_file


# Parse a .xml file that includes the sprite map information
def parse_xml(format_file, image_height):
    sprites = []
    for texture in xml.etree.ElementTree.parse(format_file).getroot().iter('SubTexture'):
        sprite = Sprite(texture.attrib['name'].replace('.png', ''),
                        texture.attrib['x'],
                        texture.attrib['y'],
                        texture.attrib['width'],
                        texture.attrib['height'])
        sprite.reverse_y(image_height)
        sprites.append(sprite)
    return sprites


# Parse a .txt file that includes the sprite map information
def parse_text(format_file, image_height):
    sprites = []
    with open(format_file) as ff:
        for line in ff:
            name, x, y, width, height = line.replace(' =', '').split(' ')
            sprite = Sprite(name, x, y, width, height.replace('\n', ''))
            sprite.reverse_y(image_height)
            sprites.append(sprite)
    return sprites


def kenny_sprite_slicer():
    sprites = []

    sprite_sheet = input('Where is the sprite sheet: ').replace('"', '').strip()
    # Get image height
    image_height = Image.open(sprite_sheet).size[1]

    if input('Is there a format file?\n1)Yes\n2)No\n') == '1':
        format_file = input('Where is the format file (.txt or .xml): ').replace('"', '').strip()
        format_file_extension = os.path.splitext(format_file)[1]
        if not os.path.isfile(format_file):
            raise Error('Format file does not exist.')

        if format_file_extension == '.xml':
            sprites = parse_xml(format_file, image_height)
        elif format_file_extension == '.txt':
            sprites = parse_text(format_file, image_height)
        else:
            raise Error('Wrong format file type')

    destination = input('Where is the destination: ').replace('"', '').strip()

    sprite_sheet_name = os.path.split(sprite_sheet)[1]

    if not os.path.isfile(sprite_sheet):
        raise Error('Sprite sheet does not exist.')

    # Create the meta file for the sprite sheet
    create_meta_file(os.path.join(destination, sprite_sheet_name + ".meta"), sprites)

    # Copy the sprite sheet over
    shutil.copy(sprite_sheet, os.path.join(destination, sprite_sheet_name))
