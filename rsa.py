e = 1
c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083

def integer_to_bytes(integer, _bytes):
    output = bytearray()
    for byte in range(_bytes):        
        output.append((integer >> (8 * (_bytes - 1 - byte))) & 255)
    return output

#print(len(str(c))) <- 55
print(integer_to_bytes(c, 54))
