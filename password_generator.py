from tkinter import *
import random
import time

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
capital_letters = [letter.upper() for letter in small_letters]
numerical_characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '-', '=', '+', "/"]
substitutions = {
    'a':    ['4', '@', 'a'],
    'b':    ['6','8', '13', 'b'],
    'c':    ['<', '(', 'c'],
    'e':    ['3', 'e'],
    'g':    ['6', '&', '9', 'g'],
    'i':    ['!', '1', 'i'],
    'l':    ['!', '1', 'l'],
    'o':    ['0', '()', 'o'],
    'r':    ['12', 'r'],
    's':    ['$', '5', 's'],
    't':    ['7', 't'],
    'x':    ['%', 'x'],
    'z':    ['7_', '2', 'z']
}

def generate():
    output['state']= NORMAL
    selected = str(small.get()) + str(capital.get()) + str(num.get()) + str(sym.get())
    characters=[]
    global password
    password = ""
    output.delete(0, END)

    if selected[0]=='1':
        characters= characters + small_letters

    if selected[1]=='1':
        characters= characters + capital_letters

    if selected[2]=='1':
        characters= characters + numerical_characters

    if selected[3]=='1':
        characters= characters + symbols

    x=len(characters)-1
    random.seed(time.time())

    for _ in range(int(password_length.get())):
        password = password + characters[random.randint(0, x)]
    
    cover()
    copy_button['state']=NORMAL

def activate():
    active=int(small.get()) + int(capital.get()) + int(num.get()) + int(sym.get())
    if active:
        generate_button['state']=NORMAL
    
    else:
        generate_button['state']=DISABLED

def cover():
    try:
        output['state']= NORMAL
        display= password
        if int(hide.get()):
            output.delete(0, END)
            for i in range(len(display)):
                    display = display.replace(display[i], '*')
            output.insert(0, display)
            output['state']= DISABLED
        else:
            output.delete(0, END)
            output.insert(0, display)
    except:
        pass
    
def copy():
    main.clipboard_clear()
    main.clipboard_append(password)

def translate():
    pattern = insert_pattern_field.get()
    translated_pattern=""
    for letter in pattern:
        random.seed(time.time())
        if letter.lower() in substitutions:
            letter=letter.lower()
            translation = substitutions[letter]
            index = random.randint(0, len(translation)-1)
            translated_pattern+=translation[index]

        else:
            translated_pattern+=letter
    insert_pattern_field.delete(0, END)
    insert_pattern_field.insert(0, translated_pattern)

main = Tk()

small, capital, num, sym, hide= IntVar(), IntVar(), IntVar(), IntVar(), IntVar()
check_small = Checkbutton(main, text="Includes small letters", variable= small, command=activate)
check_capital = Checkbutton(main, text="Includes capital letters", variable= capital, command=activate)
check_numbers = Checkbutton(main, text="Includes numbers", variable= num, command=activate)
check_symbols = Checkbutton(main, text="Includes symbols", variable= sym, command=activate)
check_hidden = Checkbutton(main, text="Hide password", variable= hide, command=cover)
var = DoubleVar(value=8)
label = Label(text="Password length:")
password_length = Spinbox(main, from_=3, to=20, textvariable=var,)
generate_button = Button(main, text="Generate Password!", command=generate, state=DISABLED)
output = Entry(main, state=DISABLED, cursor="arrow")
copy_button = Button(main, text="Copy", command=copy, state=DISABLED)
insert_pattern_field = Entry(main)
test_button = Button(main, text="Translate pattern", command=translate)

check_small.pack()
check_capital.pack()
check_numbers.pack()
check_symbols.pack()
check_hidden.pack()
label.pack()
password_length.pack()
generate_button.pack()
output.pack()
copy_button.pack()
insert_pattern_field.pack()
test_button.pack()

main.mainloop()