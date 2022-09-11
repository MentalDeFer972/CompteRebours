import time

def launchRebours(value) :
    while value : 
        time.sleep(1)
        value -= 1
        print("temps:" , str(value))


print("Veuillez saisir le compte à rebours(en secondes)")    
value = input()

launchRebours(int(value))  

if value == 0 :  
    print("Times up!")
