import PIL as p
import PIL.Image as I

o = open('test.html', 'w')
Io = I.open('test.JPG')
nIo = Io.resize((200, 150))
height = []
width = []
for i in range(0, nIo.size[1]):
    width = []
    for j in range(0, nIo.size[0]):
        r, g, b = nIo.getpixel((j, i))
        width.append('<a style="font-size:0.2px;background:rgb(%d,%d,%d)">milad</a>' % (r, g, b))
    height.append('</br>')
    height.append(''.join(width))
o.write(''.join(height))
o.close()
