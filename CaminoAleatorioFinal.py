import matplotlib.pyplot as plt
import random
from tabulate import tabulate

def generar_camino(pasos_totales, ejecucion, borrachos, cantidad_restaurantes, tiempo_vida):
    print(f"\nEjecución {ejecucion}:")

    resultados = []

    x = [[] for _ in range(borrachos)]
    y = [[] for _ in range(borrachos)]

    res_x = []
    res_y = []

    restaurantes_visitados = {i: False for i in range(cantidad_restaurantes)}

    for res in range(cantidad_restaurantes):
        restauranX = random.randint(1, 9)
        restauranY = random.randint(1, 9)
        print(f"Restaurante {res + 1}: ({restauranX}, {restauranY})")
        res_x.append(restauranX)
        res_y.append(restauranY)

    plt.figure()

    for idx in range(borrachos):
        puntoX = random.randint(1, 9)
        puntoY = random.randint(1, 9)
        print(f"Borracho {idx + 1}: ({puntoX}, {puntoY})")

        x[idx].append(puntoX)
        y[idx].append(puntoY)

    destino = [None] * borrachos
    pasos_hasta_destino = [0] * borrachos

    pasos_iniciales = [pasos_totales] * borrachos

    for paso in range(pasos_totales):
        plt.clf()

        for idx in range(borrachos):
            if destino[idx] == "Restaurante":
                continue

            direccion = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            caminoX = x[idx][-1] + direccion[0]
            caminoY = y[idx][-1] + direccion[1]

            while (caminoX, caminoY) == (x[idx][-1], y[idx][-1]) or caminoX == 0 or caminoY == 0 or caminoX == 10 or caminoY == 10 or (caminoX, caminoY) in zip(x[idx], y[idx]):
                direccion = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
                caminoX = x[idx][-1] + direccion[0]
                caminoY = y[idx][-1] + direccion[1]

            x[idx].append(caminoX)
            y[idx].append(caminoY)
            pasos_hasta_destino[idx] += 1

            for res_idx, (resX, resY) in enumerate(zip(res_x, res_y)):
                if destino[idx] is None and (caminoX, caminoY) == (resX, resY):
                    print(f"Borracho {idx + 1} ¡Llegó al restaurante {res_idx + 1}!")
                    destino[idx] = "Restaurante"
                    if not restaurantes_visitados[res_idx]:
                        pasos_hasta_destino[idx] += pasos_iniciales[idx]
                        restaurantes_visitados[res_idx] = True
                        # Actualizar el camino del borracho con los nuevos pasos
                        for _ in range(pasos_iniciales[idx]):
                            direccion = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
                            caminoX = x[idx][-1] + direccion[0]
                            caminoY = y[idx][-1] + direccion[1]

                            while (caminoX, caminoY) == (x[idx][-1], y[idx][-1]) or caminoX == 0 or caminoY == 0 or caminoX == 10 or caminoY == 10 or (caminoX, caminoY) in zip(x[idx], y[idx]):
                                direccion = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
                                caminoX = x[idx][-1] + direccion[0]
                                caminoY = y[idx][-1] + direccion[1]

                            x[idx].append(caminoX)
                            y[idx].append(caminoY)

                            pasos_hasta_destino[idx] += 1
                        break

        plt.xlim(0, 10)
        plt.ylim(0, 10)
        # Agregar marcadores y líneas de los caminos de los borrachos
        for idx in range(borrachos):
            plt.plot(x[idx], y[idx], marker='*', linestyle='-', label=f'Borracho {idx + 1} - {pasos_hasta_destino[idx]} pasos')

        for res in range(cantidad_restaurantes):
            plt.text(res_x[res], res_y[res], "Restaurante", color='purple', fontsize=10, ha='center', va='bottom')
            plt.plot(res_x[res], res_y[res], marker='o', color='purple', markersize=10)

        plt.pause(0.5)

    ganadores = [idx + 1 for idx, pasos in enumerate(pasos_hasta_destino) if pasos > tiempo_vida]

    if ganadores:
        print(f"\nBorracho(s) {', '.join(map(str, ganadores))} supera el tiempo de vida!")

        for idx in ganadores:
            resultados.append([ejecucion, f"Borracho {idx} - Gana", pasos_hasta_destino[idx - 1]])
    else:
        print("\nNingún borracho superó el tiempo de vida durante esta ejecución.")

        for idx in range(borrachos):
            resultados.append([ejecucion, f"Borracho {idx + 1} - Muere", pasos_hasta_destino[idx]])

    plt.show()

    return resultados

cantidad_ejecuciones = int(input("Ingrese la cantidad de veces que desea ejecutar el programa: "))
pasos_totales = int(input("Ingrese el número total de pasos para generar el camino: "))
borrachos = int(input("Ingrese el número de borrachos: "))
cantidad_restaurantes = int(input("Ingrese la cantidad de restaurantes: "))
tiempo_vida = int(input("Ingrese el tiempo de vida: "))

resultados = []

for ejecucion in range(1, cantidad_ejecuciones + 1):
    resultado = generar_camino(pasos_totales, ejecucion, borrachos, cantidad_restaurantes, tiempo_vida)
    resultados.extend(resultado)

headers = ["Ejecución", "Destino", "Pasos"]

print(tabulate(resultados, headers=headers, tablefmt="grid"))

