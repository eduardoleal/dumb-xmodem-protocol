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
        if (fcs == somarec):
            return 1
    return 0

soh = s.read(1)
print str(0x01)
if soh == str(0x01):
    seq = int(s.read(1))
    print seq
    seqn = s.read(2)
    print seqn
    mensagem = s.read(128)
    print mensagem
    somarec = s.read(1)
    print somarec

    if check(seq, seqn, mensagem, somarec) == 1:
        s.write(str(0x06))
    else:
        s.write(str(0x15))


if soh == str (0x04):
    s.close
