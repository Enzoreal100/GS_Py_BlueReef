#Sobre

O Previsor de Temperaturas powered by Blue Reef é uma ferramenta criada para ser utilizada em conjunto com todo o ecossistema da Blue Reef.

Nele podemos ter a previsão da temperatura média em regiões de bacia de coral do próximo ano, ou ver a linha de prospectiva da temperatura na região, podendo analizar se pode ser uma tendência de temperatura prejudicial a saúde do recife.

As funcionalidades podem executadas através da janela de terminal da IDE ou do sistema.

#Recursos

Bibliotecas utilizadas: 

MatPlotLib - Para a visualização gráfica dos dados, 
Baixar utilizando o comando:

pip install matplotlib

NumPy - Para auxílio nos calculos e utilização do MatPlotLib,
Baixar utilizando o comando:

pip install numpy


#Fluxo

Ao executar o arquivo, teremos a saudação, o print das funcionalidades e seus índice e a requisição de input do usuário para qual funcionalidade utilizar. Caso a condicional não seja satisfeita essa condicional (input diferente de 0 e 1), uma mensagem de erro é impressa e a requisição do input é refeita, até que a condicional seja satisfeita. Quando a condicional for satisfeita, o código executará a operação necessária, sendo: 

1 - Gráfico das temperaturas registradas.

2 - Predição de temperatura média dos próximos 12 meses.


Doravante a execução da tarefa pedida pelo usuário, uma mensagem aparece perguntando se o usuário gostaria de executar mais alguma função do algorítimo. Caso a resposta seja diferente de 's' ou 'n', uma mensagem de erro é impressa e acontece a requesição de input novamente até que a condição seja satisfeita. Caso a resposta seja 's', o códio retorna ao seu início; Caso a resposta seja 'n', uma mensagem de agradecimento aparece ao usuário e o código se encerra.


#Funções

forca_escolha: Força o usuário a escolher entre os caracteres necessários para satisfazer as condicionais

ajusta_curva: ajusta a curva para os dados recebidos, caso o interesse de ver outros dados.

predicta_resultado: 


