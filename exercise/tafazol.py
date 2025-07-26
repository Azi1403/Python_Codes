# def game(number):
#     s = str(number)
#     p = int(s[0])-int(s[1])
#     if p>0:
#         print(p)  
#     else:
#         print(-p)          
    
# game(17)


# vaghti num/10 kharej ghesmat o baghimande baes jodashodan adad mishe
def game(number):
    p = number//10
    s= number%10
    
    print(max(s,p)-min(s,p))
         
    
game(17)