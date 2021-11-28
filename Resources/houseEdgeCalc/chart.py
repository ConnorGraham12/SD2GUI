import tkinter as tk
from Resources.houseEdgeCalc.test2 import get_bs_stand_soft_17, get_bs_hit_soft_17
# hit_17_dict = get_bs_hit_soft_17()





iterate  = [('4', '2'), ('4', '3'), ('4', '4'), ('4', '5'), ('4', '6'), ('4', '7'), ('4', '8'), ('4', '9'), ('4', '10'),('4', 'J'), ('4', 'Q'), ('4', 'K'), ('4', 'A'), ('5', '2'), ('5', '3'), ('5', '4'), ('5', '5'), ('5', '6'), ('5', '7'), ('5', '8'), ('5', '9'), ('5', '10'),('5', 'J'), ('5', 'Q'), ('5', 'K'), ('5', 'A'), ('6', '2'), ('6', '3'), ('6', '4'), ('6', '5'), ('6', '6'), ('6', '7'), ('6', '8'), ('6', '9'), ('6', '10'),('6', 'J'), ('6', 'Q'), ('6', 'K'), ('6', 'A'), ('7', '2'), ('7', '3'), ('7', '4'), ('7', '5'), ('7', '6'), ('7', '7'), ('7', '8'), ('7', '9'), ('7', '10'),('7', 'J'), ('7', 'Q'), ('7', 'K'), ('7', 'A'), ('8', '2'), ('8', '3'), ('8', '4'), ('8', '5'), ('8', '6'), ('8', '7'), ('8', '8'), ('8', '9'), ('8', '10'),('8', 'J'), ('8', 'Q'), ('8', 'K'), ('8', 'A'), ('9', '2'), ('9', '3'), ('9', '4'), ('9', '5'), ('9', '6'), ('9', '7'), ('9', '8'), ('9', '9'), ('9', '10'),('9', 'J'), ('9', 'Q'), ('9', 'K'), ('9', 'A'), ('10', '2'),('10', '3'),('10', '4'),('10', '5'),('10', '6'),('10', '7'),('10', '8'),('10', '9'),('10', '10'),('10', 'J'),('10', 'Q'),('10', 'K'),('10', 'A'),('11', '2'),('11', '3'),('11', '4'),('11', '5'),('11', '6'),('11', '7'),('11', '8'),('11', '9'),('11', '10'),('11', 'J'),('11', 'Q'),('11', 'K'),('11', 'A'),('12', '2'),('12', '3'),('12', '4'),('12', '5'),('12', '6'),('12', '7'),('12', '8'),('12', '9'),('12', '10'),('12', 'J'),('12', 'Q'),('12', 'K'),('12', 'A'),('13', '2'),('13', '3'),('13', '4'),('13', '5'),('13', '6'),('13', '7'),('13', '8'),('13', '9'),('13', '10'),('13', 'J'),('13', 'Q'),('13', 'K'),('13', 'A'),('14', '2'),('14', '3'),('14', '4'),('14', '5'),('14', '6'),('14', '7'),('14', '8'),('14', '9'),('14', '10'),('14', 'J'),('14', 'Q'),('14', 'K'),('14', 'A'),('15', '2'),('15', '3'),('15', '4'),('15', '5'),('15', '6'),('15', '7'),('15', '8'),('15', '9'),('15', '10'),('15', 'J'),('15', 'Q'),('15', 'K'),('15', 'A'),('16', '2'),('16', '3'),('16', '4'),('16', '5'),('16', '6'),('16', '7'),('16', '8'),('16', '9'),('16', '10'),('16', 'J'),('16', 'Q'),('16', 'K'),('16', 'A'),('17', '2'),('17', '3'),('17', '4'),('17', '5'),('17', '6'),('17', '7'),('17', '8'),('17', '9'),('17', '10'),('17', 'J'),('17', 'Q'),('17', 'K'),('17', 'A'),('18', '2'),('18', '3'),('18', '4'),('18', '5'),('18', '6'),('18', '7'),('18', '8'),('18', '9'),('18', '10'),('18', 'J'),('18', 'Q'),('18', 'K'),('18', 'A'),('19', '2'),('19', '3'),('19', '4'),('19', '5'),('19', '6'),('19', '7'),('19', '8'),('19', '9'),('19', '10'),('19', 'J'),('19', 'Q'),('19', 'K'),('19', 'A'),('20', '2'),('20', '3'),('20', '4'),('20', '5'),('20', '6'),('20', '7'),('20', '8'),('20', '9'),('20', '10'),('20', 'J'),('20', 'Q'),('20', 'K'),('20', 'A'),('21', '2'),('21', '3'),('21', '4'),('21', '5'),('21', '6'),('21', '7'),('21', '8'),('21', '9'),('21', '10'),('21', 'J'),('21', 'Q'),('21', 'K'),('21', 'A')     ]
iterate2 = [('13', '2'),('13', '3'),('13', '4'),('13', '5'),('13', '6'),('13', '7'),('13', '8'),('13', '9'),('13', '10'),('13', 'J'),('13', 'Q'),('13', 'K'),('13', 'A'),('14', '2'),('14', '3'),('14', '4'),('14', '5'),('14', '6'),('14', '7'),('14', '8'),('14', '9'),('14', '10'),('14', 'J'),('14', 'Q'),('14', 'K'),('14', 'A'),('15', '2'),('15', '3'),('15', '4'),('15', '5'),('15', '6'),('15', '7'),('15', '8'),('15', '9'),('15', '10'),('15', 'J'),('15', 'Q'),('15', 'K'),('15', 'A'),('16', '2'),('16', '3'),('16', '4'),('16', '5'),('16', '6'),('16', '7'),('16', '8'),('16', '9'),('16', '10'),('16', 'J'),('16', 'Q'),('16', 'K'),('16', 'A'),('17', '2'),('17', '3'),('17', '4'),('17', '5'),('17', '6'),('17', '7'),('17', '8'),('17', '9'),('17', '10'),('17', 'J'),('17', 'Q'),('17', 'K'),('17', 'A'),('18', '2'),('18', '3'),('18', '4'),('18', '5'),('18', '6'),('18', '7'),('18', '8'),('18', '9'),('18', '10'),('18', 'J'),('18', 'Q'),('18', 'K'),('18', 'A'),('19', '2'),('19', '3'),('19', '4'),('19', '5'),('19', '6'),('19', '7'),('19', '8'),('19', '9'),('19', '10'),('19', 'J'),('19', 'Q'),('19', 'K'),('19', 'A'),('20', '2'),('20', '3'),('20', '4'),('20', '5'),('20', '6'),('20', '7'),('20', '8'),('20', '9'),('20', '10'),('20', 'J'),('20', 'Q'),('20', 'K'),('20', 'A'),('21', '2'),('21', '3'),('21', '4'),('21', '5'),('21', '6'),('21', '7'),('21', '8'),('21', '9'),('21', '10'),('21', 'J'),('21', 'Q'),('21', 'K'),('21', 'A')]
iterate3 = [('2', '2'),('2', '3'),('2', '4'),('2', '5'),('2', '6'),('2', '7'),('2', '8'),('2', '9'),('2', '10'),('2', 'J'),('2', 'Q'),('2', 'K'),('2', 'A'),('3', '2'),('3', '3'),('3', '4'),('3', '5'),('3', '6'),('3', '7'),('3', '8'),('3', '9'),('3', '10'),('3', 'J'),('3', 'Q'),('3', 'K'),('3', 'A'),('4', '2'),('4', '3'),('4', '4'),('4', '5'),('4', '6'),('4', '7'),('4', '8'),('4', '9'),('4', '10'),('4', 'J'),('4', 'Q'),('4', 'K'),('4', 'A'),('5', '2'),('5', '3'),('5', '4'),('5', '5'),('5', '6'),('5', '7'),('5', '8'),('5', '9'),('5', '10'),('5', 'J'),('5', 'Q'),('5', 'K'),('5', 'A'),('6', '2'),('6', '3'),('6', '4'),('6', '5'),('6', '6'),('6', '7'),('6', '8'),('6', '9'),('6', '10'),('6', 'J'),('6', 'Q'),('6', 'K'),('6', 'A'),('7', '2'),('7', '3'),('7', '4'),('7', '5'),('7', '6'),('7', '7'),('7', '8'),('7', '9'),('7', '10'),('7', 'J'),('7', 'Q'),('7', 'K'),('7', 'A'),('8', '2'),('8', '3'),('8', '4'),('8', '5'),('8', '6'),('8', '7'),('8', '8'),('8', '9'),('8', '10'),('8', 'J'),('8', 'Q'),('8', 'K'),('8', 'A'),('9', '2'),('9', '3'),('9', '4'),('9', '5'),('9', '6'),('9', '7'),('9', '8'),('9', '9'),('9', '10'),('9', 'J'),('9', 'Q'),('9', 'K'),('9', 'A'),('10', '2'),('10', '3'),('10', '4'),('10', '5'),('10', '6'),('10', '7'),('10', '8'),('10', '9'),('10', '10'),('10', 'J'),('10', 'Q'),('10', 'K'),('10', 'A'),('A', '2'),('A', '3'),('A', '4'),('A', '5'),('A', '6'),('A', '7'),('A', '8'),('A', '9'),('A', '10'),('A', 'J'),('A', 'Q'),('A', 'K'),('A', 'A'), ]


from tkinter import *
  
storageArray = [None] * 300
class Chart:

    def __init__(self, root, dict):
        if dict =="stand":
            # print("STAND")
            hit_17 = get_bs_stand_soft_17()
        if dict == "hit":
            # print("HIT")
            hit_17 = get_bs_hit_soft_17()
        hard_hands = hit_17['hard']
        soft_hands = hit_17['soft']
        pair_hands = hit_17['pair']
        hardFrame = tk.Frame(root)
        softFrame = tk.Frame(root)
        splitframe = tk.Frame(root)


        Chart.HardTable(hardFrame, hard_hands)
        Chart.SoftTable(softFrame, soft_hands)
        Chart.SplitTable(splitframe, pair_hands)
        hardFrame.pack()
        softFrame.pack()
        splitframe.pack()
    
    class HardTable:

        def __init__(self,root,hard_hands):

            item = 0
            count = 0
            for y in range(15):
                for x in range(14):
                    
                    temp = tk.Entry(root, width=3, fg='black',font=('arial',10,'bold'), justify='center',cursor="arrow")

                    if(y == 0):

                        msg = ['HARD','2','3','4','5','6','7','8','9','10','J', 'Q','K','A','X',"X"]
                        temp.insert('end', str(msg[x]))
                        temp.configure(bg = '#707070') 
                        if(x==0):
                            temp.configure(width=6)
                        
                    elif (x == 0 and y > 0):
                        msg = ['4','5','6','7','8','9','10','11', '12','13','14','15','16', '17+']
                        temp.insert('end', str(msg[y-1]))
                        temp.configure(bg = '#707070', width=6)   

                    else:
                        tmp = hard_hands[iterate[item]] 
                        if((str(tmp)) == "['HIT']"):
                            temp.insert('end', 'H')
                            temp.configure(bg = 'red')
                            
                        elif((str(tmp)) == "['STAND']"):
                            temp.insert('end', 'S')
                            temp.configure(bg = 'yellow')
                        elif((str(tmp)) == "['DOUBLE', 'HIT']"):
                            temp.insert('end', 'Dh')
                            temp.configure(bg = 'blue')
                        elif((str(tmp)) == "['SURRENDER', 'HIT']"):
                            temp.insert('end', 'Rh')
                            temp.configure(bg = 'white')
                        elif((str(tmp)) == "['SURRENDER', 'STAND']"):
                            temp.insert('end', 'Rs')
                            temp.configure(bg = 'white')
                        
                            
                        item += 1
                    storageArray[count] = temp 
                    count += 1  
                    temp.grid(row=y, column=x)    
    class SoftTable:

        def __init__(self,root,soft_hands):

            item = 0
            count = 0
            for y in range(9):
                for x in range(14):
                    
                    temp = tk.Entry(root, width=3, fg='black',font=('arial',10,'bold'), justify='center',cursor="arrow")

                    if(y == 0):

                        msg = ['SOFT','2','3','4','5','6','7','8','9','10','J', 'Q','K','A','X',"X"]
                        temp.insert('end', str(msg[x]))
                        temp.configure(bg = '#707070')
                        if(x==0):
                            temp.configure(width=6) 
                        
                    elif (x == 0 and y > 0):
                        msg = ['13','14','15','16', '17', '18', '19', '20+']
                        temp.insert('end', str(msg[y-1]))
                        temp.configure(bg = '#707070', width=6)   

                    else:
                        tmp = soft_hands[iterate2[item]]
                        
                        if((str(tmp)) == "['HIT']"):
                            temp.insert('end', 'H')
                            temp.configure(bg = 'red')
                            
                        elif((str(tmp)) == "['STAND']"):
                            temp.insert('end', 'S')
                            temp.configure(bg = 'yellow')
                        elif((str(tmp)) == "['DOUBLE', 'HIT']"):
                            temp.insert('end', 'Dh')
                            temp.configure(bg = 'blue')
                        elif((str(tmp)) == "['SURRENDER', 'HIT']"):
                            temp.insert('end', 'Rh')
                            temp.configure(bg = 'white')
                        elif((str(tmp)) == "['DOUBLE', 'STAND']"):
                            temp.insert('end', 'Ds')
                            temp.configure(bg = '#00ffff')
                        
                        
                        item += 1
                    storageArray[count] = temp 
                    count += 1  
                    temp.grid(row=y, column=x)    
    class SplitTable:

        def __init__(self,root,pair_hands):

            item = 0
            count = 0
            for y in range(11):
                for x in range(14):
                    
                    temp = tk.Entry(root, width=3, fg='black',font=('arial',10,'bold'), justify='center',cursor="arrow", takefocus='false')

                    if(y == 0):

                        msg = ['SPLIT','2','3','4','5','6','7','8','9','10','J', 'Q','K','A','X',"X"]
                        temp.insert('end', str(msg[x]))
                        temp.configure(bg = '#707070')
                        if(x==0):
                            temp.configure(width=6)
                        
                    elif (x == 0 and y > 0):
                        msg = ['2,2','3,3','4,4','5,5','6,6', '7,7', '8,8', '9,9','10,10', 'A,A']
                        temp.insert('end', str(msg[y-1]))
                        temp.configure(bg = '#707070', width=6)   

                    else:
                        tmp = pair_hands[iterate3[item]]
                        if((str(tmp)) == "['HIT']"):
                            temp.insert('end', 'H')
                            temp.configure(bg = 'red')
                            
                        elif((str(tmp)) == "['STAND']"):
                            temp.insert('end', 'S')
                            temp.configure(bg = 'yellow')
                        elif((str(tmp)) == "['DOUBLE', 'HIT']"):
                            temp.insert('end', 'Dh')
                            temp.configure(bg = 'blue')
                        elif((str(tmp)) == "['SURRENDER', 'HIT']"):
                            temp.insert('end', 'Rh')
                            temp.configure(bg = 'white')
                        elif((str(tmp)) == "['DOUBLE', 'STAND']"):
                            temp.insert('end', 'Ds')
                            temp.configure(bg = '#00ffff')
                        elif((str(tmp)) == "['SPLIT_DAS', 'HIT']"):
                            temp.insert('end', 'Ph')
                            temp.configure(bg = '#add8e6')
                        elif((str(tmp)) == "['SPLIT']"):
                            temp.insert('end', 'P')
                            temp.configure(bg = '#3EB489') 
                        elif((str(tmp)) == "['SPLIT', 'HIT']"):
                            temp.insert('end', 'S/H')
                            temp.configure(bg = '#ffb6c1') 
                        elif((str(tmp)) == "['SURRENDER', 'SPLIT']"):
                            temp.insert('end', 'Rs')
                            temp.configure(bg = '#76b5c5') 
                        # print(str(tmp))    
                        item = item + 1
                    storageArray[count] = temp 
                    count += 1  
                    temp.grid(row=y, column=x)  

# root = Tk()
# graphFrame = tk.Frame(root)
# hardFrame = tk.Frame(graphFrame)
# softFrame = tk.Frame(graphFrame)
# splitframe = tk.Frame(graphFrame)

# t = HardTable(hardFrame)
# t2 = SoftTable(softFrame)
# t3 = SplitTable(splitframe)

# hardFrame.pack()
# softFrame.pack()
# splitframe.pack()

# graphFrame.pack()



# root.mainloop()
                