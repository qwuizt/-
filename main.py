from read_files import data
from line import find_line,find_kor,find_deterline,k_error_line,check_line
from write_file import write_in_file_tabl,write_in_fileexp,write_in_filefuture,write_in_fileline,write_in_filesqr
from square import find_square,find_detersquare,k_error_square,check_square
from exp import find_deterexp,find_exp,k_error_exp,check_exp
from futureValue import future_value
from draw_diagrams import draw
def start():
    matrix_data,tabl_data = data()
    write_in_file_tabl(matrix_data,tabl_data)
    a_line = find_line(matrix_data)
    kor = find_kor(matrix_data)
    det_l = find_deterline(matrix_data)
    sa1l,sa2l = k_error_line(matrix_data)
    mline = check_line(matrix_data,tabl_data)
    write_in_fileline(a_line[0],a_line[1],kor[0],det_l[0],sa1l,sa2l,mline[0],mline[1],mline[2],mline[3],mline[4],mline[5])
    a_sqr = find_square(matrix_data)
    det_sqr = find_detersquare(matrix_data)
    sa1s,sa2s,sa3s = k_error_square(matrix_data)
    msqr = check_square(matrix_data,tabl_data)
    write_in_filesqr(a_sqr[0],a_sqr[1],a_sqr[2],det_sqr[0],sa1s,sa2s,sa3s,msqr[0],msqr[1],msqr[2],msqr[3],msqr[4],msqr[5],msqr[6],msqr[7])
    a_exp = find_exp(matrix_data)
    det_exp = find_deterexp(matrix_data)
    sa1e,sa2e = k_error_exp(matrix_data)
    mexp = check_exp(matrix_data,tabl_data)
    write_in_fileexp(a_exp[0],a_exp[1],det_exp[0],sa1e,sa2e,mexp[0],mexp[1],mexp[2],mexp[3],mexp[4],mexp[5])
    x,y = future_value(matrix_data)
    write_in_filefuture(x,y)
    draw(matrix_data,a_line[0],a_line[1],a_sqr[0],a_sqr[1],a_sqr[2],a_exp[0],a_exp[1])
start()




