# Kenny Sprite Sheet Slicer
# SpriteMetaFileData.py
# Copyright Will Blankenship 2015

import uuid
from datetime import datetime


def create_meta_file(out_file_name, sprites):
    # Inject the GUID into the meta file
    metaFileText.insert(1, str('guid: ' + str(uuid.uuid4()).replace('-', '') + __break))
    # current_time = datetime.now()
    # time_stamp = str(current_time.hour) + str(current_time.minute) + str(current_time.microsecond)
    # metaFileText.insert(2, str('timeCreated: ' + time_stamp + __break))

    # Write the meta file
    out_file = open(out_file_name, 'w')
    out_file.writelines(metaFileText)

    for sprite in sprites:
        out_file.writelines(__create_sprite_meta_data(sprite))

    out_file.writelines(metaFileFooter)


def __create_sprite_meta_data(sprite):
    return [
        str(__tab + __tab + '- name: ' + sprite.name + __break),
        str(__tab + __tab + __tab + 'rect: ' + __break),
        str(__tab + __tab + __tab + __tab + 'serializedVersion: 2 ' + __break),
        str(__tab + __tab + __tab + __tab + 'x: ' + sprite.x + __break),
        str(__tab + __tab + __tab + __tab + 'y: ' + sprite.y + __break),
        str(__tab + __tab + __tab + __tab + 'width: ' + sprite.width + __break),
        str(__tab + __tab + __tab + __tab + 'height: ' + sprite.height + __break),
        str(__tab + __tab + __tab + 'alignment: 0 ' + __break),
        str(__tab + __tab + __tab + 'pivot: {x: .5, y: .5} ' + __break),
        str(__tab + __tab + __tab + 'border: {x: 0, y: 0, z: 0, w: 0} ' + __break),
    ]

__tab = '  '
__break = '\n'

metaFileText = [
    str('fileFormatVersion: 2' + __break),
    str('licenseType: Free' + __break),
    str('TextureImporter:' + __break),
    str(__tab + 'fileIDToRecycleName:' + __break),
    str(__tab + 'serializedVersion: 2' + __break),
    str(__tab + 'mipmaps:' + __break),
    str(__tab + __tab + 'mipMapMode: 0' + __break),
    str(__tab + __tab + 'enableMipMap: 0' + __break),
    str(__tab + __tab + 'linearTexture: 0' + __break),
    str(__tab + __tab + 'correctGamma: 0' + __break),
    str(__tab + __tab + 'fadeOut: 0' + __break),
    str(__tab + __tab + 'borderMipMap: 0' + __break),
    str(__tab + __tab + 'mipMapFadeDistanceStart: 1' + __break),
    str(__tab + __tab + 'mipMapFadeDistanceEnd: 3' + __break),
    str(__tab + 'bumpmap:' + __break),
    str(__tab + __tab + 'convertToNormalMap: 0' + __break),
    str(__tab + __tab + 'externalNormalMap: 0' + __break),
    str(__tab + __tab + 'heightScale: .25' + __break),
    str(__tab + __tab + 'normalMapFilter: 0' + __break),
    str(__tab + 'isReadable: 0' + __break),
    str(__tab + 'grayScaleToAlpha: 0' + __break),
    str(__tab + 'generateCubemap: 0' + __break),
    str(__tab + 'cubemapConvolution: 0' + __break),
    str(__tab + 'cubemapConvolutionSteps: 8' + __break),
    str(__tab + 'cubemapConvolutionExponent: 1.5' + __break),
    str(__tab + 'seamlessCubemap: 0' + __break),
    str(__tab + 'textureFormat: -1' + __break),
    str(__tab + 'maxTextureSize: 2048' + __break),
    str(__tab + 'textureSettings:' + __break),
    str(__tab + __tab + 'filterMode: -1' + __break),
    str(__tab + __tab + 'aniso: 16' + __break),
    str(__tab + __tab + 'mipBias: -1' + __break),
    str(__tab + __tab + 'wrapMode: 1' + __break),
    str(__tab + 'nPOTScale: 0' + __break),
    str(__tab + 'lightmap: 0' + __break),
    str(__tab + 'rGBM: 0' + __break),
    str(__tab + 'compressionQuality: 50' + __break),
    str(__tab + 'allowsAlphaSplitting: 0' + __break),
    str(__tab + 'spriteMode: 2' + __break),
    str(__tab + 'spriteExtrude: 1' + __break),
    str(__tab + 'spriteMeshType: 1' + __break),
    str(__tab + 'alignment: 0' + __break),
    str(__tab + 'spritePivot: {x: .5, y: .5}' + __break),
    str(__tab + 'spriteBorder: {x: 0, y: 0, z: 0, w: 0}' + __break),
    str(__tab + 'spritePixelsToUnits: 100' + __break),
    str(__tab + 'alphaIsTransparency: 1' + __break),
    str(__tab + 'textureType: 8' + __break),
    str(__tab + 'buildTargetSettings: []' + __break),
    str(__tab + 'spriteSheet:' + __break),
    str(__tab + __tab + 'sprites:' + __break)
]

metaFileFooter = [
    str(__tab + 'spritePackingTag:' + __break),
    str(__tab + 'userData:' + __break),
    str(__tab + 'assetBundleName:' + __break),
    str(__tab + 'assetBundleVariant:' + __break)
]
