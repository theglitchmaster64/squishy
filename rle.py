#!/usr/bin/env python3

def pad(data,size):
    bytes_to_add = size - (len(data)%size)
    last_byte = int.to_bytes(data[-1],1,'little')
    data += last_byte*bytes_to_add
    return data


def compress(data):
    #cmp = b'rle_v0.1' #signature
    cmp = b''
    data += int.to_bytes(data[-1]+1,1,'little') #add a byte to end to make last comparison false
    i = 0
    while (i<len(data)+1):
        l = 1
        j = i
        while (j<len(data)-1):
            #print('comparing {} and {}: {}'.format(chr(data[j]),chr(data[j+1]),data[j]==data[j+1]))
            if (data[j] == data[j+1]):
                l += 1
            else:
                if (l == 1):
                    if (data[j] == 0):
                        cmp += int.to_bytes(data[i],1,'little')
                        cmp += int.to_bytes(data[i],1,'little')
                        i = i + l -1
                        break
                    cmp += int.to_bytes(data[i],1,'little')
                    i = i + l -1
                    break
                elif (l>255):
                    for x in range(0,l//255):
                        cmp += int.to_bytes(data[i],1,'little') + b'\x00' + int.to_bytes(255,1,'little')
                    cmp += int.to_bytes(data[i],1,'little') + b'\x00' + int.to_bytes(l%255,1,'little')
                    i = i + l -1
                    break
                cmp += int.to_bytes(data[i],1,'little') + b'\x00' + int.to_bytes(l,1,'little')
                i = i + l - 1
                break
            j += 1
        i += 1
    return cmp

def decompress(data):
    if (True): #data[0:8] == b'rle_v0.1'):
        data += int.to_bytes(data[-1]+1,1,'little')
        dcmp = b''
        i = 0
        while (i<len(data)-1):
            if (data[i+1]==0):
                if (data[i+2]==0):
                    dcmp += int.to_bytes(data[i],1,'little')
                    dcmp += int.to_bytes(0,1,'little')
                    i=i+3
                    continue
                dcmp += int.to_bytes(data[i],1,'little')*data[i+2]
                i = i+2
            else:
                dcmp += int.to_bytes(data[i],1,'little')
            i+=1
        return dcmp
    else:
        return None

def verify(f1,f2):
    ret = True
    if (len(f1) != len(f2)):
        print('size mismatch {}, {}'.format(len(f1),len(f2)))
        ret = False
    for i in range(0,len(f1)):
        if (f1[i] != f2[i]):
            print('mismatch at position: {}, values are: {} {}'.format(i,f1[i],f2[i]))
            ret = False
    return ret
