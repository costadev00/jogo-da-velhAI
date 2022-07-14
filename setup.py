import MinMaxVelha
import MinMaxVelhaAlphaBeta

while True:
   
    print("Escolha para rodar")
    print("1- MinMax")
    print("2- MinMaxAlphaBeta")
    n=input("")       

    if n == "1":
        exec(open("MinMaxVelha.py").read())
        break

    elif n == "2":
        exec(open("MinMaxVelhaAlphaBeta.py").read())
        break

    else:
        print("Opção inválida")