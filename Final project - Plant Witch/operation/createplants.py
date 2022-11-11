# https://www.geeksforgeeks.org/calling-a-super-class-constructor-in-python/ this is where I read about subclasses.  This site did not suggest the "subclass" part in the 
# constructor init though. That was this tool. 
 

class plants():
    def __init__(self,  name='', quantity=int, sun='full', drainage='high', water='', bed='', seasonality='perrenial', storage='', fert ='', sow_time='', sow_loc='',
                 sow_depth='', sow_space='', p_height='', germ_time='', notes=''): 
        self.name = name
        self.quantity = quantity
        self.sun = sun
        self.drainage = drainage 
        self.water = water
        self.bed = bed
        self.seasonality = seasonality
        self.storage = storage
        self.fert = fert
        self.sow_time = sow_time
        self.sow_loc = sow_loc
        self.sow_depth = sow_depth
        self.sow_space = sow_space
        self.height = p_height 
        self.germ_time = germ_time       
        self.notes = notes        
        
#CONTROL + H DOES FIND AND REPLACE

class herbs(plants):
    def __init__(self, name='', quantity=int, sun='full', drainage='high', water='', bed='', seasonality='perrenial', smoke='N', burn='Y', edible='Y', storage='', fert='',
                 sow_time='', sow_loc='', sow_depth='', sow_space='', p_height='', germ_time='', notes=''):
        plants.__init__(self, name, quantity, sun, drainage, water, bed, seasonality, storage, fert, sow_time, sow_loc, sow_depth, sow_space, p_height, germ_time, notes,)

        self.smoke = smoke
        self.burn = burn
        self.edible = edible
        

class vegetables(plants):
    def __init__(self, name='', quantity=int, sun='full', drainage='moderate', water='daily', bed='', seasonality='perrenial', storage='', reap='', fert='', sow_time='', 
                 sow_loc='', sow_depth='', sow_space='', p_height='', germ_time='', notes = ''):
        plants.__init__(self, name, quantity, sun, drainage, water, bed, seasonality, storage, fert, sow_time, sow_loc, sow_depth, sow_space, p_height, germ_time, notes)
    
        self.reap= reap
        
     

class flowers(plants):
    def __init__(self, name='', quantity=int, color='', safety='', sun='full', drainage='moderte', water='daily', bed='', seasonality='', storage='', smoke='N', burn='', 
                edible='', fert='', sow_time='', sow_loc='', sow_depth='', sow_space='', p_height='', germ_time='', notes=''):
        plants.__init__(self, name, quantity, sun, drainage, water, bed, seasonality, storage, fert, sow_time, sow_loc, sow_depth, sow_space, p_height, germ_time, notes)

        self.color = color
        self.safety= safety
        self.smoke = smoke
        self.burn = burn
        self.edible = edible
           

# solicits user input on the plants
plant_names = []
herb_deets = []
veg_deets = []
flower_deets = []
def getuserresponse():
    QN = input('What is the plant name? enter "done" if finished: ') 
    while QN != 'done':
        Q = input('How many' + QN + ' do you have current?: ')
        QS = input('How much sun does' + QN + ' need?: ')
        QDr= input('Does ' + QN + ' need low, moderate, or high drainage?: ')
        QW= input('What are the water needs for ' + QN + ' ?: ')
        QB = input('What bed is ' + QN + ' in?: ')
        QSe = input('What is the seasonality of ' + QN + ' ?: ')
        QF = input('What are the fertlization needs of ' + QN + ' ?: ')
        QTm = input('When do you sow ' + QN + ' ?: ')
        QL = input('Do you sow ' + QN + ' indoors or in ground?: ')
        QDp = input('How deep do you sow ' + QN + ' ?: ')
        QSp = input('What is the plant spacing for ' + QN + ' ?: ')
        QH = input('How tall does ' + QN + ' get?: ')
        QG = input('How long does it take for ' + QN + ' to germinate?: ')
        QN = input('Please enter any additional notes about ' + QN + ' here.: ')
        QT = input('Is ' + QN + ' an herb, vegetable, or flower?: ')
    while QT == 'herb':
        QBr = input('Can you use ' + QN + ' for smudge?: ')
        QSm = input('Can you smoke ' + QN + ' ?: ')
        QE = input('Is ' + QN + ' edible?:')
    while QT == 'vegetable':
        QR = input('When do you harvest ' + QN + '?: ')
    while QT == 'flower':
        QC = input('What colors are ' + QN + ' ?: ')
        QSf = input('Is ' + QN + ' poisonous?: ')
        QSm_f = input('Can you smoke ' + QN + ' ?: ')
        QBr_f = input('Can you use ' + QN + ' for smudge?: ')
        QE_f = input('Is ' + QN + ' edible?:')



    
        plant_names.append(plants(QN, Q, QS, QDr, QW, QB, QSe, QF, QTm, QL, QDp, QSp, QH, QG, QN, QT))
        herb_deets.append(herbs(QBr, QSm, QE))
        veg_deets.append(vegetables(QR))
        flower_deets.append(flowers(QC, QSf, QSm_f, QBr_f, QE_f))
        QN = input('What is the plant name?:') 

    
    
# writes the user input/class data to a file        
def save_plants():
    f = open('../data/plants.txt', 'a')
    f.write('store plant data here\n')
    getuserresponse() 

    for p in plants:
        f.write(p.name) #repeat for other properties
        f.write(p.quantity)
        f.write(p.sun)
        f.write(p.drainage)
        f.write(p.water)
        f.write(p.bed)
        f.write(p.seasonality)
        f.write(p.storage)
        f.write(p.fert)
        f.write(p.sow_time)
        f.write(p.sow_loc)
        f.write(p.sow_depth)
        f.write(p.sow_space)
        f.write(p.p_height)
        f.write(p.germ_time)
        f.write(p.notes)

    for h in herbs:
        f.write(h.smoke)
        f.write(h.burn)
        f.write(h.edible)
       
    for v in vegetables:
        f.write(v.reap)

    for fl in flowers:
        f.write(fl.color)
        f.write(fl.safety)
        f.write(fl.smoke)
        f.write(fl.burn)
        f.write(fl.edible)