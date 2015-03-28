import serial
s = serial.Serial('/dev/pts/1')

def txp(seq, data):
    end = 0
    while (end == 0):
        soh = str(0x01)
        s.write(soh)
        s.write(str(seq))
        s.write(str(-seq))

        fcs = 0
        for i in range(128):
            fcs = fcs + ord(data[i])

        fcs = fcs % 256
        s.write(data)
        s.write(str(fcs))
        rx = s.read(1)
        if(rx == str(0x06)):
            end = 1

def txd(data):
    n = len(data) / 128
    if (len(data) % 128 > 0):
        n = n + 1
    for i in range(n):
        seq = i % 256 + 1
        j = i * 128
        dp = data[j:j+128]
        txp(seq, dp)
info = 'abc'
txd(info)
s.close()
