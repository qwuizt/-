from line import find_line
#Прогнозное значение
def future_value(matrix_data):
    xmax = max(matrix_data[1])
    xmin = min(matrix_data[1])
    r = xmax - xmin
    x = (sum(matrix_data[0])/len(matrix_data[0])) + 0.1 * r
    from_find_line = find_line(matrix_data)
    y = from_find_line[0] + from_find_line[1] * x
    return x,y



