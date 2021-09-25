# !/user/bin/env Python3
# -*- coding:utf-8 -*-

import tkinter
from tkinter import filedialog
import os
import subprocess
import platform


def update_text():
    text_compare.update()
    text_compare.see(tkinter.END)


def setting_break():
    global is_break
    is_break = True


def open_random_file():
    global random_path, random_name, random_name_no_suffix, text_random
    random_path = filedialog.askopenfilename(
        title='Select input file', initialdir=(os.path.expanduser('H:/')))
    if random_path is not None:
        text_random.delete("1.0", "end")
        text_random.insert('1.0', random_path)
    random_name = os.path.split(random_path)[1]
    random_name_no_suffix = os.path.splitext(random_name)[0]


def open_source1_file():
    global source1_path, source1_name, source1_name_no_suffix, text_source1
    source1_path = filedialog.askopenfilename(
        title='Select first code file', initialdir=(os.path.expanduser('H:/')))
    if source1_path is not None:
        text_source1.delete("1.0", "end")
        text_source1.insert('1.0', source1_path)
    source1_name = os.path.split(source1_path)[1]
    source1_name_no_suffix = os.path.splitext(source1_name)[0]


def open_source2_file():
    global source2_path, source2_name, source2_name_no_suffix, text_source2
    source2_path = filedialog.askopenfilename(
        title='Select second code file', initialdir=(os.path.expanduser('H:/')))
    if source2_path is not None:
        text_source2.delete("1.0", "end")
        text_source2.insert('1.0', source2_path)
    source2_name = os.path.split(source2_path)[1]
    source2_name_no_suffix = os.path.splitext(source2_name)[0]


def deleteEXE():
    random = os.path.split(random_path)[0] + '/' + random_name_no_suffix
    source1 = os.path.split(source1_path)[0] + '/' + source1_name_no_suffix
    source2 = os.path.split(source2_path)[0] + '/' + source2_name_no_suffix

    if platform.system() == 'Windows':
        random = random + '.exe'
        source1 = source1 + '.exe'
        source2 = source2 + '.exe'

    if os.path.exists(random):
        os.remove(random)
    if os.path.exists(source1):
        os.remove(source1)
    if os.path.exists(source2):
        os.remove(source2)

    print(random)


def compileSource(file_path, file_name_no_suffix):
    text_compare.insert('end', '[BUILD]', 'PURPLE')
    text_compare.insert('end', ' Compiling ' + file_path + '... ')
    update_text()
    result = subprocess.call(
        ["g++", "-g", "-std=c++17", file_path, "-o", os.path.split(file_path)[0] + '/' + file_name_no_suffix], shell=False)
    if result == 0:
        text_compare.insert('end', 'done\n', 'GREEN')
        update_text()
        return 1
    else:
        text_compare.insert('end', 'failed\n', 'RED')
        update_text()
        return 0


def source_compare():
    if len(random_path) != 0 \
            and len(source1_path) != 0 \
            and len(source2_path) != 0:

        if compileSource(random_path, random_name_no_suffix) \
                and compileSource(source1_path, source1_name_no_suffix) \
                and compileSource(source2_path, source2_name_no_suffix):

            text_compare.insert('end', '\n')
            COUNTER = 0
            global is_break
            is_break = False

            while True:
                COUNTER += 1
                text_compare.insert('end', '[INFO] ', 'BLUE')
                text_compare.insert(
                    'end', 'Round ' + str(COUNTER) + ', comparing... ')
                update_text()

                subprocess_input = subprocess.run(
                    [os.path.split(random_path)[0] + '/' + random_name_no_suffix], stdout=subprocess.PIPE)
                subprocess_source1 = subprocess.run(
                    [os.path.split(source1_path)[0] + '/' + source1_name_no_suffix], input=subprocess_input.stdout, stdout=subprocess.PIPE)
                subprocess_source2 = subprocess.run(
                    [os.path.split(source2_path)[0] + '/' + source2_name_no_suffix], input=subprocess_input.stdout, stdout=subprocess.PIPE)

                if subprocess_source1.stdout.decode() != subprocess_source2.stdout.decode():
                    text_compare.insert('end', 'failed\n\n', 'RED')
                    text_compare.insert('end', '[ERROR] ', 'RED')
                    text_compare.insert('end', 'INPUT:\n', 'GRAY')
                    text_compare.insert(
                        'end', subprocess_input.stdout.decode() + '\n')
                    text_compare.insert('end', '[ERROR] ', 'RED')
                    text_compare.insert('end', source1_name_no_suffix)
                    text_compare.insert('end', ' OUTPUT:\n', 'GRAY')
                    text_compare.insert(
                        'end', subprocess_source1.stdout.decode() + '\n')
                    text_compare.insert('end', '[ERROR] ', 'RED')
                    text_compare.insert('end', source2_name_no_suffix)
                    text_compare.insert('end', ' OUTPUT:\n', 'GRAY')
                    text_compare.insert(
                        'end', subprocess_source2.stdout.decode() + '\n')
                    update_text()
                    break
                else:
                    text_compare.insert('end', 'done\n', 'GREEN')
                    text_compare.update()

                if is_break:
                    text_compare.insert('end', '\n[INFO] ', 'BLUE')
                    text_compare.insert(
                        'end', 'Comparison stopped, no differences have been found yet\n')
                    update_text()
                    break
        else:
            text_compare.insert('end', '[ERROR]', 'RED')
            text_compare.insert('end', ' There is something wrong...\n\n')
            update_text()
        deleteEXE()
    else:
        tkinter.messagebox.showerror(
            'Missing file', 'Make sure filling all file path', parent=window)


window = tkinter.Tk()
window.title('Output Comparator')
window.geometry('900x750')

devnull = open(os.devnull, 'w')
cxx_version = subprocess.run(["g++", "--version"], stdout=devnull)
if cxx_version.returncode != 0:
    tkinter.messagebox.showerror(
        'Missing C++ compiler', 'Make sure g++ is in your PATH', parent=window)
    exit(1)

random_path = ''
source1_path = ''
source2_path = ''

random_name = ''
source1_name = ''
source2_name = ''

random_name_no_suffix = ''
source1_name_no_suffix = ''
source2_name_no_suffix = ''

frame = tkinter.Frame(window)
frame.pack()

frame1 = tkinter.Frame(frame)
frame1.pack()
frame2 = tkinter.Frame(frame)
frame2.pack()
frame3 = tkinter.Frame(frame)
frame3.pack()
frame4 = tkinter.Frame(window)
frame4.pack()

button_random = tkinter.Button(
    frame1, text='Random data file', command=open_random_file, width=15)
button_source1 = tkinter.Button(
    frame2, text='First code file', command=open_source1_file, width=15)
button_source2 = tkinter.Button(
    frame3, text='Second code file', command=open_source2_file, width=15)
button_random.pack(side='left')
button_source1.pack(side='left')
button_source2.pack(side='left')

text_random = tkinter.Text(frame1, font=('Consolas', 12), height=1)
text_source1 = tkinter.Text(frame2, font=('Consolas', 12), height=1)
text_source2 = tkinter.Text(frame3, font=('Consolas', 12), height=1)
text_random.pack(side='right')
text_source1.pack(side='right')
text_source2.pack(side='right')

button_compare = tkinter.Button(
    frame4, text='Start', command=source_compare, width=10)
button_compare.pack(side='left')
button_compare_stop = tkinter.Button(
    frame4, text='Stop', command=setting_break, width=10)
button_compare_stop.pack(side='right')

text_compare = tkinter.Text(window, font=('Consolas', 12), height=30)
text_compare.pack()

text_compare.tag_config('PURPLE', foreground='PURPLE')
text_compare.tag_config('GREEN', foreground='GREEN')
text_compare.tag_config('RED', foreground='RED')
text_compare.tag_config('BLUE', foreground='BLUE')
text_compare.tag_config('GRAY', foreground='GRAY')

is_break = False

window.mainloop()
