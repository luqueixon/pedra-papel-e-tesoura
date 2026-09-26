import random
l = ["pedra","papel","tesoura"]
o = str(input("Escolha uma das opções:\n"
              "Pedra\n"
              "Papel\n"
              "Tesoura\n"
              ": ")).lower()
x = random.choice(l)
while o != "papel" and o!= "pedra" and o != "tesoura":
    print("Tente Novamente!")
    o = str(input("Escolha uma das opções:\n"
              "Pedra\n"
              "Papel\n"
              "Tesoura\n"
              ": ")).lower()

print(f"O que você jogou: {o}")
print(f"O que você a máquina jogou: {x}")
print("\n")

def final(o,x):
    if o == x:
        print("Empate!")
    elif o == "pedra" and x == "papel" or o == "papel" and x == "tesoura" or o == "tesoura" and x == "pedra":
        print("Você perdeu!")
    else:
        print("Você ganhou!")

final(o,x)



