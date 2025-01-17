#import math
#import plotext as pt
from math import*
#mendefinisikan list variable x dan y
x, y =[], []
#setting frequensi samplingnya
Fs = 8000
#frekuensi glombang yang akan diolah
f1, f2 = 50, 60
#masukan jumlah sinyal yang ingin ditampilkan
sample=1000
#masukan amplitudo sinyal
a, b =220, 110
for i in range(0, sample):
    x.append(a*sin(2*pi*f*i/Fs))
    x.append(b*sin(2*pi*f*i/Fs))
pt.plot(x, label = "Indonesia")
pt.show(x, label = "Japan")
