from pynput.keyboard import Key, Listener
import time
import pandas as pd

global start_time
global uni, bio, trio
global pre_symbol
global pre_sym_time
global pre_pre_symbol
global pre_pre_sym_time

pre_symbol = ''
pre_sym_time = 0
pre_pre_symbol = ''
pre_pre_sym_time = 0

uni = {"attempt": [i + 1 for i in range(15)],
       "'.'": [],
       "'t'": [],
       "'i'": [],
       "'e'": [],
       "'5'": [],
       "key.shift": [],
       "'r'": [],
       "'o'": [],
       "'a'": [],
       "'n'": [],
       "'l'": [],
       "key.enter": []}

bio = {"attempt": [i + 1 for i in range(15)],
       "'.'-'t'": [],
       "'t'-'i'": [],
       "'i'-'e'": [],
       "'e'-'5'": [],
       "'5'-key.shift": [],
       "key.shift-'r'": [],
       "'r'-'o'": [],
       "'o'-'a'": [],
       "'a'-'n'": [],
       "'n'-'l'": [],
       "'l'-key.enter": []}

trio = {"attempt": [i + 1 for i in range(15)],
        "'.'-'i'": [],
        "'t'-'e'": [],
        "'i'-'5'": [],
        "'e'-key.shift": [],
        "'5'-'r'": [],
        "key.shift-'o'": [],
        "'r'-'a'": [],
        "'o'-'n'": [],
        "'a'-'l'": [],
        "'n'-key.enter": []}


def press(key):
    global start_time
    global pre_symbol
    global pre_sym_time
    global pre_pre_symbol
    global pre_pre_sym_time

    print(f"{key} pressed")

    start_time = time.time()


def release(key):
    global start_time
    global pre_symbol
    global pre_sym_time
    global pre_pre_symbol
    global pre_pre_sym_time

    uni[str(key).lower()].append(time.time() - start_time)

    if pre_pre_symbol != '':
        trio[str(pre_pre_symbol).lower() + "-" + str(key).lower()].append(time.time() - pre_pre_sym_time)
        pre_pre_symbol = pre_symbol
        pre_pre_sym_time = pre_sym_time
    else:
        pre_pre_symbol = pre_symbol
        pre_pre_sym_time = pre_sym_time

    if pre_symbol != '':
        bio[str(pre_symbol).lower() + "-" + str(key).lower()].append(time.time() - pre_sym_time)
        pre_symbol = key
        pre_sym_time = start_time
    else:
        pre_symbol = key
        pre_sym_time = start_time

    if key == Key.enter:
        return False

    start_time = time.time()


for i in range(15):
    time.sleep(5)

    pre_symbol = ''
    pre_pre_symbol = ''

    with Listener(on_press=press, on_release=release) as listener:
        print(f"Input password attempt {i + 1}: ")
        start_time = time.time()
        listener.join()


print(uni)
print(bio)
print(trio)

df_uni = pd.DataFrame(uni)
df_bio = pd.DataFrame(bio)
df_trio = pd.DataFrame(trio)


df_uni.to_csv("Olshanyy_uni2.csv", index=False, encoding='utf-8')
df_bio.to_csv("Olshanyy_bio2.csv", index=False, encoding='utf-8')
df_trio.to_csv("Olshanyy_trio2.csv", index=False, encoding='utf-8')
