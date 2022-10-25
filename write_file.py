#Запись в файл исходных данных
def write_in_file_tabl(matrix_data, tabl_data):
    with open('out_data.txt', 'a') as f_out:   
        f_out.write("Исходные данные")
        for row in range(0,len(matrix_data)):
            f_out.write("\n")
            for col in range(0,len(matrix_data[0])):
                f_out.write(str(matrix_data[row][col]) + " ")
        f_out.write("\n")
        f_out.write("Число наблюдений: " + str(len(matrix_data[0])) + "\n")
        f_out.write("Табличные данные\n")
        for e in range(0,len(tabl_data)):
            f_out.write(str(tabl_data[e]) + "\n")

#Запись в файл линейной аппроксимации
def write_in_fileline(a1,a2,koef_cor,r_det_l,sa1,sa2,fline,ta1,ta2,my_str_forflin,my_str_fors1,my_str_fors2):
    with open('out_data.txt', 'a') as f_out:   
        f_out.write("коэффициенты линейной аппроксимации: " + "a1=" + str(a1) + ",a2=" + str(a2) + "\n")
        f_out.write("коэффициент корелляции: " + "koef_cor=" + str(koef_cor) + "\n")
        f_out.write("коэффициент детерминированности: " + "R_det_L=" + str(r_det_l) + "\n")
        f_out.write("Cтандартные ошибки коэффициентов: " + "Sa1L=" + str(sa1) + ",Sa2L=" + str(sa2) + "\n")
        f_out.write("Критерии для проверки нулевых гипотез: \n")
        f_out.write("FLine=" + str(fline) + ",ta1L=" + str(ta1) + ",ta2L=" + str(ta2) + "\n")
        f_out.write(my_str_forflin + "\n")
        f_out.write(my_str_fors1 + "\n")
        f_out.write(my_str_fors2 + "\n")
#Запись в файл квадратичной аппроксимации
def write_in_filesqr(a1,a2,a3,r_det_sq,sa1,sa2,sa3,fsqr,ta1,ta2,ta3,my_str_forfsquare,my_str_fors1,my_str_fors2,my_str_fors3):
    with open('out_data.txt', 'a') as f_out:
        f_out.write("коэффициенты квадратичной аппроксимации: " + "a1=" + str(a1) + ",a2=" + str(a2) + ",a3=" + str(a3) + "\n")
        f_out.write("коэффициент детерминированности: " + "R_det_sqr=" + str(r_det_sq) + "\n")
        f_out.write("Cтандартные ошибки коэффициентов: " + "Sa1Sqr=" + str(sa1) + ",Sa2Sqr=" + str(sa2) + ",Sa3Sqr=" + str(sa3) + "\n")
        f_out.write("Критерии для проверки нулевых гипотез: \n")
        f_out.write("Fsqr=" + str(fsqr) + ",ta1Sqr=" + str(ta1) + ",ta2Sqr=" + str(ta2) + ",ta3Sqr=" + str(ta3) + "\n")
        f_out.write(my_str_forfsquare + "\n")
        f_out.write(my_str_fors1 + "\n")
        f_out.write(my_str_fors2 + "\n")
        f_out.write(my_str_fors3 + "\n")
#Запись в файл экспоненциальной аппроксимации
def write_in_fileexp(a1,a2,r_det_exp,sa1,sa2,fexp,ta1,ta2,my_str_forfsexp,my_str_fors1,my_str_fors2):
    with open('out_data.txt', 'a') as f_out:
        f_out.write("коэффициенты экспоненциальной аппроксимации: " + "a1=" + str(a1) + ",a2=" + str(a2) + "\n")
        f_out.write("коэффициент детерминированности: " + "R_det_exp=" + str(r_det_exp) + "\n")
        f_out.write("Cтандартные ошибки коэффициентов: " + "Sa1Exp=" + str(sa1) + ",Sa2Exp=" + str(sa2) + "\n")
        f_out.write("Критерии для проверки нулевых гипотез: \n")
        f_out.write("Fexp=" + str(fexp) + ",ta1Exp=" + str(ta1) + ",ta2Exp=" + str(ta2) + "\n")
        f_out.write(my_str_forfsexp + "\n")
        f_out.write(my_str_fors1 + "\n")
        f_out.write(my_str_fors2 + "\n")
#Запись прогнозного значения
def write_in_filefuture(x,y):
    with open('out_data.txt', 'a') as f_out:
        f_out.write("В прогнозной точке Xpr =" + str(x) + " прогнозное значение Ypr=" + str(y) + "\n")