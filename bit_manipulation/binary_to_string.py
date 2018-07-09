# given a real number between 0 and 1, print the binary 
# representation. more that 32 chars, return error

def binary_to_string(x):
    if len(str(x).split('.')) != 2:
        return "Error"

    decimal = get_decimal(x)
    binary_val = '.'
    while len(binary_val) < 33 and decimal != 1:
        decimal *= 2
        if decimal < 1:
            binary_val += '0'
        else:
            binary_val += '1'
            if decimal > 1:
                decimal = get_decimal(decimal)

    return binary_val

def get_decimal(x):
    full_num = str(x).split('.')
    return float(x) - float(full_num[0])

print(binary_to_string(0.15625))
