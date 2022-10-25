import matplotlib.pyplot as plt
import math




def draw(matrix_data,a_line1,a_line2,a_sqr1,a_sqr2,a_sqr3,a_exp1,a_exp2):
    plt.plot(matrix_data[1], matrix_data[0], "ro")
    line,sqr,exp = [],[],[] # списки со значениями
    a = min(matrix_data[1])
    b = max(matrix_data[1])
    n = 100
    h = (b-a)/(n-1)
    x_list = [a + h * i for i in range(n)]
    y_line = lambda x: a_line1 + a_line2 * x
    y_sqr = lambda x: a_sqr1 + a_sqr2 * x + a_sqr3 * x**2
    y_exp = lambda x: a_exp1*math.exp(a_exp2*x)
    line = [y_line(x) for x in x_list]
    sqr = [y_sqr(x) for x in x_list]
    exp = [y_exp(x) for x in x_list]
    line_blue = plt.plot(x_list,line) # График линейного уровнения
    line_yellow = plt.plot(x_list,sqr) # График квадратичного уровнения
    line_green= plt.plot(x_list,exp) # график экспоненциального уравнения
    plt.setp(line_blue, color="blue",label='Линейная функция')
    plt.setp(line_yellow, color="yellow",label='Квадратичная функция')
    plt.setp(line_green, color="green",label='Экспоненциальная функция')
    plt.show()
    return True

