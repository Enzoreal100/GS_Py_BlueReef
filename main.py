# Importando MatPlotLib e NumPy
import matplotlib.pyplot as plt
import numpy as np

# Dados simulando DB requirida pelo arduino
medias_mensais = np.array(
    [27.5, 27.5, 27.5, 25, 25, 22.5, 20, 20, 22.5, 22.5, 25, 27.5, 27.5, 27.5, 27.5, 25, 25, 22.5, 22.5, 22.5, 22.5, 25,
     25, 27.5, 27.5, 27.5, 27.5, 26.25, 26.25, 23.75, 22.5, 22.5, 23.75, 25, 26.25, 27.5, 27.5, 27.5, 27.5, 26.25,
     23.75, 22.5, 22.5, 22.5, 22.5, 23.75, 25, 26.25, 27.5, 27.5, 27.5, 25, 25, 22.5, 21.25, 21.25, 22.5, 23.75, 25,
     26.25, 26.25, 27.5, 27.5, 25, 23.75, 22.5, 21.25, 21.25, 22.5, 23.75, 25, 26.25, 27.5, 28, 27.5, 26.25, 25, 23.75,
     23.75, 22.5, 22.5, 23.75, 25, 26.25, 27.5, 27.5, 25, 25, 25, 22.5, 22.5, 22.5, 22.5, 25, 26.25, 27.5, 28.75, 27.5,
     28.75, 27.5, 26.25, 23.75, 22.5, 22.5, 23.75, 25, 26.25, 27.5, 27.5, 27.5, 27.5, 27.5, 26.25, 23.75, 22.5, 22.5,
     22.5, 22.5, 23.75, 26.25, 27.5, 27.5, 27.5, 26.25, 25])
mes = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
     32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
     61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
     90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114,
     115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125])


# Func para forçar escolha do usuário

def forca_escolha(msg, cond1, cond2,  msg_erro):
    escolhe = input(msg)
    while not (escolhe == cond1 or escolhe == cond2):
        print(msg_erro)
        escolhe = input(msg)
    return escolhe


#Func para o ajuste na curva
def ajusta_curva(x, y):
    coefs = np.polyfit(x, y, 1)
    return coefs


# func para ver a predição de temperaturas
def predicta_resultado(coeficientes, x):
    c = coeficientes[1] + coeficientes[0] * x
    return c


# Func para vizualização gráfica
def plota_grafico(x, y, cor, cor2, nome,nome2, titulo, nome_x, nome_y):
    plt.figure(figsize=(15, 10))
    plt.plot(x, y, 'o--', color=cor, label=nome)
    plt.title(titulo)
    plt.xlabel(nome_x)
    plt.ylabel(nome_y)
    plt.plot(x, predicta_resultado(ajusta_curva(x, y), x), color = cor2, label= nome2)
    plt.grid(True)
    plt.legend()
    plt.show()


# código do programa
print('Bem vindo ao Previsor de Temperaturas powered by Blue Reef!')

while True:
    predicao_medias = []
    predicao_mes = []
    print('1 - Gráfico de tendência da temperatura\n'
          '2 - Predição da temperatura média dos próximos 12 meses\n')

    escolhe = forca_escolha('Qual a escolha?', '1', '2', 'Por favor, escolha entre 1 e 2')

    while True:
        if escolhe == '1':
            plota_grafico(mes, medias_mensais, 'blue', 'green', 'Temperaturas em determinados meses', 'Linha de tendência',
                          'Médias mensais de temperatura (Jan 2014 - Mai 2024)', 'Mes', 'Temperatura (C)')
            break
        else:
            resultados = predicta_resultado(ajusta_curva(mes, medias_mensais), mes)
            i = 1
            j = 0
            for i in range(12):
                predicao_medias.append(resultados[i])
                predicao_mes.append(i + 1)
                i += 1
            while j in range(len(predicao_mes)):
                print(f'Mes {predicao_mes[j]} = {predicao_medias[j]:.2f} °C')
                j += 1
            break

    confirma = forca_escolha('Gostaria de rever algo? (s/n)', 's', 'n', 'Por favor, digite "s" ou "n"')
    if confirma == 's':
        continue
    else:
        print('Obrigado por utilizar!')
        break

