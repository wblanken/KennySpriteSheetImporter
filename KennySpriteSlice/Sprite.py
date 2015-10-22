# Kenny Sprite Sheet Slicer
# Sprite.py
# Copyright Will Blankenship 2015


class Sprite:

    def reverse_y(self, image_height):
        self.y = str(image_height - int(self.y) - int(self.height))

    def __init__(self, name, x, y, width, height):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
