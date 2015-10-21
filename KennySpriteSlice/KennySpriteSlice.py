# Kenny Sprite Sheet Slicer
# KennySpriteSlice.py
# Copyright Will Blankenship 2015

# This will attempt to correctly slice sprite sheets from the Kenny Donation Collection


import xml.etree.ElementTree
from PIL import Image
import os

from .Sprite import Sprite
from .Error import Error


def parse_xml(format_file):
    sprites = []
    for texture in xml.etree.ElementTree.parse(format_file).getroot().iter('SubTexture'):
        sprites.append(Sprite(texture.attrib['name'].replace('.png', ''),
                              texture.attrib['x'],
                              texture.attrib['y'],
                              texture.attrib['width'],
                              texture.attrib['height']))
    return sprites


def parse_text(format_file):
    sprites = []
    with open(format_file) as ff:
        for line in ff:
            name, x, y, width, height = line.replace(' =', '').split(' ')
            sprites.append(Sprite(name, x, y, width, height.replace('\n', '')))
    return sprites


def write_meta_file(sprites, name_prefix, output_file):
    # Get image dimensions
    image_height = Image.open(output_file.replace('.meta', '')).size[1]

    # Create a backup of the meta file
    os.rename(output_file, output_file + '.bak')

    # Create the new file and make changes
    recycle_names = False
    in_sprite = False
    sprite_counter = 0
    with open(output_file + '.bak') as inf:
        with open(output_file, 'w') as of:
            for line in inf:
                if line.strip() == 'fileIDToRecycleName:':
                    recycle_names = True
                elif recycle_names and line.strip().startswith('serializedVersion:'):
                    recycle_names = False
                    sprite_counter = 0
                elif recycle_names:
                    line = line.split(': ')[0] + ': ' + name_prefix + sprites[sprite_counter].name + '\n'
                    sprite_counter += 1
                elif line.strip().startswith('- name:'):
                    in_sprite = True
                    line = line.split(': ')[0] + ': ' + name_prefix + sprites[sprite_counter].name + '\n'
                elif in_sprite and line.strip().startswith('x:'):
                    line = line.split(': ')[0] + ': ' + sprites[sprite_counter].x + '\n'
                elif in_sprite and line.strip().startswith('y:'):
                    y_val = image_height - int(sprites[sprite_counter].y) - int(sprites[sprite_counter].height)
                    line = line.split(': ')[0] + ': ' + str(y_val) + '\n'
                elif in_sprite and line.strip().startswith('width:'):
                    line = line.split(': ')[0] + ': ' + sprites[sprite_counter].width + '\n'
                elif in_sprite and line.strip().startswith('height:'):
                    line = line.split(': ')[0] + ': ' + sprites[sprite_counter].height + '\n'
                    sprite_counter += 1
                    in_sprite = False
                of.write(line)

    # Cleanup
    os.remove(output_file + '.bak')


def kenny_sprite_slicer():
    format_file = input('Where is the format file (.txt or .xml): ').replace('"', '').strip()
    output_file = input('Where is the output file (.meta): ').replace('"', '').strip()

    format_file_extension = os.path.splitext(format_file)[1]
    output_file_extension = os.path.splitext(output_file)[1]

    if not os.path.isfile(output_file):
        raise Error('Output file does not exist.')
    elif not os.path.isfile(format_file):
        raise Error('Format file does not exist')
    elif output_file_extension != '.meta':
        raise Error('Invalid output file type.')

    if format_file_extension == '.xml':
        sprites = parse_xml(format_file)
    elif format_file_extension == '.txt':
        sprites = parse_text(format_file)
    else:
        raise Error('Wrong format file type')

    name_prefix = ''
    if input('Would you like to add a prefix to the names?\n1)Yes\n2)No\n') == '1':
        name_prefix = input('What is the prefix you want to use? ')
        name_prefix += '_'

    write_meta_file(sprites, name_prefix, output_file)


def main():
    try:
        kenny_sprite_slicer()
    except Error as e:
        print(e.message)

if __name__ == "__main__":
    main()
