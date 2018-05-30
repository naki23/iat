import tkinter as tk
from PIL import ImageTk
from PIL import Image
import time
import os
import csv
import sys
root = tk.Tk()

#import
correct = []
initial_data = []
kerdesek = ["Mennyire vallja magát előítéletesnek? (1-10)", "Van-e barátja/ismerőse/rokona aki cigány? i/n",] #"Szokott-e külföldre utazni? i/n"
correct_answ_list=["'space'", "'i'", "'e'","'e'","'e'","'i'","'e'","'i'","'i'","'e'","'e'","'i'","'i'", 
"'space'","'e'","'e'","'i'","'i'","'i'","'e'","'i'","'e'","'e'","'i'","'i'","'e'", 
"'space'","'e'","'e'","'e'","'i'","'i'","'e'","'e'","'i'","'i'","'e'","'e'","'e'","'i'","'e'","'i'","'i'","'e'","'i'","'i'","'i'","'i'","'e'","'i'","'e'",
"'space'","'i'","'i'","'e'","'e'","'e'","'i'","'e'","'i'","'e'","'i'","'e'","'i'",
"'space'","'i'","'e'","'i'","'e'","'i'","'e'","'i'","'e'","'e'","'i'","'e'","'e'","'i'","'e'","'e'","'i'","'i'","'e'","'i'","'i'","'i'","'e'","'i'", "'e'"]
fek = ['']
feh = ['']
cuk = ['']
bog = ['']
vez = ['']
next_img = []

num = 1
while num < 7:
    fek.append(ImageTk.PhotoImage(Image.open(os.getcwd() +"\\fek\\roma" + str(num) + ".png")))
    feh.append(ImageTk.PhotoImage(Image.open(os.getcwd() +"\\feh\\feherember" + str(num) + ".png")))
    cuk.append(ImageTk.PhotoImage(Image.open(os.getcwd() +"\\cuk\\emlos" + str(num) + ".png")))
    bog.append(ImageTk.PhotoImage(Image.open(os.getcwd() +"\\bog\\rovar" + str(num) + ".png")))
    try:
        vez.append(ImageTk.PhotoImage(Image.open(os.getcwd() +"\\vez\\" + str(num) + ".png")))
    except:
        pass
    try:
        next_img.append(ImageTk.PhotoImage(Image.open(os.getcwd() +"\\next_img\\" + str(num) + ".png")))
    except:
        pass
    num += 1
vez.append(ImageTk.PhotoImage(Image.open(os.getcwd() +"\\vez\\" + "7" + ".png")))
vez.append(ImageTk.PhotoImage(Image.open(os.getcwd() +"\\vez\\" + "8" + ".png")))
shown = next_img[0]
imgs = [vez[1], feh[5], fek[1], fek[6], fek[2], feh[3], fek[4], feh[2], feh[1], fek[5], fek[3], feh[6], feh[4],
vez[2], cuk[2], cuk[6], bog[1], bog[2], bog[3], cuk[4], bog[6], cuk[1], cuk[5], bog[4], bog[5], cuk[3],
vez[3], cuk[6], cuk[1], fek[1], feh[1], bog[1], fek[6], cuk[5], feh[6], feh[2], fek[3], cuk[4], fek[4], bog[5], cuk[2], feh[4], bog[3], fek[5], feh[1], feh[5], bog[6], bog[2], fek[2], bog[4], cuk[3], 
vez[4], fek[2], fek[5], feh[3], feh[5], feh[1], fek[1], feh[6], fek[6], feh[4], fek[4], feh[2], fek[3],
vez[5], fek[2], feh[3], fek[5], cuk[1], bog[2], cuk[5], bog[5], feh[6], feh[1], bog[4], feh[2], cuk[4], fek[1], cuk[3], cuk[2], fek[1], fek[4], feh[5], bog[6], bog[3], fek[3], cuk[6], bog[1], feh[4]]

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

#qs
for q in kerdesek:
    initial_data.append(input(q))
    #pass

#default display
panel = tk.Label(root, image=imgs[0])
panel.pack(side="bottom", fill="both", expand="yes")


def callback(event):
    global saved_time, key_pressed, global_img_num, correct_answ_list
    time_.append(time.time()-saved_time)
    print (global_img_num)
    key_pressed = repr(event.keysym)
    print ("pressed:", (key_pressed))
    show_img(vez[6])    
    time.sleep(0.4)
    if global_img_num ==0:
        shown = imgs[1]
    else:
        try: 
            shown = imgs[global_img_num+1]
        except:
            show_img(vez[8])
            print ("finished")
            correct.append("vege")
    if key_pressed == correct_answ_list[global_img_num]:
        correct.append(True)
        print ("jo")
    else:
        correct.append(False)
        show_img(vez[7])
        time.sleep(0.3)
        show_img(vez[6])    
        time.sleep(0.1)
        print ('nope')
    global_img_num += 1
    try:
        show_img(shown)                
    except:
        print ("fail")
        show_img(vez[6])
    saved_time = time.time()




def show_img(shownc):
    panel.configure(image=shownc)
    panel.image = shownc
    root.update()



""" nem kell már mert le egyszerusitem
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
        shown = img_list[local_img_num+1] """










def export(event):
    #time_.pop(0)
    data = [["kerdesekre valaszok"]+ initial_data, 
    ['idok'] + time_,
    ['jo válasz?'] + correct]

    run_num = 0
    while os.path.exists("%s_user_data.csv" % run_num):
        run_num += 1
    out_file = open("%s_user_data.csv" % run_num, 'w', newline='')
    with out_file:
        writer = csv.writer(out_file, dialect='excel')
        writer.writerows(data)

    print("Writing complete")
    root.destroy()
    print ("done", run_num)
    time.sleep(60)

    

#display 
root.bind("<Key>", callback)
root.bind("<Control-0>", export)
root.mainloop()

""" 
append( diff prev vs time #done
correct? 
    based on index #nope de megvan
time = prev #done
wait #done
next img !!!!!!!!
mode????!!!!!!!!!!
    
"""