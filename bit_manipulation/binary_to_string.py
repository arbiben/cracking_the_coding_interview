# given a real number between 0 and 1, print the binary 
# representation. more that 32 chars, return error

def binary_to_string(x):
    if len(str(x).split('.')) != 2:
        return "Error"

    decimal = get_decimal(x)
    int_bin_val = get_int_binary(int(x))
    binary_val = '.'
    while len(binary_val) <= 33 and decimal > 0:
        decimal *= 2
        if decimal < 1:
            binary_val += '0'
        else:
            binary_val += '1'
            decimal -= 1
    

    if len(binary_val) >= 34:
        return "Error booooo"
    
    return str(int_bin_val) + str(binary_val)

def get_decimal(x):
    full_num = str(x).split('.')
    return float(x) - float(full_num[0])

def get_int_binary(x):
    power = 0
    while x >= 2**(power+1):
        power += 1
    bin_val = ''
    for i in range(power, -1, -1):
        if x >= 2**i:
            bin_val += '1'
            x -= (2**i)
        else:
            bin_val += '0'

    return bin_val

print(binary_to_string(40.15625))
