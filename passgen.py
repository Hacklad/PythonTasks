# write a password generation program: letter, number and ymbles
import random

lez = ['A','B','C','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e'
       ,'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num_rz = [0,1,2,3,4,5,6,7,8,9]
symbz = ['!','@','#','$','%','^','&','*','-','+']

fp = []
ki = random.randint(2,5)
le_repp = random.choices(lez,k=ki)
# yyy = random.shuffle(le_repp) // reshuffle is for list
# print(yyy)
# print(le_repp)
# lrepp = ''.join(map(str,le_repp))
num_repp = random.choices(num_rz,k=ki)
# print(num_repp)
# # nrepp = ''.join(map(str,num_repp))
symbz_repp = random.choices(symbz,k=ki)
print(symbz_repp)

fp = symbz_repp + num_repp + le_repp
final_pwd = ''.join(str(po) for po in fp)
print(final_pwd)

# srepp = ''.join(map(str,symbz_repp))
# shuf_io = lrepp + nrepp + srepp
# print(shuf_io)
# final_pass = random.shuffle(shuf_io). 
