import numpy as np
import math


#квадратичная аппроксимация аппроксимация

def find_square(matrix_data):
    n_ = len(matrix_data[0])
    mx = sum(matrix_data[1])
    my = sum(matrix_data[0])
    mx2 = 0
    mxy = 0
    mx3 = 0
    mx4 = 0
    mx2y = 0
    for e in range(0,len(matrix_data[1])):
        mx2 += math.pow(matrix_data[1][e],2)    
        mxy += matrix_data[1][e] * matrix_data[0][e]
        mx3 += math.pow(matrix_data[1][e],3)
        mx4 += math.pow(matrix_data[1][e],4)
        mx2y += math.pow(matrix_data[1][e],2) * matrix_data[0][e]
    m1 = [[n_,mx,mx2],[mx,mx2,mx3],[mx2,mx3,mx4]]
    m2 = [[my],[mxy],[mx2y]]
    m1_inv = np.linalg.inv(m1)
    m1_inv_m2 = m1_inv.dot(m2)
    a1 = m1_inv_m2[0][0]
    a2 = m1_inv_m2[1][0]
    a3 = m1_inv_m2[2][0]
    return a1,a2,a3,m1_inv


#коэффициент детерминированности
def find_detersquare(matrix_data):
    a_sqr = find_square(matrix_data)
    sum_square =0
    middle_y = sum(matrix_data[0])/len(matrix_data[0]) 
    sum_y = 0
    for e in range(0,len(matrix_data[0])):
        sum_square += (matrix_data[0][e] -(a_sqr[0] + a_sqr[1] * matrix_data[1][e] + a_sqr[2] * (matrix_data[1][e])**2))**2
        sum_y += (matrix_data[0][e] - middle_y)**2
    deter = 1 - sum_square/sum_y
    return deter,sum_square







#стандартные ошибки коэффицентов
def k_error_square(matrix_data):
    from_find_detersquare = find_detersquare(matrix_data)
    dost = from_find_detersquare[1] / (len(matrix_data[1]) - 3)
    from_find_square = find_square(matrix_data)
    sa1 = math.sqrt(dost * from_find_square[3][0][0])
    sa2 = math.sqrt(dost * from_find_square[3][1][1])
    sa3 = math.sqrt(dost * from_find_square[3][2][2])
    return sa1,sa2,sa3

#критерии для проверки нулевых гипотез
def check_square(matrix_data, tabl_data):
    from_find_detersquare = find_detersquare(matrix_data)
    from_k_error = k_error_square(matrix_data)
    from_find_square = find_square(matrix_data)
    fsquare = from_find_detersquare[0]*(len(matrix_data[1])-3)/(2*(1-from_find_detersquare[0]))
    ta1 = abs(from_find_square[0]) / from_k_error[0]
    ta2 = abs(from_find_square[1]) / from_k_error[1]
    ta3 = abs(from_find_square[2]) / from_k_error[2]
    if fsquare > tabl_data[0][2]: my_str_forfsquare = 'Уравнение значимо'
    else: my_str_forfsquare = 'Уравнение не значимо'
    if ta1 > tabl_data[0][3]: my_str_fors1 = 'значим'
    else: my_str_fors1 = 'не значим'
    if ta2 > tabl_data[0][3]: my_str_fors2 = 'значим'
    else: my_str_fors2 = 'не значим'
    if ta3 > tabl_data[0][3]: my_str_fors3 = 'значим'
    else: my_str_fors3 = 'не значим'
    return str(fsquare),str(ta1),str(ta2),str(ta3),my_str_forfsquare,my_str_fors1,my_str_fors2,my_str_fors3