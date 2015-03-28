# Receptor XMODEM

# dependencies
import serial
s = serial.Serial('/dev/pts/27')

# check  packages
def check(seq, seqn, mensagem, somarec):
    somaesp = 0

    if seq - seqn == 0:
        somaesp = int(mensagem) + somaesp % 256

        for i in range(128):
            somaesp = somaesp + int (mensagem[i])

        somaesp = somaesp % 256

        if somaesp == somarec:
            return True

        return False

    return False


soh = s.read(1)
if soh == str (0x01):
    seq = int(s.read())
    # print seq
    seqn = s.read(1)
    # print seqn
    mensagem = s.read(128)
    print mensagem
    somarec = s.read(1)
    # print somarec

    if check(seq, seq, mensagem, somarec):
        s.write(str(0x06))
    else:
        s.write(str(0x15))

else:
    if soh == str (0x04):
        s.write(str(0x06))
        s.close
