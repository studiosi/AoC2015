obj_row,  obj_col = 2978,  3083
first_code = 20151125

def generate(obj_row,  obj_col):
    x_row= obj_row + obj_col - 1
    x_n = sum(range(1,  x_row + 1)) - (x_row - obj_col)    
    print(x_n)
    previous = first_code
    aux = first_code
    for i in range(1,  x_n) :
        aux = (previous * 252533) % 33554393
        previous = aux
    return aux

print("RESULT: ",  generate(obj_row,  obj_col))
