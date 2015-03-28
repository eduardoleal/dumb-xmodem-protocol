#codigo do transmissor - XMODEM

import serial
s = serial.Serial('/dev/pts/1')

seq = 0x01
data = "ABC"

#
# qnd de pacotes
#
def qtdpac(x):
    size = len(x) / 128
    if (len(x) % 128 > 0):
        size =+ 1
    return size

#
# envia pedacos pacote
#
def txp (seq, data):

    fim = False
    while (fim == False):
        fcs = 0
        soh = str(0x01)
        s.write(soh)
        print soh
        s.write(str(seq))
        print seq
        inverso = -seq
        s.write (str(inverso))
        print (inverso)

        for i in range(len(data)):
            fcs = fcs + 1


        for i in range(128 - len(data)):
            data = data + ' '

        data2 = 0

        for c in range(len(data)):
            data2 = data2 + c


        s.write(str(data2))
        print data2
        s.write(str(fcs))
        print (fcs)
        rx = s.read()
        if (rx == str(0x06)):
            fim = True


#
# Main
#
qtd = qtdpac(data)
while (qtd > 0):
    txp(seq, data)
    seq = seq + 0x01
    qtd = qtd - 1


#
#  termina envio
#
# s.write(str (0x04))
# s.close
