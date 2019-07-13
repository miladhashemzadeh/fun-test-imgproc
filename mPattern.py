# -*-coding:utf8;-*-
# qpy:3
# qpy:console

__author__ = "milad"
# simple fun android code

o = open("/dev/urandom", 'rb')
p = open("/sdcard/random.html", 'w')
w = []
h = []
for i in range(0, 199):
    for j in range(0, 199):
        w.append('<a style="font-size:0.2px;background:rgb(%d,%d,%d)">100101101</a>'
                 % (int(o.read(1)[0]),
                    int(o.read(1)[0]),
                    int(o.read(1)[0])))
    w.append('</br>')
h.append(''.join(w))
p.write(''.join(h))
o.close()
p.close()
