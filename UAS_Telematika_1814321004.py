input = "Sakip Arslan"

res = ''.join(format(ord(i), 'b')for i in input)

ab = (res[0:4])
ac = (res[9])
ad = (res[12:15])
ae = (res[23:26])
af = (res[30:33])
ag = (res[67:70])
ah = (res[-12:-9])

Hasil = ab + ac + ad + ae + af + ag + ah

print("Konversi ke NRZ-L: " +(Hasil))



#Nama   : Sakip Arslan
#NIM    : 1814321004

