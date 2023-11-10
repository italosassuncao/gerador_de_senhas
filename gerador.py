import random
import string


tamanho = int(input("Informe a quantidade de caracteres desejada: "))

chars = string.ascii_letters + string.digits + "/!@#%&+;?"

rand = random.SystemRandom()

print("".join(rand.choice(chars) for i in range(tamanho)))
