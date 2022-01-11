def int_to_binary(n):
   if n > 1:
       int_to_binary(n//2)
   print(n % 2,end = '')
 
int_to_binary(4)