import time as tm
#PROGRAM A
brangkas = []
jumlah = int(input("Maukasn Jumlah Elemen: "))
for i in range(0, jumlah):
    elemen = input("masukan data anda: ")
    brangkas.append(elemen)
 
#for i in range(0, jumlah):
#   print(brangkas[i])
#   tm.sleep(1)

#Program B
prev= t.time()
while(True):
    now = t.time()
    delay = now - prev
    if delay >= 1:
        prev = t.time()
        print("Hello world")