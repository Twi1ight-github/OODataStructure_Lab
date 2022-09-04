print("*** TorKham HanSaa ***")
class Torkham:

    def __init__(self,word):
        self.worf = word
    
    def game(self,word):
        inGame=[]
        index = -1
        while 1: 
            index+=1
            
            if word[index][0] == "R" :
                inGame = []
                print("game restarted")
                continue
            elif word[index][0] == 'X':
                exit()
            elif word[index][0] == 'P':
                if index > 0 and len(word[index])>=4 and len(word[index-1])>=4:
                    if ord(word[index][2]) == ord(word[index-1][-2]) and ord(word[index][3]) == ord(word[index-1][-1]): #fisrt 2 letter and last 2 letter are same
                        inGame.append(word[index][2:])
                        print("'{}'".format(word[index][2:]) + " -> " + str(inGame))

                    elif ord(word[index][2]) == ord(word[index-1][-2])+32 and ord(word[index][3]) == ord(word[index-1][-1])+32:
                        inGame.append(word[index][2:])
                        print("'{}'".format(word[index][2:]) + " -> " + str(inGame))

                    elif ord(word[index][2]) == ord(word[index-1][-2])+32 and ord(word[index][3]) == ord(word[index-1][-1])-32:
                        inGame.append(word[index][2:])
                        print("'{}'".format(word[index][2:]) + " -> " + str(inGame))

                    elif ord(word[index][2]) == ord(word[index-1][-2])-32 and ord(word[index][3]) == ord(word[index-1][-1])-32:
                        inGame.append(word[index][2:])
                        print("'{}'".format(word[index][2:]) + " -> " + str(inGame))

                    elif ord(word[index][2]) == ord(word[index-1][-2])-32 and ord(word[index][3]) == ord(word[index-1][-1])+32:
                        inGame.append(word[index][2:])
                        print("'{}'".format(word[index][2:]) + " -> " + str(inGame))

                    else:
                        print("'{}'".format(word[index][2:]) + " -> game over")
                        exit()
                        
                else:
                    inGame.append(word[index][2:])
                    print("'{}'".format(word[index][2:]) + " -> " + str(inGame))

            else:
                print("'{}'".format(word[index]) + " is Invalid Input !!!")
                exit()
            



word = []
word = input("Enter Input : ").split(",")
torkham = Torkham(word)
torkham.game(word)


