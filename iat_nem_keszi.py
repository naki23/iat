# a next() készítése közben rájöttem hogy azt nem gondoltam végig és mivel már enélkül is túl bonyolult volt ezért inkább az egyszerűbb módot választottam amivel viszont a többieknek is kell dolgoznia
import tkinter as tk
from PIL import ImageTk
from PIL import Image
import time
import os
root = tk.Tk()

#import
imgs = []
fek = []
feh = []
cuk = []
bog = []
next_img = []
num = 0
while num < 7:
    try:
        imgs.append(ImageTk.PhotoImage(Image.open(os.getcwd() +"\\imgs\\" + str(num) + ".png")))
    except:
        pass
    #fek.append(ImageTk.PhotoImage(Image.open(os.getcwd() +"\\fek\\" + str(num) + ".png")))
    #feh.append(ImageTk.PhotoImage(Image.open(os.getcwd() +"\\feh\\" + str(num) + ".png")))
    cuk.append(ImageTk.PhotoImage(Image.open(os.getcwd() +"\\cuk\\emlos" + str(num) + ".png")))
    bog.append(ImageTk.PhotoImage(Image.open(os.getcwd() +"\\bog\\rovar" + str(num) + ".png")))
    try:
        next_img.append(ImageTk.PhotoImage(Image.open(os.getcwd() +"\\next_img\\" + str(num) + ".png")))
    except:
        pass
    num += 1
shown = next_img[0]

#initialize
time_ = []
saved_time = 0
l_0 = [next_img[0]]
l_1 = [cuk[2], cuk[6], bog[1], bog[2], bog[3], cuk[4], bog[6], cuk[1], cuk[5], bog[4], bog[5], cuk[3]]
l_2 = []
l_3 = []
l_4 = []
c_section = 0 # talán nem kell
img_list = [l_0, l_1, l_2, l_3, l_4]
c_img_list = 0
key_pressed = ''
global_img_num = 0
local_img_num = 0
d = {0:"'e'", 1:"'i'", 10:"'q'"} #correct answer
test_d = {2:"'e'", 3:"'i'"}
all_modes = [d, test_d]
#itt akartam vmit
c_dict = all_modes[0]


#default display
panel = tk.Label(root, image=next_img[0])
panel.pack(side="bottom", fill="both", expand="yes")


def callback(event):
    global saved_time
    global key_pressed
    time_.append(time.time()-saved_time)
    key_pressed = repr(event.keysym)
    print ("pressed:", (key_pressed))
    if check():
        print ("correct")
        next_()
    else:
        print('nem nyert')
        # error
    show_img(imgs[2])    
    time.sleep(0.4)
    try:
        show_img(shown)        
    except:
        print (fail)
        show_img(imgs[1])
    saved_time = time.time()
    print (time_)


def show_img(shownc):
    panel.configure(image=shownc)
    panel.image = shownc
    root.update()

def in_list(item, Tlist):
    for element in Tlist:
        if element == item:
            return True            
        else:
            pass
    return False

def melyik(item):
    if in_list(item, fek):
        return 0
    elif in_list(item, feh):
        return 1
    elif in_list(item, cuk):
        return 2
    elif in_list(item, bog):
        return 3
    elif in_list(item, next_img):
        return 10
    else:
        return -1

def check():
    print (melyik(shown))
    type_ = melyik(shown)
    print (c_dict)
    print (type_)
    if c_dict[type_] == key_pressed:
        return True
    else:
        return False

def next_():
    #based on cmode next or next mode
    global c_dict, shown, c_img_list
    c_section = all_modes.index(c_dict)
    if melyik(shown) == 10:
        print (c_dict)
        c_dict=all_modes[c_section+1]
        print (c_dict)
        print (c_img_list)
        c_img_list = img_list[c_section+1]
        print (c_img_list)
        c_section += 1
        local_img_num = 0
    else:
        shown = img_list[local_img_num+1]












def export():
    time.pop(0)
    data = [["initial_data"]+ initial_data, 
    ['wait between shown images'] + time,
    ['answer as expected?'] + correct]
    
    out_file = open('example2.csv', 'w', newline='')
    with out_file:
        writer = csv.writer(out_file, dialect='excel')
        writer.writerows(data)

    print("Writing complete")

#display 
root.bind("<Key>", callback)
root.mainloop()

""" 
append( diff prev vs time #done
correct? !!!
    based on index nope de megvan
time = prev done
wait done
next img !!!
mode????
    
"""