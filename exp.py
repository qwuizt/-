import numpy as np
import math


#Экспоненциальная аппроксимация

def find_exp(matrix_data):
    n_ = len(matrix_data[0])
    mx = sum(matrix_data[1])    
    my = sum(matrix_data[0])
    m_lny = 0
    m_xlny = 0
    mx2 = 0
    for e in range(0,len(matrix_data[1])):
        m_lny += math.log(matrix_data[0][e])
        m_xlny += matrix_data[1][e] * math.log(matrix_data[0][e])
        mx2 += math.pow(matrix_data[1][e],2)
    m1 = [[n_,mx],[mx,my]]
    m2 = [[m_lny],[m_xlny]]
    m1_inv = np.linalg.inv(m1)
    m1_inv_m2 = m1_inv.dot(m2)
    a1 = m1_inv_m2[0][0]
    a1_exp = math.exp(a1)
    a2_exp = m1_inv_m2[1][0]
    return a1_exp,a2_exp,mx2


#коэффициент детерминированности
def find_deterexp(matrix_data):
    a_exp = find_exp(matrix_data)
    sum_ln =0
    sum_ln_exp = 0 
    for e in range(0,len(matrix_data[0])):
        sum_ln += (math.log(matrix_data[0][e]) - len(matrix_data[0]))**2
        sum_ln_exp += (math.log(matrix_data[0][e]) - math.log(a_exp[0] * math.exp(a_exp[1] * matrix_data[1][e])))**2
    deter = 1 - sum_ln_exp/sum_ln
    return deter,sum_ln_exp
  
#стандартные ошибки коэффицентов
def k_error_exp(matrix_data):
    from_find_deterexp = find_deterexp(matrix_data)
    from_find_exp = find_exp(matrix_data)
    middle_x = sum(matrix_data[1])/len(matrix_data[1])
    sum_x = 0
    for e in range(0,len(matrix_data[0])):
        sum_x += (matrix_data[1][e] - middle_x)**2
    sa1 = math.sqrt((from_find_deterexp[1] * from_find_exp[2])/((len(matrix_data[1])-2)*len(matrix_data[1])*sum_x))
    sa2 = math.sqrt(from_find_deterexp[1]/((len(matrix_data[1])-2)*sum_x))
    return sa1,sa2

#критерии для проверки нулевых гипотез
def check_exp(matrix_data, tabl_data):
    from_find_deterexp = find_deterexp(matrix_data)
    from_k_error = k_error_exp(matrix_data)
    from_find_exp = find_exp(matrix_data)
    fexp = from_find_deterexp[0]*(len(matrix_data[1])-2)/(1-from_find_deterexp[0])
    ta1 = abs(from_find_exp[0]) / from_k_error[0]
    ta2 = abs(from_find_exp[1]) / from_k_error[1]
    if fexp > tabl_data[0][0]: my_str_forfexp = 'Уравнение значимо'
    else: my_str_forfexp = 'Уравнение не значимо'
    if ta1 > tabl_data[0][1]: my_str_fors1 = 'значим'
    else: my_str_fors1 = 'не значим'
    if ta2 > tabl_data[0][1]: my_str_fors2 = 'значим'
    else: my_str_fors2 = 'не значим'
    return str(fexp),str(ta1),str(ta2),my_str_forfexp,my_str_fors1,my_str_fors2