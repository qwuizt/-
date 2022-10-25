
import numpy as np
import math


#Линейная аппроксимация

def find_line(matrix_data):
    n_ = len(matrix_data[0])
    mx = sum(matrix_data[1])
    mx2 = 0
    mxy = 0
    for e in range(0,len(matrix_data[1])):
        mx2 += math.pow(matrix_data[1][e],2)
        mxy += matrix_data[1][e] * matrix_data[0][e]    
    my = sum(matrix_data[0])
    m1 = [[n_,mx],[mx,mx2]]
    m2 = [[my],[mxy]]
    m1_inv = np.linalg.inv(m1)
    m1_inv_m2 = m1_inv.dot(m2)
    a1 = m1_inv_m2[0][0]
    a2 = m1_inv_m2[1][0]
    return a1,a2,mx2

#коэффицент корреляции
def find_kor(matrix_data):
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    middle_x = sum(matrix_data[1])/len(matrix_data[1])
    middle_y = sum(matrix_data[0])/len(matrix_data[0])
    for e in range(0,len(matrix_data[0])):
        sum_x += (matrix_data[1][e] - middle_x)**2
        sum_y += (matrix_data[0][e] - middle_y)**2
        sum_xy += (matrix_data[1][e] - middle_x)*(matrix_data[0][e] - middle_y)
    kor = sum_xy/math.sqrt(sum_x*sum_y)
    return kor,sum_x,sum_y

#коэффициент детерминированности
def find_deterline(matrix_data):
    a_line = find_line(matrix_data)
    sum_line =0 
    for e in range(0,len(matrix_data[0])):
        sum_line += (matrix_data[0][e] -(a_line[0] + a_line[1] * matrix_data[1][e]))**2
    from_find_kor = find_kor(matrix_data)
    sum_y = from_find_kor[2]
    deter = 1 - sum_line/sum_y
    return deter,sum_line
  

  
#стандартные ошибки коэффицентов
def k_error_line(matrix_data):
    from_find_deterline = find_deterline(matrix_data)
    dost = from_find_deterline[1] / (len(matrix_data[1]) - 2)
    from_find_line = find_line(matrix_data)
    from_find_kor = find_kor(matrix_data)
    sa1 = math.sqrt((dost * from_find_line[2]) / (len(matrix_data[1])*from_find_kor[1]))
    sa2 = math.sqrt(dost/from_find_kor[1])
    return sa1,sa2

#критерии для проверки нулевых гипотез
def check_line(matrix_data, tabl_data):
    from_find_deterline = find_deterline(matrix_data)
    from_k_error = k_error_line(matrix_data)
    from_find_line = find_line(matrix_data)
    flin = from_find_deterline[0]*(len(matrix_data[1])-2)/(1-from_find_deterline[0])
    ta1 = abs(from_find_line[0]) / from_k_error[0]
    ta2 = abs(from_find_line[1]) / from_k_error[1]
    if flin > tabl_data[0][0]: my_str_forflin = 'Уравнение значимо'
    else: my_str_forflin = 'Уравнение не значимо'
    if ta1 > tabl_data[0][1]: my_str_fors1 = 'значим'
    else: my_str_fors1 = 'не значим'
    if ta2 > tabl_data[0][1]: my_str_fors2 = 'значим'
    else: my_str_fors2 = 'не значим'
    return str(flin),str(ta1),str(ta2),my_str_forflin,my_str_fors1,my_str_fors2




    


