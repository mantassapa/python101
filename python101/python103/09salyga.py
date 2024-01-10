#ar blogas pazimys 

# if p<=0 or p>=11:
#     print('netinkamas')
#  1<=p<=10

def ivedimas():
    p = int(input('p = '))
    if not(1<=p<=10):
        print('netinkamas kartokite .. ')
        return ivedimas()
    else:
        return p 

paz = ivedimas()
print('pazimys =', paz)


    

