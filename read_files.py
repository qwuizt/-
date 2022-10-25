#Чтение из файлов
def data():
    with open('in_data.txt') as f_in:
        matrix_data = [list(map(float, row.split())) for row in f_in.readlines()] #матрица с значениямии x и y
    with open('tabl_data.txt') as f_tabl:
        tabl_data = [list(map(float, space.split())) for space in f_tabl] #табличные значения
    return matrix_data,tabl_data