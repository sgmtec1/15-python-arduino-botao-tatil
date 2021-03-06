# CHAVE TATIL
from pyfirmata import Arduino, INPUT, OUTPUT, util
import lcd
import time

board=Arduino ('COM5')
verm = 7
botao1 = 2
anterior = False
estado = False

it = util.Iterator(board)
it.start()

board.digital[botao1].mode = INPUT
board.digital[verm].mode = OUTPUT

while True:
    valor = board.digital[botao1].read()
    if valor == True and anterior == False:
        estado = not estado
        print('LED', estado)
        board.digital[verm].write(estado)
    anterior = valor
    board.pass_time(0.05)