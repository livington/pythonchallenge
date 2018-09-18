from PIL import Image, ImageFile

image_name = 'oxygen.png'


if __name__ == '__main__':
    # img = open(image_name, 'rb')
    # p = ImageFile.Parser()
    #
    # while 1:
    #     s = img.read(1024)
    #     if not s:
    #         break
    #     p.feed(s)
    #
    # new_img = p.close()
    # new_img.save('copy' + image_name)

    img = Image.open(image_name)
    px = img.load()
    print(px[img.width-1, img.height-1])
    for r in range(img.height):
            px_color = px[0, r]
            if px_color[1] == px_color[0] and px_color[2] == px_color[0]:
                print(''.join([''.join([chr(px[(c, r)][i]) for i in range(3)]) for c in range(img.width) ]))# if px[(c, r)][0] != px[(c, r)][1] and px[(c, r)][0] != px[(c, r)][2]])
                break

    print(''.join([chr(l) for l in [105, 110, 116, 101, 103, 114, 105, 116, 121]]))