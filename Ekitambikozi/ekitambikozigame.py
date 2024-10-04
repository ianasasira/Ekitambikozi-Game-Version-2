#This Program was developed by group10 BCS2024

#This program is called ekitambikozi

#Declaring the user player numbers for the game
playerone="one"
playertwo="two"
playerthree="three"
playerfour="four"
playerfive="five"  
playersix="six"
playerseven="seven"


#Declaring the herd variables with predefined values

herdone=10
herdtwo=12
herdthree=14

#Declaring a list for the above variables

cows = [herdone,herdtwo,herdthree]
players = [playerone,playertwo,playerthree,playerfour,playerfive,playersix,playerseven]

#The selected herds for the user player
User_Selection_1=""
User_Selection_2=""
User_Selection_3=""

#This is the player index for iterating between the players
playerone_index = 1
playertwo_index = 0




print("WELCOME TO THE ** THE EKITAMBIKOZI GAME BY GROUP 10 **")
print("THE USER SHOULD NOT PICK ALL COWS AT THE FIRST PICKIN")
print("THE USER SHOULD PICK ATLEAST ONE COW:")
print("THE USER SHOULD PICK FIRST")



#userplayer = input("which of the players one,two three are you picking")
print("Player 1 Please Play:")



for eachplayer in players:
            #This is the user playing

            #This provide iteration between player one and player two
            if playerone_index > playertwo_index:
                print(" *** Ekitambikozi Game *** ")
                print("Please pick a number less than that in the particular herd(s) below")
                print("Player 1 please pick from one of the herds below: 1 or 2 or 3 from below:")
                print("HERDONE(1) "+str(herdone))
                print("HERDTWO(2) "+str(herdtwo))
                print("HERDTHREE(3) "+str(herdthree))

                # Get user input for the herd to select from
                selectedherd= input("Select a herd number 1 or 2 or 3  from above:")

                if selectedherd=="1":

                            playerherd =input("PLAYER 1 how many cows are you taking from herd one ---  :"+str(herdone)+" Cattle:")
                            
                            #Check if the herd number submitted is the same
                            if int(playerherd) >= int(herdone):
                                print("ERROR: Dear Player, please select a number less than in herd one: "+ str(herdone)+" Cattle:")
                                playerherd =input("PLAYER 1 how many cows are you taking from herd one --- which has :"+str(herdone) +"Select a value less than this")
                                
                                # This elif statement checks if the user has submitted a number equal to that in the herd number
                            elif int(playerherd)!= int(herdone) :
                                herdone=int(herdone)-int(playerherd)
                                User_Selection_1 =True
                                
                        
                if int(herdone) ==0 and int(herdtwo)==0 and int(herdthree)==0:
                            print("Yeee! Dear User you win please take Wendy!!!")
                            exit()

                elif selectedherd=="2":
                    playerherd =input("PLAYER 1 how many cows are you taking from herd two:"+str(herdtwo)+" Cattle:")
                    
                    if int(playerherd) >= int(herdtwo):
                                print("ERROR: Dear Player, please select a number less than in herd two: "+ str(herdtwo) +" Cattle:")
                                playerherd =input("PLAYER 1 how many cows are you taking from herd two --- which has :"+str(herdtwo) +"Select a value less than this")
                                
                                # This elif statement checks if the user has submitted a number equal to that in the herd number
                    elif int(playerherd)!= int(herdtwo) :
                                herdtwo=int(herdtwo)-int(playerherd)
                                User_Selection_2 =True
                                print(User_Selection_2)
                                
                        
                if int(herdone) ==0 and int(herdtwo)==0 and int(herdthree)==0:
                        print("Yeee! Dear User you win please take Wendy!!!")
                        exit()
                        


                elif selectedherd =="3":
                    playerherd =input("PLAYER 1 how many cows are you taking from herd three:"+str(herdthree)+" Cattle:")
                    #Check if submitted herd is the same in herds
                    if int(playerherd) >= int(herdthree):
                                print("ERROR: Dear Player, please select a number less than in herd three: "+ str(herdthree) +" Cattle:")
                                playerherd =input("PLAYER 1 how many cows are you taking from herd three --- which has :"+str(herdthree) +"Select a value less than this")
                                
                                # This elif statement checks if the user has submitted a number equal to that in the herd number
                    elif int(playerherd)!= int(herdthree) :
                                herdthree=int(herdthree)-int(playerherd)
                                User_Selection_3 =True
                    

                if int(herdone) ==0 and int(herdtwo)==0 and int(herdthree)==0:
                            print("Yeee! Dear User you win please take Wendy!!!")
                            exit()
            
                    
        ## This is the computer playing
            if playertwo_index < playerone_index:
                
                
                
                if User_Selection_1==True:
                        
                        herdone=0
                        
                        print("PlayerTwo:(The Computer)")
                        #print("PLAYER 2 these are the herds to pick from")
                        print("HERDONE "+str(herdone))
                        print("HERDTWO "+str(herdtwo))
                        print("HERDTHREE "+str(herdthree))
                        #selectedherd= input("select from the herd")
                        User_Selection_1 = False

                        if int(herdone) ==0 and int(herdtwo)==0 and int(herdthree)==0:
                            print("PlayerTwo:(The Computer) wins and i have taken Wendy")
                            exit()


                elif User_Selection_2==True:
                    
                        herdtwo=0
                        
                        

                        print("PlayerTwo:(The Computer)")
                        #print("PLAYER 2 these are the herds to pick from")
                        print("HERDONE "+str(herdone))
                        print("HERDTWO "+str(herdtwo))
                        print("HERDTHREE "+str(herdthree))
                        User_Selection_2=False
                        #selectedherd= input("select from the herd")
                        if int(herdone) ==0 and int(herdtwo)==0 and int(herdthree)==0:
                                print("PlayerTwo:(The Computer) wins and i have taken Wendy")
                                exit()


                elif User_Selection_3 ==True:
                    
                        herdthree=0
                        
                        

                        print("PlayerTwo:(The Computer)")
                        #print("PLAYER 2 these are the herds to pick from")
                        print("HERDONE "+str(herdone))
                        print("HERDTWO "+str(herdtwo))
                        print("HERDTHREE "+str(herdthree))
                        #selectedherd= input("select from the herd")
                        User_Selection_3 = False
                        if int(herdone) ==0 and int(herdtwo)==0 and int(herdthree)==0:
                                print("PlayerTwo:(The Computer) wins and i have taken Wendy")
                                exit()





           






    
        


    


    



    
    
