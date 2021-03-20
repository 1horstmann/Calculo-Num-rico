import classes 


# Definição de dados
x = [2.5 ,3.9 ,2.9, 2.4, 2.9, 0.8, 9.1, 0.8, 0.7, 7.9, 1.8, 1.9, 0.8, 6.5, 1.6, 5.8, 1.3, 1.2, 2.7] #Definindo os dados da variável independente
y = [211, 167, 131, 191, 220, 297, 7, 211, 300, 107, 167, 266, 227, 86, 207, 115, 285, 199, 172] #Definindo os dados da variável dependente


# Chamando a classe
a = classes.AjustamentoDeCurvas(x,y)


# Utilizando a classe
a.calculo_r() #calculando o valor de r
a.calculo_r2() #calculando o valor de r^2
a.ajustamento_linear() #calculando o ajustamento linear
a.ajustamento_quadratico() #calculando o ajustamento quadrático
a.ajustamento_exponencial() #calculando o ajustamento exponencial
a.ajustamento_hiperbolico() #calculando o ajustamento hiperbólico
a.ajustamento_loglog() #calculando o ajustamento log log
a.melhor_expressão_ajustamento(mostrar=True) #verificando qual é o melhor ajustamento
a.calculo_ajustamento(x=10,ajustamento='Linear') #calculando um valor de y, dado um valor de x em determinado ajustamento
