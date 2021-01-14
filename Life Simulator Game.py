'''
Asad Rehman
'''
import easygui as a #this program uses easygui, setting as a makes it more convenient
def start(): #set game inside function to allow game to be eaisly restarted at the end
        age = 0 #age counter
        beg = ["Play", "Quit"] 
        beg1 = a.buttonbox("Welcome to Life Simulator. This game simulates the life of a person. Throughout, you will be able to make decisions which will dictate your fate.  Press play to begin.", "", beg)
        if beg1 == beg[0]:
                w = True #If play is clicked, sets w as True so program carries out 
        else:
                quit()
        while w == True:
                saz = ["saz.gif"]
                a.msgbox("Hi! Welcome to the Life simulator.", image = saz)

                gend = ["Male", "Female"]
                gendpick = a.buttonbox("Which gender would you like to be born as?", "", gend)#Gender Choice

                eth = ["Black", "Indian", "Asian", "Hispanic", "White"]
                ethpick = a.buttonbox("Which ethnicity would you like to be born as?", "", eth) #Race Choice

                name = a.enterbox("Please enter your name:") #Name choice

                born = ["baby.gif"] #defines image 
                a.msgbox("Hello " + name + "!") 
                a.msgbox("You are born as a " + ethpick + " " + gendpick + ".", image = born) 
                a.msgbox("You are currently " + str(age) + " years old.")

                age1 = ["Options", "Age"]
                pick1 = a.buttonbox("Would you like to explore your options or age 1 year?", "", age1)

                while pick1 == age1[0]:
                        a.msgbox("You have no options... you were literally just born!")
                        pick1 = a.buttonbox("Would you like to explore your options or age 1 year?", "", age1)
                        if pick1 == age1[1]: 
                                break
                        if pick1 == age1[1]:
                            age += 1
                            a.msgbox("You are now " + str(age) + " years old.")

                import random 
                dadleavechance = random.randint(1, 6) #chance of dad leaving is 50%
                if 1 <= dadleavechance <= 3:
                        firstchoice = ["Play","Let him leave"]
                        pick2 = a.buttonbox("Your dad says he is going to leave. To get him to stay, you must collect 500 shells in the Island Dice Game.", "", firstchoice)
                        if pick2 == firstchoice[1]:
                                a.msgbox("Your dad has left.")
                        if pick2 == firstchoice[0]:
                                import random
                                q = 100
                                a.msgbox("Welcome to the island dice game! You start off with 100 Shells ")
                                y = True
                                while y: #Carries out osland dice game 
                                        b = random.randint(1,6)
                                        c = random.randint(1,6)
                                        d = a.integerbox("How many shells would you like to risk?: ", upperbound = 100)
                                        e = a.enterbox("Please enter a risk level (high or low): ")
                                        f = b + c
                                        if f >= 2 and f <= 6:
                                                if e == "High" or e == "high":
                                                        q -= d
                                                        a.msgbox("The dice rolled is " + str(f))
                                                        a.msgbox("You now have: " + str(q) + " Shells.")
                                                else:
                                                        d = d * 2
                                                        q += d
                                                        a.msgbox("The dice rolled is " + str(f))
                                                        a.msgbox("You now have: " + str(q) + " Shells.")
                                        elif f >= 8 and f <= 12:
                                                if e == "High" or e == "high":
                                                        d = d * 2
                                                        q += d
                                                        a.msgbox("The dice rolled is " + str(f))
                                                        a.msgbox("You now have: " + str(q) + " Shells.")
                                                else:
                                                        q -= d
                                                        a.msgbox("The dice rolled is " + str(f))
                                                        a.msgbox("You now have: " + str(q) + " Shells.")
                                        else:
                                                q -= d
                                                a.msgbox("The dice rolled is " + str(f))
                                                a.msgbox("You now have: " + str(q) + " Shells.")

                                        if q == 0:
                                                a.msgbox("Your dad has left.") #If 500 shells or 0 shells, game ends 
                                                y = False
                                                break
                                        if q >= 500:
                                                a.msgbox("Despite your win, your dad leaves anyways.") #Plot twist 
                else:
                        a.msgbox("Your dad stays with you.")

                                
                age2 = ["Options", "Age"]
                agepick2 = a.buttonbox("Would you like to explore your options or age 9 more years?", "", age2)
                if agepick2 == age2[0]:
                        if 1 <= dadleavechance <= 3: #Different menu based on past 
                                a.msgbox("Your dad just left you... what options do you even have right now??")
                                agepick2 = a.buttonbox("Would you like to explore your options or age 9 more years?", "", age2)
                        else:
                                a.msgbox("Your dad stayed...be happy for now.")
                                agepick2 = a.buttonbox("Would you like to explore your options or age 9 more years?", "", age2)
                if agepick2 == age2[1]:
                        ten = ["ten.gif"]
                        a.msgbox("You are now 10 years old.", image = ten)
                        age +=9
                        if  1 <= dadleavechance <= 3: #Different menu based on past 
                                anx = ["anx.gif"]
                                a.msgbox("You have been getting bullied for the past 6 years and have now been diagnosed with anxiety.", image = anx)
                                age3 = ["Options", "Age"]
                                agepick3 = a.buttonbox("Would you like to explore your options or age 5 years?", "", age3)
                                if agepick3 == age3[0]: #Menu options 
                                        choice1 = ["Transfer Schools", "Drop Out of School", "Assault Your Bully", "Age 5 Years"] 
                                        choicepick1 = a.choicebox("Here are your options:", "", choice1) 

                                        if choicepick1 == choice1[0]: #Transfer Schools
                                                schools = ["Asad Public School", "Spencer Bundy Elementary School"]
                                                schoolpick = a.buttonbox("Please choose which school you'd like to transfer to:", "", schools)
                                                if schoolpick == schools[0]:
                                                        a.msgbox("Your depression got more severe at Asad Public School.")
                                                        a.msgbox("You started eating lots of candy.")
                                                        a.msgbox("You have lost your life at the age of 10 from diabetes.")
                                                        w = False #If they die, loop ends as look is while w is True 
                                                        break
                                                else:
                                                        a.msgbox("Congrats! You have beat your depression.")
                                                        a.msgbox("You are now 11 years old and are the most popular kid in your grade.")
                                                        cand = ["candy.gif"]
                                                        a.msgbox("You are offered a cool candy by an older kid who says it will make you cooler.", image = cand)

                                                        candy = ["Take It", "Don't Take It"]
                                                        candypick = a.buttonbox("Do you take it or not?", "", candy)

                                                        if candypick == candy[0]:
                                                                a.msgbox("You got addicted and started eating a lot of that candy.")
                                                                a.msgbox("You have lost your life at the age of 10 from diabetes.")
                                                                w = False
                                                                break

                                                        else:
                                                                a.msgbox("Good choice!")
                                                                agepick3 = age3[1]                                                
                                                        
                                        elif choicepick1 == choice1[1]: #Drop Out of School
                                                a.msgbox("You have dropped out of school.")
                                                a.msgbox("Your parents are extremely disappointed in your actions.")
                                                drop1 = ["Back to School", "No"]
                                                droppick = a.buttonbox("Do you go back to school or not?", "", drop1)

                                                if droppick == drop1[0]:
                                                        agepick3 = age3[1] #age 5 years 
                                                else:
                                                        a.msgbox("You have been kicked out of your house.")
                                                        a.msgbox("You have nowhere to live.")
                                                        a.msgbox("Your life ended at 11 years old when you got hit by a car and died.")
                                                        w = False
                                                        break
                                        elif choicepick1 == choice1[2]: #Assault Your Bully
                                                a.msgbox("You decide to attack your bully.")
                                                a.msgbox("You are no longer being bullied.")
                                                import random
                                                getcaught = random.randint(1, 6) #chance of getting caught
                                                if 1 < getcaught < 4:
                                                        a.msgbox("You get in trouble for your actions. Your parents are disappointed.")
                                                else:
                                                        a.msgbox("You get away with attacking your bully. No one finds out.")
                                if agepick3 == age3[1]:
                                        a.msgbox("You are now 15 years old.")
                                        age += 5 #add to age counter
                        else:
                            a.msgbox("Childhood is fun.")
                            a.msgbox("You are now 14 years old.")
                            age += 5 #add to age counter

                highs = ["hs.gif"] #image
                a.msgbox("Congrats you are now on your way to high school!", image = highs)
                hs1 = ["Horton High School", "Central Kings High School"] #Differnt outcomes based on school choice
                hspick1 = a.buttonbox("Which highschool would you like to attend?", "", hs1) #hs = Highschool

                stdy = ["study.gif"]

                a.msgbox("On the first day of school, you see some people from middle school hanging out together.")
                hs2 = ["Go Talk to Them", "Say Nothing"]
                hspick2 = a.buttonbox("What do you choose to do?", "", hs2)

                if hspick2 == hs2[0]:
                        if hspick1 == hs1[0]: #If Horton School
                                a.msgbox("They do not want to talk to you.")
                                a.msgbox("You are embarrassed.")
                                hs3 = ["Defend Yourself and Fight", "Run Away"]
                                hspick3 = a.buttonbox("What is your reaction?: ", "", hs3)
                        if hspick1 == hs1[1]:
                                a.msgbox("They welcome you.")
                                a.msgbox("You have made new friends.")

                if hspick2 == hs2[1]: #If you do not talk to them 
                        a.msgbox("You remain antisocial.")

                a.msgbox("You are now 15 years old.")
                age +=1
                a.msgbox("There is a school event coming up.")
                hs4 = ["Go", "Stay Home"]
                hspick4 = a.buttonbox("Do you go with your friends?", "", hs4)
                if hspick4 == hs4[0]: 
                        if hspick2 == hs2[1]:
                                a.msgbox("You have no friends to go with you.")
                                hs5 = ["Yes", "No"]
                                hspick5 = a.buttonbox("Do you try and make some friends? ", "", hs5)
                                if hspick5 == hs5[0]:
                                        if hspick1 == hs1[1] or hspick3 == hs3[0]: #If going to Central Kings or stuck up for themsleves at Horton
                                                a.msgbox("You are able to find friends.")
                                                hspick4 = hs4[0]
                                        else:
                                                a.msgbox("You do not find friends.")
                                else:
                                        a.msgbox("You become depressed.")
                        else:
                                a.msgbox("You have a mediocore time with your friends.")
                if hspick4 == hs4[1]:
                        a.msgbox("You have a good time at home. Your friends are not happy.")
                        import random
                        friendleaves = random.randint(1, 2) #chance of leaving 
                        if friendleaves > 1:
                                a.msgbox("Your friends leave you.")
                                a.msgbox("You are suffering from depression.")
                        else:
                                a.msgbox("Your friends do not invite you next time.")

                        if friendleaves > 1:
                                a.msgbox("Your mom has been noticing that you have been sad. She suggests you go to the therapist with her.")
                                hs5 = ["Go", "Not for me"]
                                hspick5 = a.buttonbox("Do you go to the therapist? ", "", hs5)
                                if hspick5 == hs5[0]:
                                        a.msgbox("You have been cured of your depression.")
                                if hspick5 == hs5[1]:
                                        a.msgbox("You have died from depression.")
                                        w = False
                                        break

                a.msgbox("While at school, you see the popular kids waiting at a locker near you.")
                hs6 = ["Go talk to them", "Leave them alone"]
                hspick6 = a.buttonbox("Do you approach them? ", "", hs6)
                if hspick6 == hs6[0]:
                        if hspick1 == hs1[0]:               
                                import random
                                popchance = random.randint(1, 6) #chance they talk to you 
                                if 1 <= popchance <= 3:
                                        a.msgbox("They welcome you. They take out some suspicious candy.")
                                        hs7 = ["Take the Candy", "Refuse the Candy"]
                                        hspick7 = a.buttonbox("They offer you the candy and tell you to eat it: ", "", hs7)
                                        if hspick7 == hs7[0]:
                                                a.msgbox("You are now popular.")
                                                import random
                                                cdeath = random.randint(1, 6) #chance candy harms you 
                                                if 1 <= cdeath <= 4:
                                                        a.msgbox("The candy kills you. You have died at the age of 15.")
                                                        w = False
                                                        break
                                                else:
                                                        a.msgbox("The candy does not harm you.")
                                        else:
                                                a.msgbox("They call you lame. You leave, ashamed.")                                                        
                                else:
                                        a.msgbox("They do not want to talk to you.")
                        if hspick1 == hs1[1]:
                                a.msgbox("They are friendly. You become popular.")
                else:
                        ("You remain antisocial.")

                notstudy = 0 #Keeps track of if player studies during highschool, dictates future job options 
                study = 0

                a.msgbox("You have a big test tommorow, but your friends want to hang out.", image = stdy)
                hs8 = ["Go hang out", "Stay home and study"]
                hspick8 = a.buttonbox("What do you choose to do? ", "", hs8) #If theys study, add to study, if not, add to notstudy 
                if hspick8 == hs8[0]:
                        a.msgbox("You do bad on your test.")
                        notstudy += 1 
                else:
                        a.msgbox("You do well on your test.")
                        study += 1

                a.msgbox("You start to like someone in school.")
                if gendpick == gend[0]: #If guy, they like female, if girl, they like guy 
                        a.msgbox("You have a crush on Carly.") 
                if gendpick == gend[1]:
                        a.msgbox("You have a crush of Freddie.")
                hs9 = ["Yes", "No"]
                hspick9 = a.buttonbox("Do you ask them out? ", "", hs9)
                if hspick9 == hs9[0]:
                        import random
                        datechance = random.randint(1, 6)#chane they say yes 
                        if 1 <= datechance <= 3:
                                a.msgbox("They say yes. You are now dating.")
                                if ethpick == eth[1]: 
                                        a.msgbox("Your parents find out about your secret relationship.")
                                        a.msgbox("You are sent back to your home country. You die at the age of 16.")
                                        w = False
                                        break
                                else:
                                        a.msgbox("Yor significant other wants to have sex, but you do not have a condom.")
                                        bb1 = ["Yes", "No"] # bb = Baby 
                                        bbpick1 = a.buttonbox("Do you have sex?: ", "", bb1)
                                        if bbpick1 == bb1[0]:
                                                a.msgbox("You have unprotected sex.")
                                                import random
                                                babychance = random.randint(1, 6)
                                                if 1 <= babychance <= 5: #chance of baby 
                                                        a.msgbox("Uh oh, theres a baby coming.")
                                                        if gendpick == gend[1]:
                                                                bb2 = ["Keep it", "Abortion"]
                                                                bbpick2 = a.buttonbox("What do you do? ", "", bb2)
                                                                if bbpick2 == bb2[0]:
                                                                        a.msgbox("You die during pregnancy.")
                                                                        w = False
                                                                        break
                                                                else:
                                                                        a.msgbox("You die during the abortion procedure.")
                                                                        w = False
                                                                        break
                                                        else:
                                                                ("Your girlfriends dad murders you.")
                                                                w = False
                                                                break
                                                else:
                                                        ("You had fun.")
                                        else:
                                                a.msgbox("They break up with you.")
                        else:
                                a.msgbox("They reject you.")
                                        
                else:
                        a.msgbox("You remian single and lonely.")

                        
                a.msgbox("You have a big assignment tommorow, but your friends want to hang out.", image = stdy) #study scenerio, adds to counter
                hs10 = ["Go hang out", "Stay home and work"]
                hspick10 = a.buttonbox("What do you choose to do? ", "", hs8)
                if hspick10 == hs10[0]:
                        a.msgbox("You do bad on your assignment.")
                        notstudy += 1
                else:
                        a.msgbox("You do well on your assignment.")
                        study += 1                        
                        
                a.msgbox("You have an exam tommorow, but your friends want to hang out.", image = stdy) #study scenerio, adds to counter
                hs11 = ["Go hang out", "Stay home and study"]
                hspick11 = a.buttonbox("What do you choose to do? ", "", hs8)
                if hspick11 == hs11[0]:
                        a.msgbox("You do bad on your exam.")
                        notstudy += 1
                else:
                        a.msgbox("You do well on your exam.")
                        study += 1

                age += 2
                grad = ["grad.gif"]
                a.msgbox("You are now 18 years old. You graduate highschool.", image = grad)

                choices2 = ["Workplace", "Community College", "University",] #Different choices in future 
                choicepicks2 = a.choicebox("Here are your options moving forward:", "", choices2)
                age = 18
                if choicepicks2 == choices2[2]: #If they did not study, notstudy will be greater than study and they cannot go to University 
                        if study < notstudy:
                                a.msgbox("Your grades are not high enough for Univeristy.")
                                choicepicks2 = a.choicebox("Here are your options moving forward:", "", choices2)
                        else:
                                choices3 = ["Engineering", "Business", "Computer Science", "Arts"] #choices in University, dictates future jobs
                                choicepicks3 = a.choicebox("Select your major:", "", choices3)
                                a.msgbox("You are now enrolled in University.")
                                age += 4 #University is four year program
                                a.msgbox("You have graduated from University with a degree.")

                if choicepicks2 == choices2[1]:
                        a.msgbox("You are enrolled in Community College.")
                        age += 2 #Community college is two year program
                        a.msgbox("You have graduated from Community College.")
                if choicepicks2 == choices2[0]:
                        a.msgbox("You do not pursue further education.")

                work = ["work.gif"]
                a.msgbox("Welcome to the workplace. You are " + str(age) + ".", image = work) #age varies based on choice
                job = 0 #new counters keep track of employment and living status 
                move = 0
                while age <= 28: #This menu set is active until 28, then is replaced

                        lf1 = ["Options", "Age"]
                        lfpick1 = a.buttonbox("Would you like to explore your options or age 1 year?", "", lf1)
                        if lfpick1 == lf1[0]:
                                lfchoice1 = ["Get a Job", "Move Out"]
                                lfchoice = a.choicebox("Here are your options:", "", lfchoice1)
                                if lfchoice == lfchoice1[1]:
                                        if job > 2: #job status determines eligibilty to move out 
                                                 if move > 5: #If they have moved out, counter will keep track and inform 
                                                        a.msgbox("You do not live with your parents.")
                                                 else:
                                                        a.msgbox("You move out from your parents house.")
                                                        move += 10 #adds to counter first time they move out                                      
                                                
                                        else:
                                                a.msgbox("You do not have a job. You cannot move out.") 

                                if lfchoice == lfchoice1[0]:
                                        if job > 2: #if they already have a job when clicking job option
                                                jbchoice1 = ["YES", "NO"]
                                                jbpick1 = a.buttonbox("You already have a job. Do you want to leave it?", "", jbchoice1) #choice to leave job
                                                if jbpick1 == jbchoice1[0]:
                                                        job = 0 #if leave job, set counter to zero
                                                        jobchoice1 = a.choicebox("Here are possible job options: ", "", jobchoice) #job menu 
                                                        if jobchoice1 == jobchoice[0]: 
                                                                if choicepicks2 == choices2[2] and choicepicks3 == choices3[0]: #qualification check: will not let user get job unless they have necessary education 
                                                                        a.msgbox("Welcome to your new position.")
                                                                        job += 15 #specific value will dictate aspects later on 
                                                                else:
                                                                        a.msgbox("You are unable to get this job.")
                                                
                                                        if jobchoice1 == jobchoice[1]:
                                                                if choicepicks2 == choices2[2] and choicepicks3 == choices3[2]: #qualification check 
                                                                        a.msgbox("Welcome to your new position.")
                                                                        job += 15
                                                                else:
                                                                        a.msgbox("You are unable to get this job.")
                                                        if jobchoice1 == jobchoice[2]:
                                                                if choicepicks2 == choices2[2] and choicepicks3 == choices3[1]: #qualification check 
                                                                        a.msgbox("Welcome to your new position.")
                                                                        job += 15
                                                                else:
                                                                        a.msgbox("You are unable to get this job.")
                                                        if jobchoice1 == jobchoice[3] or jobchoice1 == jobchoice[4]: #qualifcation check 
                                                                if choicepicks2 != choices2[0]:
                                                                        a.msgbox("Welcome to your new position.")
                                                                        job += 10
                                                                else:
                                                                        a.msgbox("You are unable to get this job.")
                                                        if jobchoice1 == jobchoice[5] or jobchoice1 == jobchoice[6]:
                                                                a.msgbox("Welcome to your new position.")
                                                                job += 5   
                                                if jbpick1 == jbchoice1[1]:
                                                                        a.msgbox("You stay with your current job.")
                                        else: #if they do not already have job, goes straight into job menu 
                                                jobchoice = ["Junior Engineer", "Game Developer", "Financial Analyst", "Teacher", "Marketing Agent", "Fast Food Worker", "Taxi Driver"]
                                                jobchoice1 = a.choicebox("Here are possible job options: ", "", jobchoice)
                                                if jobchoice1 == jobchoice[0]:
                                                        if choicepicks2 == choices2[2] and choicepicks3 == choices3[0]:
                                                                a.msgbox("Welcome to your new position.")
                                                                job += 15
                                                        else:
                                                                a.msgbox("You are unable to get this job.")
                                        
                                                if jobchoice1 == jobchoice[1]:
                                                        if choicepicks2 == choices2[2] and choicepicks3 == choices3[2]:
                                                                a.msgbox("Welcome to your new position.")
                                                                job += 15
                                                        else:
                                                                a.msgbox("You are unable to get this job.")
                                                if jobchoice1 == jobchoice[2]:
                                                        if choicepicks2 == choices2[2] and choicepicks3 == choices3[1]:
                                                                a.msgbox("Welcome to your new position.")
                                                                job += 15
                                                        else:
                                                                a.msgbox("You are unable to get this job.")
                                                if jobchoice1 == jobchoice[3] or jobchoice1 == jobchoice[4]:
                                                        if choicepicks2 != choices2[0]:
                                                                a.msgbox("Welcome to your new position.")
                                                                job += 10
                                                        else:
                                                                a.msgbox("You are unable to get this job.")
                                                if jobchoice1 == jobchoice[5] or jobchoice1 == jobchoice[6]:
                                                        a.msgbox("Welcome to your new position.")
                                                        job += 5                              
                                                        
                        if lfpick1 == lf1[1]:
                                age += 1 #adds 1 to age if they click age one year
                                a.msgbox("You are now " + str(age) + "." )
                                import random #chance of cancer in youth
                                cancerchance = random.randint(1, 15)
                                if cancerchance == 10: 
                                        can = ["canc.gif"]
                                        a.msgbox("You have been diagnosed with cancer.", image = can)
                                        import random
                                        survchance = random.randint(1, 10)#chance of beating cancer 
                                        if 1 < survchance < 5:
                                                a.msgbox("You have died from cancer.")
                                                w = False
                                                break
                                        else:
                                                a.msgbox("You have beat cancer.")
                                
                        savings = 0 #counter keeps track of savings, dictates what they can buy 
                        date = 0 #keep track of relationship status 
                while 29 <= age < 65: #new menu for thse ages 

                        fe1 = ["Options", "Age"] #f = final (final menu) 
                        fepick1 = a.buttonbox("Would you like to explore your options or age 1 year?", "", fe1)
                        if fepick1 == fe1[0]:
                                fchoice1 = ["Job Change", "Buy a House", "Buy a Car", "Play Lottery", "Relationships"] #choices
                                fpick1 = a.choicebox("Here are your options:", "", fchoice1)
                                if fpick1 == fchoice1[0]:
                                        if job > 2: #checks job status 
                                                jbchoice1 = ["YES", "NO"]
                                                jbpick1 = a.buttonbox("You already have a job. Do you want to leave it?", "", jbchoice1)
                                                if jbpick1 == jbchoice1[0]: #job choices
                                                        job = 0
                                                        jobchoice1 = a.choicebox("Here are possible job options: ", "", jobchoice)
                                                        if jobchoice1 == jobchoice[0]:
                                                                if choicepicks2 == choices2[2] and choicepicks3 == choices3[0]: #qualification check(same as above)
                                                                        a.msgbox("Welcome to your new position.")
                                                                        job += 15
                                                                else:
                                                                        a.msgbox("You are unable to get this job.")
                                                
                                                        if jobchoice1 == jobchoice[1]:
                                                                if choicepicks2 == choices2[2] and choicepicks3 == choices3[2]:
                                                                        a.msgbox("Welcome to your new position.")
                                                                        job += 15
                                                                else:
                                                                        a.msgbox("You are unable to get this job.")
                                                        if jobchoice1 == jobchoice[2]:
                                                                if choicepicks2 == choices2[2] and choicepicks3 == choices3[1]:
                                                                        a.msgbox("Welcome to your new position.")
                                                                        job += 15
                                                                else:
                                                                        a.msgbox("You are unable to get this job.")
                                                        if jobchoice1 == jobchoice[3] or jobchoice1 == jobchoice[4]:
                                                                if choicepicks2 != choices2[0]:
                                                                        a.msgbox("Welcome to your new position.")
                                                                        job += 10
                                                                else:
                                                                        a.msgbox("You are unable to get this job.")
                                                        if jobchoice1 == jobchoice[5] or jobchoice1 == jobchoice[6]:
                                                                a.msgbox("Welcome to your new position.")
                                                                job += 5   
                                                if jbpick1 == jbchoice1[1]:
                                                                        a.msgbox("You stay with your current job.")
                                        else:
                                                jobchoice = ["Senior Engineer", "Senior Game Developer", "Senior Financial Analyst", "Head Teacher", "Senior Marketing Agent", "Fast Food Manager", "Taxi Driver"]
                                                jobchoice1 = a.choicebox("Here are possible job options: ", "", jobchoice)
                                                if jobchoice1 == jobchoice[0]:
                                                        if choicepicks2 == choices2[2] and choicepicks3 == choices3[0]:
                                                                a.msgbox("Welcome to your new position.")
                                                                job += 15
                                                        else:
                                                                a.msgbox("You are unable to get this job.")
                                        
                                                if jobchoice1 == jobchoice[1]:
                                                        if choicepicks2 == choices2[2] and choicepicks3 == choices3[2]:
                                                                a.msgbox("Welcome to your new position.")
                                                                job += 15
                                                        else:
                                                                a.msgbox("You are unable to get this job.")
                                                if jobchoice1 == jobchoice[2]:
                                                        if choicepicks2 == choices2[2] and choicepicks3 == choices3[1]:
                                                                a.msgbox("Welcome to your new position.")
                                                                job += 15
                                                        else:
                                                                a.msgbox("You are unable to get this job.")
                                                if jobchoice1 == jobchoice[3] or jobchoice1 == jobchoice[4]:
                                                        if choicepicks2 != choices2[0]:
                                                                a.msgbox("Welcome to your new position.")
                                                                job += 10
                                                        else:
                                                                a.msgbox("You are unable to get this job.")
                                                if jobchoice1 == jobchoice[5] or jobchoice1 == jobchoice[6]:
                                                        a.msgbox("Welcome to your new position.")
                                                        job += 5                              

                                if fpick1 == fchoice1[1]: #house choices 
                                        hchoice1 = ["Condo: 60,000 Dollars", "Small 2 Bedroom House: 100,000 Dollars", "4 Bedroom House: 300,000 Dollars", "Large 6 Bedroom House: 600,000 Dollars", "Mansion: 10,000,000 Dollars"]
                                        hpick1 = a.choicebox("Here are the available houses:", "", hchoice1) # h = house
                                        if hpick1 == hchoice1[0]:
                                                if savings >= 60000: #savings check: counter (amount of money) dictates which house user can buy 
                                                        con = ["cond.gif"]
                                                        a.msgbox("You have purchased a condo.", image = con)
                                                        savings -= 60000 #if they buy, subtracts cost from savings 
                                                else:
                                                        a.msgbox("You do not have enough money to buy this house.") 
                                        if hpick1 == hchoice1[1]:
                                                if savings >= 100000: #savings check
                                                        smhouse = ["smhouse.gif"]
                                                        a.msgbox("You have purchased a Small 2 Bedroom House.", image = smhouse)
                                                        savings -= 100000 #subtract from counter
                                                else:
                                                        a.msgbox("You do not have enough money to buy this house.")
                                        if hpick1 == hchoice1[2]:
                                                if savings >= 300000:
                                                        midhouse = ["midhouse.gif"]
                                                        a.msgbox("You have purchased a 4 Bedroom House.", image = midhouse)
                                                        savings -= 300000 
                                                else:
                                                        a.msgbox("You do not have enough money to buy this house.")
                                        if hpick1 == hchoice1[3]:
                                                if savings >= 600000:
                                                        bighouse = ["bighouse.gif"]
                                                        a.msgbox("You have purchased a Large 6 Bedroom House.", image = bighouse)
                                                        savings -= 600000
                                                else:
                                                        a.msgbox("You do not have enough money to buy this house.")
                                        if hpick1 == hchoice1[4]:
                                                if savings >= 10000000:
                                                        mansion = ["mansion.gif"]
                                                        a.msgbox("You have purchased the Mansion.", image = mansion)
                                                        savings -= 10000000
                                                else:
                                                        a.msgbox("You do not have enough money to buy this house.")
                                if fpick1 == fchoice1[2]: #car choices
                                        cchoice1 = ["Honda Civic: 10,000 Dollars", "Toyota Rav4: 15,000 Dollars", "BMW M5: 25,000 Dollars", "Range Rover: 40,000 Dollars", "Mercedes Benz S Class: 100,000 Dollars", "Bugatti Chiron: 1,000,000 Dollars"]
                                        cpick1 = a.choicebox("Here are the available cars:", "", cchoice1) # c = car 
                                        if cpick1 == cchoice1[0]:
                                                if savings >= 10000: #savings check: checks if user has enough money to buy car
                                                        honda = ["bad_car.gif"]
                                                        a.msgbox("You have purchased a Honda Civic.", image = honda)
                                                        savings -= 10000 #subtracts purchase value from savings counter 
                                                else:
                                                        a.msgbox("You do not have enough money to buy this car.")
                                        if cpick1 == cchoice1[1]:
                                                if savings >= 15000:
                                                        toyota = ["rav4.gif"]
                                                        a.msgbox("You have purchased a Toyota Rav4.", image = toyota)
                                                        savings -= 15000
                                                else:
                                                        a.msgbox("You do not have enough money to buy this car.")
                                        if cpick1 == cchoice1[2]:
                                                if savings >= 25000:
                                                        bmw = ["m5.gif"]
                                                        a.msgbox("You have purchased a BMW M5.", image = bmw)
                                                        savings -= 25000
                                                else:
                                                        a.msgbox("You do not have enough money to buy this car.")
                                        if cpick1 == cchoice1[3]:
                                                if savings >= 40000:
                                                        rover = ["range.gif"]
                                                        a.msgbox("You have purchased a Range Rover.", image = rover)
                                                        savings -= 40000
                                                else:
                                                        a.msgbox("You do not have enough money to buy this car.")
                                        if cpick1 == cchoice1[4]:
                                                if savings >= 100000:
                                                        benz = ["benz.gif"]
                                                        a.msgbox("You have purchased the Mercedes Benz S-Class.", image = benz)
                                                        savings -= 100000
                                                else:
                                                        a.msgbox("You do not have enough money to buy this car.")
                                        if cpick1 == cchoice1[5]:
                                                if savings >= 1000000:
                                                        chiron = ["chiron.gif"]
                                                        a.msgbox("You have purchased the Bugatti Chiron.", image = chiron)
                                                        savings -= 1000000
                                                else:
                                                        a.msgbox("You do not have enough money to buy this car.")        
                                        
                                if fpick1 == fchoice1[3]: #play lottery
                                        a.msgbox("You buy a lottery ticket.")
                                        saving -= 500 #costs money, user cannot keep playing 
                                        import random #random chance of winning lottery
                                        lotchance = random.randint(1, 1000)
                                        if lotchance == 69 or lotchance == 666: #low chance
                                                a.msgbox("You have won the lottery!!!!")
                                                savings += 15000000 #adds money if they win 
                                        else:
                                                a.msgbox("You do not win the lottery.")
                                if fpick1 == fchoice1[4]: #relationships 
                                        rchoice1 = ["Hang out with friends", "Find a Date", "Breakup with your Significant Other"]
                                        rpick1 = a.choicebox("Here are the options:", "", rchoice1) # r = relationship 
                                        if rpick1 == rchoice1[0]:
                                                import random
                                                friendact = random.randint(1, 5) #chooses between different possible activities 
                                                if friendact == 1:
                                                        a.msgbox("You go bowling with your friends.")
                                                if friendact == 2:
                                                        a.msgbox("You have drinks with your friends.")
                                                if friendact == 3:
                                                        a.msgbox("You eat dinner with your friends.")
                                                if friendact == 4:
                                                        a.msgbox("You go clubbing with your friends.")
                                                else:
                                                        a.msgbox("You watch a movie with your friends.")
                                        if rpick1 == rchoice1[1]:
                                                if date > 1: #if looking for date, if counter is above 1 it means they are already dating, and must break up 
                                                        a.msgbox("You are already dating someone.")
                                                else: #if not dating anyone 
                                                        if gendpick == gend[1]: #if user is female 
                                                                import random
                                                                guy = random.randint(1, 5) #different scenerios to find a date 
                                                                if guy == 1:
                                                                        a.msgbox("You meet Mark while at the mall. You guys have a lot in common.")
                                                                        gchoice1 = ["Yes", "No"] 
                                                                        gpick1 = a.buttonbox("Do you ask him out?", "", gchoice1 )
                                                                        if gpick1 == gchoice1[0]:
                                                                                import random
                                                                                yeschance = random.randint(1, 2) #chance of saying yes  
                                                                                if yeschance == 1:
                                                                                        a.msgbox("He says yes. You are now dating.")
                                                                                        date += 3 #if you start dating, counter increases in order to keep track 
                                                                                else:
                                                                                        a.msgbox("He rejects you.")
                                                                        else:
                                                                                a.msgbox("You do not ask him out.")
                                                                                            
                                                                if guy == 2: 
                                                                        a.msgbox("You meet a guy named Rohan while walking through the park. You guys hit it off.")
                                                                        gchoice1 = ["Yes", "No"]
                                                                        gpick1 = a.buttonbox("Do you ask him out?", "", gchoice1 )
                                                                        if gpick1 == gchoice1[0]:
                                                                                import random
                                                                                yeschance = random.randint(1, 2)
                                                                                if yeschance == 1:
                                                                                        a.msgbox("He says yes. You are now dating.")
                                                                                        date += 3
                                                                                else:
                                                                                        a.msgbox("He rejects you.")
                                                                        else:
                                                                                a.msgbox("You do not ask him out.")
                                                                if guy == 3:
                                                                        a.msgbox("You meet Jamal while at a resturant. You guys text for a bit and become good friends.")
                                                                        gchoice1 = ["Yes", "No"]
                                                                        gpick1 = a.buttonbox("Do you ask him out?", "", gchoice1 )
                                                                        if gpick1 == gchoice1[0]:
                                                                                import random
                                                                                yeschance = random.randint(1, 2)
                                                                                if yeschance == 1:
                                                                                        a.msgbox("He says yes. You are now dating.")
                                                                                        date += 3
                                                                                else:
                                                                                        a.msgbox("He rejects you.")
                                                                        else:
                                                                                a.msgbox("You do not ask him out.")
                                                                if girl == 4:
                                                                        a.msgbox("You meet Wu while jogging. You go on a run together and have a good time.")
                                                                        gchoice1 = ["Yes", "No"]
                                                                        gpick1 = a.buttonbox("Do you ask him out?", "", gchoice1 )
                                                                        if gpick1 == gchoice1[0]:
                                                                                import random
                                                                                yeschance = random.randint(1, 2)
                                                                                if yeschance == 1:
                                                                                        a.msgbox("He says yes. You are now dating.")
                                                                                        date += 3
                                                                                else:
                                                                                        a.msgbox("He rejects you.")
                                                                        else:
                                                                                a.msgbox("You do not ask him out.")         
                                                                if girl == 5:
                                                                        a.msgbox("Jacob is your friends ex-boyfriend. You two run into each other at a club and take a liking to one another.")
                                                                        gchoice1 = ["Yes", "No"]
                                                                        gpick1 = a.buttonbox("Do you ask him out?", "", gchoice1 )
                                                                        if gpick1 == gchoice1[0]:
                                                                                a.msgbox("He says yes. You are now dating.")
                                                                                date += 3
                                                                                a.msgbox("Your friend is mad at you. She no longer talks to you.")
                                                                                
                                                                        else:
                                                                                a.msgbox("You do not ask him out.")
                                                                        
                                                        if gendpick == gend[0]: #if user is male
                                                                import random
                                                                girl = random.randint(1, 5)
                                                                if girl == 1:
                                                                        a.msgbox("You meet Ashley while at the mall. You guys have a lot in comman.")
                                                                        gchoice1 = ["Yes", "No"]
                                                                        gpick1 = a.buttonbox("Do you ask her out?", "", gchoice1 )
                                                                        if gpick1 == gchoice1[0]:
                                                                                import random
                                                                                yeschance = random.randint(1, 2)
                                                                                if yeschance == 1:
                                                                                        a.msgbox("She says yes. You are now dating.")
                                                                                        date += 3
                                                                                else:
                                                                                        a.msgbox("She rejects you.")
                                                                        else:
                                                                                a.msgbox("You do not ask her out.")
                                                                                            
                                                                if girl == 2:
                                                                        a.msgbox("You meet a girl name Cathy while walking through the park. You guys hit it off.")
                                                                        gchoice1 = ["Yes", "No"]
                                                                        gpick1 = a.buttonbox("Do you ask her out?", "", gchoice1 )
                                                                        if gpick1 == gchoice1[0]:
                                                                                import random
                                                                                yeschance = random.randint(1, 2)
                                                                                if yeschance == 1:
                                                                                        a.msgbox("She says yes. You are now dating.")
                                                                                        date += 3
                                                                                else:
                                                                                        a.msgbox("She rejects you.")
                                                                        else:
                                                                                a.msgbox("You do not ask her out.")
                                                                if girl == 3:
                                                                        a.msgbox("You meet Requisha while at a resturant. You guys text for a bit and become good friends.")
                                                                        gchoice1 = ["Yes", "No"]
                                                                        gpick1 = a.buttonbox("Do you ask her out?", "", gchoice1 )
                                                                        if gpick1 == gchoice1[0]:
                                                                                import random
                                                                                yeschance = random.randint(1, 2)
                                                                                if yeschance == 1:
                                                                                        a.msgbox("She says yes. You are now dating.")
                                                                                        date += 3
                                                                                else:
                                                                                        a.msgbox("She rejects you.")
                                                                        else:
                                                                                a.msgbox("You do not ask her out.")
                                                                if girl == 4:
                                                                        a.msgbox("You meet Simran while jogging. You go on a run together and have a good time.")
                                                                        gchoice1 = ["Yes", "No"]
                                                                        gpick1 = a.buttonbox("Do you ask her out?", "", gchoice1 )
                                                                        if gpick1 == gchoice1[0]:
                                                                                import random
                                                                                yeschance = random.randint(1, 2)
                                                                                if yeschance == 1:
                                                                                        a.msgbox("She says yes. You are now dating.")
                                                                                        date += 3
                                                                                else:
                                                                                        a.msgbox("She rejects you.")
                                                                        else:
                                                                                a.msgbox("You do not ask her out.")         
                                                                if girl == 5:
                                                                        a.msgbox("Susan is your friends ex-girlfriend. You two run into each other at a club and take a liking to one another.")
                                                                        gchoice1 = ["Yes", "No"]
                                                                        gpick1 = a.buttonbox("Do you ask her out?", "", gchoice1 )
                                                                        if gpick1 == gchoice1[0]:
                                                                                a.msgbox("She says yes. You are now dating.")
                                                                                date += 3
                                                                                a.msgbox("Your friend is mad at you. He no longer talks to you.")
                                                                                
                                                                        else:
                                                                                a.msgbox("You do not ask her out.")
                                                                        

                                        if rpick1 == rchoice1[2]: #breakup with significant other 
                                                if date > 1: #if counter is greater than 1, it means you are dating someone 
                                                        a.msgbox("You break up with your significant other.")
                                                        date -= 3 #sets counter to zero so program knows you are single 
                                                        import random
                                                        killc = random.randint(1, 10) #chance regarding how significant other takes it 
                                                        if killc == 10:
                                                                a.msgbox("They attack you. You escape and sue them. You get 10,000 dollars.")
                                                                savings += 10000 #adds the money to savings 
                                                        else:
                                                                a.msgbox("You part peacefully.")
                                                else: #if not dating someone 
                                                        a.msgbox("You are not dating someone. Go find a date.")
                                                
                                

                        if fepick1 == fe1[1]: #choose to age 1 year
                                if job == 15: #adds yearly savings to counter, varies based on job level.This is why certain jobs added different amounts to counter
                                        savings += 30000 #if High paying job (ex: Engineer)
                                if job == 10:
                                        savings += 20000 #medium paying job 
                                if job == 5:
                                        savings += 10000 #low paying job (ex: Fast Food Worker)
                                age += 1 #adds to age counter 
                                a.msgbox("You are now " + str(age) + ". You have " + str(savings) + " dollars.") #tells user their age and amount of money they have 
                                #at certain ages, different events will take place, these are programmed below 
                                if age == 30:
                                        a.msgbox("You meet up with some old highschool friends. You have a good time.")

                                if age == 32:
                                        a.msgbox("While at a baseball game, Someone throws their drink at you.")
                                        mchoice1 = ["Assault them", "Forgive and Forget"] # m = miscellaneous
                                        mpick1 = a.buttonbox("What do you do?", "", mchoice1 )
                                        if mpick1 == mchoice1[0]:
                                                a.msgbox("You punched them in the head. You got kicked out of the game.")
                                        if mpick1 == mchoice1[1]:
                                                a.msgbox("You forgave them. You made a new friend in the end.")

                                if age == 34:
                                        a.msgbox("You get the flu.")
                                        import random
                                        flud = random.randint(1, 10) #chance of death
                                        if flud== 10:
                                                a.msgbox("You have died from the flu.")
                                                w = False
                                                break
                                        else:
                                                a.msgbox("You have made a full recovery.")

                                if age == 36:
                                        a.msgbox("While walking around, You find someones wallet.")
                                        mchoice2 = ["Take it", "Return to Owner"]
                                        mpick2 = a.buttonbox("What do you do?", "", mchoice2 )
                                        if mpick2 == mchoice2[0]:
                                                a.msgbox("You decide to take the money.")
                                        if mpick2 == mchoice2[1]:
                                                a.msgbox("You return the wallet to the owner.")

                                if age == 38:
                                        a.msgbox("You get promoted at your job.")
                                        savings += 10000 #bonus

                                if age == 40:
                                        import random
                                        teamw = random.randint(1, 2) #in honour of the raptors 
                                        if teamw == 1:
                                                a.msgbox("Your favourite basketball team wins the national championship.")
                                        else:
                                                a.msgbox("Your favourite basketball team loses in the final of the national championship.")
                                if age == 42:
                                        a.msgbox("While on your way to the airport, some random guy tells you that he will give you 100 000 dollars to take a strange package with you.")
                                        mchoice3 = ["Take it", "Refuse"]
                                        mpick3 = a.buttonbox("What do you do?", "", mchoice3 )
                                        if mpick3 == mchoice3[0]:
                                                a.msgbox("You agree to take the package.")
                                                a.msgbox("You are busted with 10 pounds of candy at the airport.")
                                                a.msgbox("You are sentencd to 10 years in prison.")
                                                a.msgbox("You die in prison during a fight.")
                                                w = False
                                                break
                                        if mpick3 == mchoice3[1]:
                                                a.msgbox("You leave the package.")
                                        
                                if age == 44:
                                        a.msgbox("Your mom invites you to brunch.")
                                        mchoice4 = ["Go", "Say you are busy"]
                                        mpick4 = a.buttonbox("Do you go?", "", mchoice4 )
                                        if mpick4== mchoice4[0]:
                                                a.msgbox("You have a good time with your mom.")
                                        if mpick4 == mchoice4[1]:
                                                a.msgbox("Your mom is sad. Your mom dies from depression.")
                                        
                                if age == 46:
                                        a.msgbox("Your idol basketball player, Kawhi Leonard, stays with your team.") #in honour of the MVP, please stay

                                if age == 48:
                                        a.msgbox("You are suffering from the gout.")
                                        

                                if age == 50:
                                        a.msgbox("You get promoted at your job.")
                                        savings += 10000 #bonus  

                                if age == 52:
                                        a.msgbox("You see a homeless man breaking the law.")
                                        mchoice5 = ["Report them", "Ignore it"]
                                        mpick5 = a.buttonbox("What do you do?", "", mchoice5 )
                                        if mpick5 == mchoice5[0]:
                                                a.msgbox("You report the homeless man. He assualts you.")
                                        if mpick5 == mchoice5[1]:
                                                a.msgbox("You ignore the law breaker.")

                                if age == 54:
                                        import random
                                        cancerchance = random.randint(1, 15)#chance of death
                                        if cancerchance == 10:
                                                a.msgbox("You have been diagnosed with cancer.")
                                                import random
                                                survchance = random.randint(1, 10)
                                                if 1 < survchance < 5:
                                                         a.msgbox("You have died from cancer.")
                                                         w = False
                                                         break
                                                else:
                                                        a.msgbox("You have beat cancer.")     

                                if age == 56:
                                        a.msgbox("You and your siblings have a good time hanging out at the lake.")

                                if age == 58:
                                        a.msgbox("Your newphew graduates from highschool.")

                                if age == 60:
                                        a.msgbox("You get promoted at your job.")
                                        savings += 10000 #bonus

                                if age == 62:
                                        import random
                                        cancerchance = random.randint(1, 15)
                                        if cancerchance == 10:
                                                a.msgbox("You have been diagnosed with hepatitis A.")
                                                import random
                                                survchance = random.randint(1, 10) #chance of death 
                                                if 1 < survchance < 5:
                                                         a.msgbox("You have died from hepatitis A.")
                                                         w = False
                                                         break
                                                else:
                                                        a.msgbox("You have beat hepatitis A.")
                                        
                        
                                if age == 64:
                                        a.msgbox("You find a mysterious bag of candy.")
                                        mchoice6 = ["Consume it", "Leave it alone"]
                                        mpick6 = a.buttonbox("What do you do?", "", mchoice6 )
                                        if mpick6 == mchoice6[0]:
                                                a.msgbox("You eat all of the candy.")
                                                a.msgbox("You die from diabetes.")
                                                w = False
                                                break
                                        if mpick6 == mchoice6[1]:
                                                a.msgbox("You walk away from the bag.")


                if age >= 65: #at 65 
                        a.msgbox("Wow, you made it to 65! You retire peacefully. Time to enjoy life.")
                        a.msgbox("Wait, you didn't start a retirement savings fund, did you?") #end twist 
                        w = False 
                        break
        while w == False: #after person dies
                a.msgbox("Thank you for playing Life simulator.")
                a.msgbox('''This game is designed by Asad Rehman. Thank you
                          for playing.''')
                endgame = ["Play Again", "Quit"]
                final = a.buttonbox("What would you like to do?", "", endgame)
                if final == endgame[0]:
                        start() #if play again, restarts function 
                        
                if final == endgame[1]:
                        quit()

start() #starts function when code is first launched 
                        








        
                        

                                




