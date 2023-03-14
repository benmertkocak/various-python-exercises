import time
import random
name = input("Lütfen ismini söyler misin? ")
print ("Merhaba, " + name, "Adam Asmaca Zamanı!")
time.sleep(1)
print ("Tahminlerine başla...\n")
time.sleep(0.5)

words = ['python','programming','bootcamp','software','science','data']
word = random.choice(words)
guesses = ''
turns = 5
while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
            print (char,end="")    
        else:
            print ("_",end=""),     
            failed += 1    
    if failed == 0:        
        print ("\nKAZANDIN!") 
        break              
    guess = input("\nBir harf tahmin et:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print("\nYanlış")    
        print("\nMaalesef..", + turns, 'Tahmin hakkın kaldı.') 
        if turns == 0:           
            print ("\nKaybettin!")