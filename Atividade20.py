# Crie um programa que utilize uma estrutura de repetição para somar todos os números pares de 1 a 100 e exiba o resultado.
s = 0
c = input("Digite S para mostrar a soma de todos os números pare entre 1 e 100: ")
if c == ("S") or ("s"):
    for n in range(1, 101):
        if n % 2 == 0:
            s += n
    print(f"Esta é a soma de todos os números pares entre 1 e 100: {s} ")
