from data import *

## This function returns if 2 packets use the same keystream
def have_same_ks(packet1, packet2):
    zip_tuple = zip(packet1,packet2)
    for x in zip_tuple:
        if(int(x[0] ^ x[1]) > 128):
            print("They have NOT the same KS")
            return False
    #print("They have the same KS")
    return True
    
## Main

packets_same_ks = []

for a in range(0, len(packets)):
    for b in range(a+1, len(packets)):
        if(have_same_ks(packets[a], packets[b])):
            packets_same_ks.append(a)
            packets_same_ks.append(b)
        
print(packets_same_ks)