import random

def guss(x):
       random_number=random.randint(1,x)
       guss=0
       while guss != random_number:
            guss=int(input(f'Guss the Number between 1 and {x}:'))
            if guss>random_number:
                print("Sorry TOO HIGH!.Guss Again")
            elif guss<random_number:
                print("Sorry TOO LOW!.Guss Again")

       print(f'Yess!! Cogrdulations the Number {random_number} Your Gussed is Correct') 


def computer_guss(x):
    high=x
    low=1
    feedback=''
    print(" ")
    print()
    print("Now its Computer Turn TO Guss the Number")
    while feedback!='c':
        if high!=low:
             guss=random.randint(low,high)
        else:
            guss=low    
        feedback=input(f'Is{guss} Too High(H), Is  Too Low(L) OR Is Correct(C)')
        if feedback=='h':
            high=guss-1
        elif feedback=='l':
            low=guss+1
    print(f"Ya! Ya! ,The Computer Gussed Your Number,{guss}is Correct")
guss(10)
computer_guss(10)   
