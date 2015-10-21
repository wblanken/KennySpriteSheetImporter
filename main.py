from KennySpriteSlice import KennySpriteSlice, Error


def main():
    try:
        KennySpriteSlice.kenny_sprite_slicer()
    except Error as e:
        print(e.message)

if __name__ == "__main__":
    main()
