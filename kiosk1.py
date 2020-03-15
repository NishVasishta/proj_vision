bill=[]
bill1=[]
def intro():
    print('-'*80)
    print()
    first_view=[[1,'PIZZA'],
                [2,'DESSERTS'],
                [3,'SOFTDRINKS'],
                [4,'SNACKS']]
    print("ENTER YOUR CHOICE".center(60))
    print('-'*80)
    print()
    for i in first_view:
        print(i[0],"   ",i[1])
    print()
    print('-'*80)
    c=input("Enter the Card Serial Number: ")
    if c.isdecimal():
        if c=='1':
            bill_piz=pizza_menu()
            bill1.append(bill_piz)
            print("pizza bill is",bill_piz)
            amtp=[i[-1] for i in bill_piz]
            print(amtp)
            t_total_piz=sum(amtp)
            print("Total amt of pizza =",t_total_piz)
            print()
            print("Would you like to order more ? : ")
            if input("If yes, press 'Y'. Else press 'N' : ").lower() =='y':
                intro()
            else:
                print()
                print("Thanks for visiting !!")
           
            bill.append(t_total_piz)
            print(bill)
            
            
                
        
        elif c=='2':
            bill_des=dessert_menu()
            print(bill_des)
            bill1.append(bill_des)
            amtd=[i[-1] for i in bill_des]
            print(amtd)
            t_total_des=sum(amtd)
            print("Total amt of Desserts =",t_total_des)
            print()
            print("Would you like to order more ? : ")
            if input("If yes, press 'Y'. Else press 'N' : ").lower() =='y':
                intro()
            else:
                print()
                print("Thanks for visiting !!")
            bill.append(t_total_des)
        elif c=='3':
            bill_bev=drinks_menu()
            print(bill_bev)
            bill1.append(bill_bev)
            amtb=[i[-1] for i in bill_bev]
            print(amtb)
            t_total_bev=sum(amtb)
            print("Total amt of Softdrinks =",t_total_bev)
            print()
            print("Would you like to order more ? : ")
            if input("If yes, press 'Y'. Else press 'N' : ").lower() =='y':
                intro()
            else:
                print()
                print("Thanks for visiting !!")
            bill.append(t_total_bev)
            
        elif c=='4':
            bill_bites=snacks_menu()
            print(bill_bites)
            bill1.append(bill_bites)
            amts=[i[-1] for i in bill_bites]
            print(amts)
            t_total_bites=sum(amts)
            print("Total amt of Snacks =",t_total_bites)
            print()
            print("Would you like to order more ? : ")
            if input("If yes, press 'Y'. Else press 'N' :    ").lower() =='y':
                intro()
            else:
                print()
                print("Thanks for visiting !!")
            bill.append(t_total_bites)
        else:
            print("Invalid Input")
            print("*"*80)
            if input("Would you like to try again : ").lower()=='y':
                intro()
            else:
                print()
                print("Thanks for visiting !!")
    
    return (bill1,bill)        
    
def pizza_menu():
    print("YOU ARE IN PIZZA WORLD")
    print()
    menu=[[1,'Paneer Tikka',200,300,400],
          [2,'Capsicum',250,350,450],
          [3,'Golden Corn',250,350,400],
          [4,'Special',150,300,450]]
    print('-'*80)
    print()
    print("         SL.NO           PIZZA       ")
    print()
    print("                                          Small                Medium                  Large")
    print()
    for i in menu:
        print("         ",i[0],"             ",i[1])
        print()
        print("                                         ",           i[2],"                  ",         i[3],"                   ",          i[4])
        print("-"*80)
        print()
    lp=[]
    
    s=True
    while s:
        t=[]
        choice=input("ENTER YOUR CHOICE USING SL.NO : ")
        if choice=='1' or choice=='2' or choice=='3' or choice=='4':
            size=input("Enter the size required as S for small, M for medium and L for Large : ").lower()
            if size =='s' or size =='m' or size =='l':
                quant=int(input("ENTER THE QUANTITY : "))
                t.append(choice)
                n=0
            
                if size == 's':
                    n=2
                elif size == 'm':
                    n=3
                elif size == 'l':
                    n=4
                cost =int(menu[int(choice)-1][n]) 
                print(cost)
                product=menu[int(choice)-1][1]
                t.append(product)
                t.append(cost)
                t.append(quant)
                t.append(cost*quant)
            else:
                print("INVALID INPUT")
                break
        if t!=[]:
            lp.append(t)
        print()
        print(lp)
        more=input("Would you like to order more Pizza ?? If yes, Enter Y. If no,Enter N : ").lower()
        if more!='y':
            print("Thnaks for shopping")
            s=False
            break
        continue
    s=False
    
    print("*"*80)
    return(lp)
            
def dessert_menu() :
    print("YOU ARE IN DESSERT WORLD")
    print()
    des_menu=[[1,'lava cake      ',200],
          [2,'Ice cream fudge',250],
          [3,'something sweet',250],
          [4,'random dessert ',150]]
    print('-'*80)
    print()
    print("         SL.NO          DESSERT                     COST ")
    print()
    print("                                            " )
    print()
    for i in des_menu:
        print("         ",i[0],"         ",i[1],"               ", i[2])
        print()
        print("-"*80)
        print()
    ld=[]        
    
    s=True
    while s:
        t=[]
        choice=input("ENTER YOUR CHOICE USING SL.NO : ")
        if choice=='1' or choice=='2' or choice=='3' or choice=='4':
                quant=int(input("ENTER THE QUANTITY :"))
                t.append(choice)
                cost =int(des_menu[int(choice)-1][2])
                product=des_menu[int(choice)-1][1]
                print(cost)
                t.append(product)
                t.append(cost)
                t.append(quant)
                t.append(cost*quant)
        else:
                print("INVALID INPUT")
                break
        if t!=[]:
            ld.append(t)
        print()
        print(ld)
        more=input("Would you like to order more Desserts ?? If yes, Enter Y. If no,Enter N : ").lower()
        if more!='y':
            print("Thnaks for shopping")
            s=False
            break
        continue
    s=False
    
    print("*"*80)
    print(ld)
    return(ld)
    
def drinks_menu() :
    print("YOU ARE IN DRINKS WORLD")
    print()
    bev_menu=[[1,'Mountain Dew      ',160],
          [2,'Coca Cola         ',165],
          [3,'Mint Cooler       ',140],
          [4,'Green Apple Mojito',180]]
    print('-'*80)
    print()
    print("         SL.NO          SOFTDRINKS                     COST ")
    print()
    print("                                            " )
    print()
    for i in bev_menu:
        print("         ",i[0],"         ",i[1],"               ",i[2])
        print()
        print("-"*80)
        print()
    lb=[]        
    
    s=True
    while s:
        t=[]
        choice=input("ENTER YOUR CHOICE USING SL.NO : ")
        if choice=='1' or choice=='2' or choice=='3' or choice=='4':
                quant=int(input("ENTER THE QUANTITY : "))
                t.append(choice)
                cost =int(bev_menu[int(choice)-1][2])
                product=bev_menu[int(choice)-1][1]
                print(cost)
                t.append(product)
                t.append(cost)
                t.append(quant)
                t.append(cost*quant)
        else:
                print("INVALID INPUT")
                break
        if t!=[]:
            lb.append(t)
        print()
        print(lb)
        more=input("Would you like to order more Drinks ?? If yes, Enter Y. If no,Enter N : ").lower()
        if more!='y':
            print("Thnaks for shopping")
            s=False
            break
        continue
    s=False
    
    print("*"*80)
    return(lb)

            
def snacks_menu() :
    print("YOU ARE IN THE WORLD OF QUICK BITES")
    print()
    bite_menu=[[1,'NACHOS       ',200],
          [2,'CHEESE BALLS ',250],
          [3,'POTATO WEDGES',150],
          [4,'GARLIC BREAD ',150]]
    print('-'*80)
    print()
    print("         SL.NO          SNACKS                     COST ")
    print()
    print("                                            " )
    print()
    for i in bite_menu:
        print("         ",i[0],"         ",i[1],"               ", i[2])
        print()
        print("-"*80)
        print()
    ls=[]        
    
    s=True
    while s:
        t=[]
        choice=input("ENTER YOUR CHOICE USING SL.NO : ")
        if choice=='1' or choice=='2' or choice=='3' or choice=='4':
                quant=int(input("ENTER THE QUANTITY : "))
                t.append(choice)
                cost =int(bite_menu[int(choice)-1][2])
                product=bite_menu[int(choice)-1][1]
                print(cost)
                t.append(product)
                t.append(cost)
                t.append(quant)
                t.append(cost*quant)
        else:
                print("INVALID INPUT")
                break
        if t!=[]:
            ls.append(t)
        print()
        print(ls)
        more=input("Would you like to order more Snacks ?? If yes, Enter Y. If no,Enter N : ").lower()
        if more!='y':
            print("Thnaks for shopping")
            s=False
            break
        continue
    s=False
    
    print("*"*80)
    return(ls)


a=True
while a:
    name=input("Enter Your Name: ")
    if name=='' or name==' ':
        print("INVALID NAME!! DO YOU WISH TO CONTINUE?!")
        c=input("Enter 'Y' or 'N': ").lower()
        if c!='y':
            print("THANK YOU FOR VISITING!! HAVE A PLEASANT DAY!!")
            a=False
            break
        continue
    a=False
    print()
    print('-'*80)
    print("CENTRAL PERK".center(60))
    print()
    print("Welcome Mr./Mrs./Miss ",name)
    print('-'*80)
    t_bill=[]
    t_bill=intro()
    if sum(t_bill[1]) != 0:
        print()
        print("-"*60)
        print("-"*100)
        print("CENTRAL PERK".center(100))
        print("-"*100)
        print("Sl.No            PRODUCT                 COST                 QUANTITY               FINAL_PRICE ")
        print("-"*100)
        b=[]
        ts=sum(t_bill[1])
        sgst= ts*(0.025)
        cgst= ts*(0.025)
        tot=ts+sgst+cgst
        for i in bill1:
            for j in range(len(bill1)):
                if j<len(i):
                    b.append(i[j])
        count=0
        for i in b:
            count+=1
            print(count,"           ",i[1])
            print("                                          ",i[2],"                 ",i[3],"                 ",i[4] )
            print("-"*100)
        print("              SGST :                                                             ", sgst)
        print("-"*100)
        print("              CGST :                                                             ", sgst)
        print("-"*100)
        print("              Total Bill :                                                     ", tot,"Rs")
        print("-"*100)
        print()
        print("*"*100)
        print("THANKS FOR SHOPPING !! HAVE A NICE DAY !!".center(100))
        print("*"*100)

    
    
        