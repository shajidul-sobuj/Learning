
def a_lot(num1, num2):
    sum = num1 + num2
    mul = num1 * num2
    dif = abs(num1-num2)

    return sum, mul, dif #touple akare retrun kore
    # return [sum, mul, dif] # list akare return kore

everything = a_lot(5,7)
print(everything)