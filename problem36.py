from funcoes import is_palindrome
max = 1000000
resp=[]
for i in range(max):
    binario = str(bin(i))[2:]
    if is_palindrome(binario) and is_palindrome(str(i)):
        #print(i,str(bin(i))[2:])
        resp.append(i)
print(f"Sum of numbers = {sum(resp)}")

