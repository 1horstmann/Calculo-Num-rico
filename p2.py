import numpy as np
import matplotlib.pyplot as pt
import sympy as sp

class Ajustamento_de_curvas():
    
    def __init__(self, x: list, y: list):
        self.x = x
        self.y = y
        self.n = len(self.x)
        self.calculo_variaveis()
        self.max_min()

      
    def calculo_variaveis(self):   
        self.x_total = 0
        self.x2_total = 0
        self.x3_total = 0
        self.x4_total = 0

        self.y2_total = 0
        self.y_total = 0
        self.lny_total = 0

        self.xy_total = 0
        self.x2y_total = 0
        self.xlny_total = 0

        for i in range(self.n):
            self.x_total = self.x_total + self.x[i]
            self.x2_total = self.x2_total + self.x[i]**2
            self.x3_total = self.x3_total + self.x[i]**3
            self.x4_total = self.x4_total + self.x[i]**4

            self.y_total = self.y_total +  self.y[i]
            self.y2_total = self.y2_total + self.y[i]**2
            self.lny_total = self.lny_total + np.log(self.y[i])

            self.xy_total = self.xy_total + self.x[i]*self.y[i]
            self.x2y_total = self.x2y_total + self.x[i]**2*self.y[i]
            self.xlny_total = self.xlny_total + self.x[i]*np.log(self.y[i])


    def max_min(self):
        X = self.x[:]
        X.sort()
        Y = self.y[:]
        Y.sort()
        self.xmax = X[-1]
        self.xmin = X[0]
        self.ymax = Y[-1]
        self.ymin = Y[0]
        

    def calculo_r(self):
        self.sxx = self.x2_total - self.x_total**2/self.n
        self.syy = self.y2_total - self.y_total**2/self.n
        self.sxy = self.xy_total - (self.x_total*self.y_total)/self.n
        self.r = round(self.sxy/(np.sqrt(self.sxx*self.syy)),5)

        print(f'r = {self.r}')


    def calculo_r2(self):
        print(f'r^2 = {round(self.r**2,5)}')


    def ajustamento_linear(self, mostrar=True):
        A = np.array([[self.n, self.x_total], 
            [self.x_total, self.x2_total]])

        B = np.array([[self.y_total], 
            [self.xy_total]])

        X = np.dot(np.linalg.inv(A), B)
        a = round(X[0][0],5)
        b = round(X[1][0],5)

        self.y_linear = []
        for i in range(self.n):
            self.y_linear.append(a + b*self.x[i])

        x = np.linspace(0, self.xmax, 1000)
        self.y_linear_grafico = a+b*x

        self.y_linear_calculo = {'a': a, 'b': b}

        if mostrar:
            print(f'y(x) = {a} + {b}*x')
            pt.plot(self.x,self.y,'o',x,self.y_linear_grafico)
            pt.legend(['Dados', 'Ajustamento Linear'])
            pt.title('Ajustamento Linear')
            pt.axis([self.xmin, self.xmax, self.ymin, self.ymax])
            pt.show()
        

    def ajustamento_quadratico(self, mostrar=True):
        A = np.array([[self.n, self.x_total, self.x2_total],
            [self.x_total, self.x2_total, self.x3_total],
            [self.x2_total, self.x3_total, self.x4_total]])

        B = np.array([[self.y_total],
            [self.xy_total],
            [self.x2y_total]])

        X = np.dot(np.linalg.inv(A), B)
        a = round(X[0][0],5)
        b = round(X[1][0],5)
        c = round(X[2][0],5)

        self.y_quadratico = []
        for i in range(self.n):
            self.y_quadratico.append(a + b*self.x[i] + c*self.x[i]**2)

        x = np.linspace(0, self.xmax, 1000)
        self.y_quadratico_grafico = a+b*x+c*x**2

        self.y_quadratico_calculo = {'a': a, 'b': b, 'c':c}

        if mostrar:
            print(f'y(x) = {a} + {b}*x + {c}*x^2')
            pt.plot(self.x,self.y,'o',x,self.y_quadratico_grafico)
            pt.legend(['Dados', 'Ajustamento Quadrático'])
            pt.title('Ajustamento Quadrático')
            pt.axis([self.xmin, self.xmax, self.ymin, self.ymax])
            pt.show()
        

    def ajustamento_exponencial(self, mostrar=True):
        A = np.array([[self.n, self.x_total], 
            [self.x_total, self.x2_total]])

        B = np.array([[self.lny_total], 
            [self.xlny_total]])

        X = np.dot(np.linalg.inv(A), B)
        Y = X[0][0]
        a = round(np.exp(Y),5)
        b = round(X[1][0],5)

        self.y_exponencial = []
        for i in range(self.n):
            self.y_exponencial.append(a*np.exp(b*self.x[i]))
        
        x = np.linspace(0, self.xmax, 1000)
        self.y_exponencial_grafico = a*np.exp(b*x)

        self.y_exponencial_calculo = {'a': a, 'b': b}

        if mostrar:
            print(f'y(x) = {a}*e^({b}*x)')
            pt.plot(self.x,self.y,'o',x,self.y_exponencial_grafico)
            pt.legend(['Dados', 'Ajustamento Exponêncial'])
            pt.title('Ajustamento Exponêncial')
            pt.axis([self.xmin, self.xmax, self.ymin, self.ymax])
            pt.show()


    def ajustamento_hiperbolico(self, mostrar=True):
        A = np.array([[self.n, self.x_total], 
            [self.x_total, self.x2_total]])

        B = np.array([[1/self.y_total], 
            [self.x_total/self.y_total]])

        X = np.dot(np.linalg.inv(A), B)
        a = round(X[0][0],5)
        b = round(X[1][0],5)

        self.y_hiperbolico = []
        for i in range(self.n):
            self.y_hiperbolico.append(1/(a+b*self.x[i]))
        
        x = np.linspace(0, self.xmax, 1000)
        self.y_hiperbolico_grafico = 1/(a+b*x)

        self.y_hiperbolico_calculo = {'a': a, 'b': b}

        if mostrar:
            print(f'y(x) = 1/({a} + {b}*x)')
            pt.plot(self.x,self.y,'o',x,self.y_hiperbolico_grafico)
            pt.legend(['Dados', 'Ajustamento Hiperbólico'])
            pt.title('Ajustamento Hiperbólico')
            pt.axis([self.xmin, self.xmax, self.ymin, self.ymax])
            pt.show()


    def ajustamento_loglog(self, mostrar=True):
        pass


    def melhor_expressão_ajustamento(self, mostrar=True):
        self.ajustamento_linear(mostrar=False)
        self.ajustamento_quadratico(mostrar=False)
        self.ajustamento_exponencial(mostrar=False)
        self.ajustamento_hiperbolico(mostrar=False)

        sigma2_linear = 0
        sigma2_quadratica = 0
        sigma2_exponencial = 0
        sigma2_hiperbolico = 0

        for i in range(self.n):
            sigma2_linear = sigma2_linear + (self.y_linear[i] - self.y[i])**2 / self.n
            sigma2_quadratica = sigma2_quadratica + (self.y_quadratico[i] - self.y[i])**2 / self.n
            sigma2_exponencial = sigma2_exponencial + (self.y_exponencial[i] - self.y[i])**2 / self.n
            sigma2_hiperbolico = sigma2_hiperbolico + (self.y_hiperbolico[i] - self.y[i])**2 / self.n
        sigma = [sigma2_linear, sigma2_quadratica, sigma2_exponencial, sigma2_hiperbolico]

        menor = id_menor = 0
        for i in range(len(sigma)):
            if i == 0:
                menor = round(sigma[i],5)
                id_menor = i
            elif sigma[i] < menor:
                menor = round(sigma[i],5)
                id_menor = i

        if mostrar:
            print(f'Sigma^2 Linear = {sigma[0]}')
            print(f'Sigma^2 Quadrático = {sigma[1]}')
            print(f'Sigma^2 Exponêncial = {sigma[2]}')
            print(f'Sigma^2 Hiperbólico = {sigma[3]}')
            if id_menor == 0:
                print(f'O ajustamento linear é o melhor modelo pois tem a menor variância residual')
                self.melhor = 'Linear'
            elif id_menor == 1:
                print(f'O ajustamento quadrático é o melhor modelo pois tem a menor variância residual')
                self.melhor = 'Quadrático'
            elif id_menor == 2:
                print(f'O ajustamento exponencial é o melhor modelo pois tem a menor variância residual')
            elif id_menor == 3:
                print(f'O ajustamento hiperbólico é o melhor modelo pois tem a menor variância residual')


            x = np.linspace(0, self.xmax, 1000)
            pt.plot(self.x,self.y,'o',x,self.y_linear_grafico,x,self.y_quadratico_grafico,x,self.y_exponencial_grafico,x,self.y_hiperbolico_grafico)
            pt.legend(['Dados', 'Ajustamento Linear', 'Ajustamento Quadrático', 'Ajustamento Exponêncial', 'Ajustamento Hiperbólico'])
            pt.title('Comparação dos ajustamentos')
            pt.axis([self.xmin, self.xmax, self.ymin, self.ymax])
            pt.show()

        else:
            if id_menor == 0:
                self.melhor = 'Linear'
            elif id_menor == 1:
                self.melhor = 'Quadrático'
            elif id_menor == 2:
                self.melhor = 'Exponêncial'
            elif id_menor == 3:
                self.melhor = 'Hiperbólico'

            
    def calculo_ajustamento(self, x:int,ajustamento:str):
        """[Calculo y para um dado valor de x]

        Args:
            x (int): valor de x
            ajustamento (str): 'Linear', 'Quadrático', 'Exponêncial' ou 'Melhor'
        """
        self.melhor_expressão_ajustamento(mostrar=False)

        if ajustamento == 'Melhor':
            if self.melhor == 'Linear':
                resposta = round(self.y_linear_calculo['a']+self.y_linear_calculo['b']*x,5)
                print(f'y({x}) = {resposta}')
            elif self.melhor == 'Quadrático':
                resposta = round(self.y_quadratico_calculo['a']+self.y_quadratico_calculo['b']*x+self.y_quadratico_calculo['c']*x**2,5)
                print(f'y({x}) = {resposta}')
            else:
                resposta = round(self.y_exponencial_calculo['a']*np.exp(self.y_exponencial_calculo['b']*x),5)
                print(f'y({x}) = {resposta}')

        else:
            if ajustamento == 'Linear':
                resposta = round(self.y_linear_calculo['a']+self.y_linear_calculo['b']*x,5)
                print(f'y({x}) = {resposta}')
            elif ajustamento == 'Quadrático':
                resposta = round(self.y_quadratico_calculo['a']+self.y_quadratico_calculo['b']*x+self.y_quadratico_calculo['c']*x**2,5)
                print(f'y({x}) = {resposta}')
            elif ajustamento == 'Exponêncial':
                resposta = round(self.y_exponencial_calculo['a']*np.exp(self.y_exponencial_calculo['b']*x),5)
                print(f'y({x}) = {resposta}')
            else:
                print('Entrada inválida')
        
        

        

        


