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
