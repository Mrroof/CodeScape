global_var = 'i am global'

def globe():
    global global_var 
    global_var = "i have been modied"

globe()
print(global_var)

