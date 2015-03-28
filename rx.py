# Receptor XMODEM

# dependencies
import serial
s = serial.Serial('/dev/pts/27')

# check  packages
def check(seq, seqn, mensagem, somarec):
    if (seq + int(seqn) == 0):
        fcs = 0
        for i in range(128):
            fcs = fcs + ord(mensagem[i])
        fcs = fcs % 256

        if (fcs == int(somarec)):
            return 1
    return 0

end = 0
msgTotal = ''
while (end == 0):
    soh = s.read(1)

    if soh == str(0x01):
        seq = int(s.read(1))
        seqn = s.read(2)
        mensagem = s.read(128)
        somarec = s.read(3)
        if (check(seq, seqn, mensagem, somarec) == 1):
            msgTotal = msgTotal + mensagem
            s.write(str(0x06))
        else:
            s.write(str(0x15))


    if soh == str (0x04):
        end = 1
print msgTotal
s.close()
