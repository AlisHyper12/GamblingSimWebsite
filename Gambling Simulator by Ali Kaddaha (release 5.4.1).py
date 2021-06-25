import PySimpleGUI as sg
import random
import keyboard
import cv2 as cv
import time
import socket

sg.theme('SystemDefault1')

btndef = {'button_color': ('black', 'white')}
redbtn = {'size': (6, 2), 'button_color': ('white', 'red'), 'pad': ('0', '0')}
blackbtn = {'size': (6, 2), 'button_color': ('white', 'black'), 'pad': ('0', '0')}
greenbtn = {'size': (5, 2), 'button_color': ('white', 'green'), 'pad': ('0', '0')}
redbtnl = {'size': (5, 8), 'button_color': ('white', 'red'), 'pad': ('0', '0')}
greenbtnl = {'size': (5, 7), 'button_color': ('white', 'green'), 'pad': ('0', '0')}
greenbtnllh = {'size': (27, 2), 'button_color': ('white', 'green'), 'pad': ('0', '0')}
greenbtnlh = {'size': (13, 2), 'button_color': ('white', 'green'), 'pad': ('0', '0')}
redbtnlh = {'size': (13, 2), 'button_color': ('white', 'red'), 'pad': ('0', '0')}
blackbtnlh = {'size': (13, 2), 'button_color': ('white', 'black'), 'pad': ('0', '0')}

with open('.SaveData\\GamblingSimSaveData.txt', 'r') as SaveData:
    z = SaveData.read()

column_layout = [
    [sg.B('Bet on heads', key='bth', **btndef), sg.B('Bet on tails', key='btt', **btndef)]
]

frame_layout = [
    [sg.T('Balance: $', background_color='#D8D8D8'), sg.T(str(int(z)), key='bal', size=(100, 0), background_color='#D8D8D8')],
    [sg.T(' ', background_color='#D8D8D8')],
    [sg.T('$', background_color='#D8D8D8'), sg.I(key='inp', size=(5, 0))],
    [sg.T('Please enter an amount of money', key='error', visible=False, background_color='#D8D8D8'),
     sg.T('Not enough funds', key='notenough', visible=False, background_color='#D8D8D8')],
    [sg.Col(column_layout, key='btns', background_color='#D8D8D8')],
    [sg.T('Bankrupt', key='over', visible=False, background_color='#D8D8D8')],
    [sg.B('Restart', key='over1', visible=False, **btndef)]
]

with open('.SaveData\\GamblingSimSaveData.txt', 'r') as SaveData:
    SaveData = SaveData.read()
with open('.SaveData\\GamblingSimSaveData1.txt', 'r') as SaveData1:
    SaveData1 = SaveData1.read()
with open('.SaveData\\GamblingSimSaveData2.txt', 'r') as SaveData2:
    SaveData2 = SaveData2.read()

cheats = [
    [sg.T('Money: '), sg.I(str(SaveData), size=(5, 0), key='moners')],
    [sg.T(str(int(SaveData1)), key='rouletteunlocktion')],
    [sg.T(str(int(SaveData2)), key='slotmachineunlocktion')],
    [sg.B('Save', **btndef)]
]

roulette_frame = [
    [sg.T('Balance: $', background_color='#D8D8D8'), sg.T('0', key='balr', size=(100, 0), background_color='#D8D8D8')],
    [sg.T(' ', background_color='#D8D8D8')],
    [sg.T('$', background_color='#D8D8D8'), sg.I(key='inpr', size=(5, 0))],
    [sg.T('Please enter an amount of money', key='errorr', visible=False, background_color='#D8D8D8'),
     sg.T('Not enough funds', key='notenoughr', visible=False, background_color='#D8D8D8'),
     sg.T('Bankrupt', visible=False, key='overr', background_color='#D8D8D8')],
    [sg.B('Restart', **btndef, key='rrestart', visible=False)]
]

coinflip_tab = [
    [sg.T('Coin Flip', font=('Berlin Sans FB', 30), text_color='#ff0000', size=(355, 0), justification='center')],
    [sg.T(' ')],
    [sg.Frame('', frame_layout, background_color='#D8D8D8')],
    [sg.T('The coin landed on heads!', key='heads', visible=False, justification='center', size=(355, 0)),
     sg.T('The coin landed on tails!', key='tails', visible=False, justification='center', size=(355, 0))],
    [sg.Image(filename='.SaveData\\780px-2006_smallQuarter_Proof.png', visible=False, key='heads1'),
     sg.Image(filename='.SaveData\\780px-2006_smallQuarter_Proofheads.png', visible=False, key='tails1')],
    [sg.T('You won :D', key='win', visible=False, justification='center', size=(355, 0)),
     sg.T('You lost :(', key='loss', visible=False, justification='center', size=(355, 0))]
]

greenCol = [
    [sg.B('1st\nrow', **greenbtn)],
    [sg.B('2nd\nrow', **greenbtn)],
    [sg.B('3rd\nrow', **greenbtn)]
]

table1 = [
    [sg.B('3', **redbtn), sg.B('6', **blackbtn), sg.B('9', **redbtn), sg.B('12', **redbtn), sg.B('15', **blackbtn),
     sg.B('18', **redbtn), sg.B('21', **redbtn), sg.B('24', **blackbtn), sg.B('27', **redbtn), sg.B('30', **redbtn),
     sg.B('33', **blackbtn), sg.B('36', **redbtn)],
    [sg.B('2', **blackbtn), sg.B('5', **redbtn), sg.B('8', **blackbtn), sg.B('11', **blackbtn), sg.B('14', **redbtn),
     sg.B('17', **blackbtn), sg.B('20', **blackbtn), sg.B('23', **redbtn), sg.B('26', **blackbtn),
     sg.B('29', **blackbtn), sg.B('32', **redbtn), sg.B('35', **blackbtn)],
    [sg.B('1', **redbtn), sg.B('4', **blackbtn), sg.B('7', **redbtn), sg.B('10', **blackbtn), sg.B('13', **blackbtn),
     sg.B('16', **redbtn), sg.B('19', **redbtn), sg.B('22', **blackbtn), sg.B('25', **redbtn), sg.B('28', **blackbtn),
     sg.B('31', **blackbtn), sg.B('34', **redbtn)]
]

table2 = [
    [sg.B('1st 12', **greenbtnllh), sg.B('2nd 12', **greenbtnllh), sg.B('3rd 12', **greenbtnllh)],
    [sg.B('1 to 18', **greenbtnlh), sg.B('EVEN', **greenbtnlh), sg.B('RED', **redbtnlh), sg.B('BLACK', **blackbtnlh),
     sg.B('ODD', **greenbtnlh), sg.B('19 to 36', **greenbtnlh)]
]

table = [
    [sg.B('0', **greenbtnl), sg.Col(layout=table1, key='table1k'), sg.Col(greenCol, key='keycol', pad=(1, 0))],
    [sg.Col(table2, key='table2k', pad=(0, 1))]
]

roulette_frame_frame = [
    [sg.Frame('', roulette_frame, background_color='#D8D8D8', visible=False, key='inprf')],
    [sg.Col(table, visible=False, key='table', element_justification='center')],
]

wheel_col = [
    [sg.Image(filename='', key='videotest', size=(500, 500))],
    [sg.T('You won :D', visible=False, key='winr'), sg.T('You lost :(', visible=False, key='lossr')],
    [sg.T('The ball landed on', visible=False, key='landing', size=(100, 0))]
]

roulette_tab = [
    [sg.B('Unlock Roulette - $1,000 (Free if purchased previously)', key='rlu', **btndef),
     sg.T('Roulette unlocked!', visible=False, key='unlock'),
     sg.T('Roulette Simulator', font=('Berlin Sans FB', 30), text_color='#ff0000', size=(355, 0),
          justification='center', key='title', visible=False)],
    [sg.T('Not enough funds :(', key='fail', visible=False), sg.B("Let's start!", key='goto', visible=False)],
    [sg.B('Ok', key='ok', visible=False, **btndef)],
    [sg.Col(roulette_frame_frame), sg.Col(wheel_col, pad=(0, 1))]
]

slotmachine_balframe = [
    [sg.T('Balance: $', background_color='#D8D8D8'), sg.T('0', key='bals', size=(100, 0), background_color='#D8D8D8')],
    [sg.T(' ', background_color='#D8D8D8')],
    [sg.T('$', background_color='#D8D8D8'), sg.I(key='inps', size=(5, 0))],
    [sg.T('Please enter an amount of money', key='errors', visible=False, background_color='#D8D8D8'),
     sg.T('Not enough funds', key='notenoughs', visible=False, background_color='#D8D8D8'),
     sg.T('Bankrupt', visible=False, key='overs', background_color='#D8D8D8')],
    [sg.B('Restart', **btndef, key='srestart', visible=False)]
]

slotmachine_frame = [
    [sg.Image(filename='.SaveData\\slotimagedef1.png', key='slotimage1', metadata=1), sg.Image(filename='.SaveData\\slotimagedef2.png', key='slotimage2'), sg.Image(filename='.SaveData\\slotimagedef3.png', key='slotimage3')]
]

slotmachine_col = [
    [sg.Slider(range=(0, 300), orientation='vertical', default_value=300, disable_number_display=True, key='lever', enable_events=True, size=(22, 20)), sg.Frame('', slotmachine_frame, background_color='#FFFFFF')]
]

slotmachine_tab = [
    [sg.B('Unlock the slot machine - $2,000', key='slu', **btndef), sg.T('Slot Machine unlocked!', visible=False, key='sunlocked'),
     sg.T('Slot Machine Simulator', font=('Berlin Sans FB', 30), text_color='#ff0000', size=(355, 0), justification='center', key='stitle', visible=False)],
    [sg.T('Must unlock roulette first', key='rl', visible=False), sg.T('Not enough funds', visible=False, key='fails'), sg.B("Let's start!", visible=False, key='gotos', **btndef)],
    [sg.B('Ok', key='oks', visible=False, **btndef)],
    [sg.Frame('', slotmachine_balframe, visible=False, key='slotbalframe', background_color='#D8D8D8')],
    [sg.Col(slotmachine_col, visible=False, key='actualslot')],
    [sg.T('You won :D', key='wins', visible=False), sg.T('You lost :(', key='losss', visible=False), sg.T('JACKPOT!!', key='jackpot')]
]

tabgroup = [
    [sg.Tab('Coin Flip', coinflip_tab, element_justification='center')],
    [sg.Tab('Roulette 🔒', roulette_tab, element_justification='center', key='roul')],
    [sg.Tab('Slot Machine 🔒', slotmachine_tab, element_justification='center', key='sm')]
]

layout = [
    [sg.T('Gambling Simulator', font=('Berlin Sans FB', 30), text_color='#ff0000', size=(355, 0), justification='center')],
    [sg.T('Developed by Ali Kaddaha 8E', font=('Berlin Sans FB', 10), text_color='blue', justification='center', size=(355, 0))],
    [sg.TabGroup(tabgroup, selected_background_color='#F0F0F0'), ],
    [sg.B('Reset save data', **btndef, key='reset'), sg.B('Import save data from previous version', **btndef, key='import'), sg.B('Refresh', key='refresh', **btndef)],
    [sg.CB('Allow the simulator to use my data for the leaderboard', key='lbdata', enable_events=True)],
    [sg.I("Enter the name you'd like to be displayed in your leaderboard entry", key='username', visible=False, size=(55, 0)), sg.B('Submit', key='susername', visible=False, **btndef)],
    [sg.Frame('Cheats', cheats, visible=False, key='Cheats')]
]

window = sg.Window('Gambling Simulator', layout, size=(1360, 950), icon='.SaveData\\coin-flip-54.ico')

f = 0


def twoupdate(h, i, j, k):
    window[h].update(visible=i)
    window[j].update(visible=k)


def threeupdate(a, b, c, d, e, f):
    window[a].update(visible=b)
    window[c].update(visible=d)
    window[e].update(visible=f)


def allshowing(l):
    updated_elements = ['heads', 'heads1', 'tails', 'tails1', 'win', 'loss', 'error', 'notenough']
    for i in updated_elements:
        window[i].update(visible=l)


def allexc():
    threeupdate('error', True, 'heads', False, 'heads1', False)
    threeupdate('tails', False, 'tails1', False, 'win', False)
    window['loss'].update(visible=False)


def checkwin(x):
    global z
    global n
    global cur_frame
    try:
        if event == str(x):
            window['inpr'].update('')
            window['videotest'].update(data=None)
            twoupdate('unlock', False, 'goto', False)
            threeupdate('winr', False, 'lossr', False, 'landing', False)
            threeupdate('errorr', False, 'notenoughr', False, 'landing', False)
            if int(values['inpr']) > int(z) or int(values['inpr']) < 1:
                window['notenoughr'].update(visible=True)
            else:
                while True:
                    window['table'].update(visible=True)
                    ret, frame = testfile.read()
                    if not ret:
                        window.refresh()
                        if n == x:
                            window['landing'].update('The ball landed on ' + str(n), visible=True)
                            z = int(z) + int(values['inpr']) * int(35)
                            window['balr'].update(str(int(z)))
                            window['winr'].update(visible=True)
                            window.refresh()
                        else:
                            window['landing'].update('The ball landed on ' + str(n), visible=True)
                            z = int(z) - int(values['inpr'])
                            window['balr'].update(str(int(z)))
                            window['lossr'].update(visible=True)
                            window.refresh()
                        if int(z) < 1:
                            threeupdate('overr', True, 'rrestart', True, 'table', False)
                            window.refresh()
                        time.sleep(2)
                        window['videotest'].update(data=None)
                        threeupdate('winr', False, 'landing', False, 'lossr', False)
                        window.refresh()
                        break
                    imgbytes = cv.imencode('.png', frame)[1].tobytes()
                    testfile.set(cv.CAP_PROP_POS_FRAMES, cur_frame)
                    window['videotest'].update(data=imgbytes)
                    cur_frame += 1
                    window.refresh()
    except:
        threeupdate('errorr', True, 'landing', False, 'winr', False)
        window['lossr'].update(visible=False)
        window['videotest'].update(data=None)


def checkwinrb(x, a, b, c, d, e, f, g, h, i, j, k, l, m, y, o, p, q, r):
    global z
    global n
    global cur_frame
    try:
        if event == x:
            window['inpr'].update('')
            window['videotest'].update(data=None)
            twoupdate('unlock', False, 'goto', False)
            threeupdate('winr', False, 'lossr', False, 'landing', False)
            threeupdate('errorr', False, 'notenoughr', False, 'landing', False)
            if int(values['inpr']) > int(z) or int(values['inpr']) < 1:
                twoupdate('notenoughr', True, 'landing', False)
            else:
                while True:
                    window['table'].update(visible=True)
                    ret, frame = testfile.read()
                    if not ret:
                        window.refresh()
                        if n in [a, b, c, d, e, f, g, h, i, j, k, l, m, y, o, p, q, r]:
                            window['landing'].update('The ball landed on ' + str(n), visible=True)
                            z = int(z) + int(values['inpr'])
                            window['balr'].update(str(int(z)))
                            window['winr'].update(visible=True)
                            window.refresh()
                        else:
                            window['landing'].update('The ball landed on ' + str(n), visible=True)
                            z = int(z) - int(values['inpr'])
                            window['balr'].update(str(int(z)))
                            window['lossr'].update(visible=True)
                            window.refresh()
                        if int(z) < 1:
                            threeupdate('overr', True, 'rrestart', True, 'table', False)
                            window.refresh()
                        time.sleep(2)
                        window['videotest'].update(data=None)
                        threeupdate('winr', False, 'landing', False, 'lossr', False)
                        window.refresh()
                        break
                    imgbytes = cv.imencode('.png', frame)[1].tobytes()
                    testfile.set(cv.CAP_PROP_POS_FRAMES, cur_frame)
                    window['videotest'].update(data=imgbytes)
                    cur_frame += 1
                    window.refresh()
    except:
        threeupdate('errorr', True, 'landing', False, 'winr', False)
        window['lossr'].update(visible=False)
        window['videotest'].update(data=None)


def checkwineo(x, a, b, c, d, e, f, g, h, i, j, k, l, m, y, o, p, q, r, s):
    global z
    global n
    global cur_frame
    try:
        if event == x:
            window['inpr'].update('')
            twoupdate('unlock', False, 'goto', False)
            twoupdate('winr', False, 'lossr', False)
            twoupdate('errorr', False, 'notenoughr', False)
            window['landing'].update('The ball landed on ' + str(n), visible=True)
            if int(values['inpr']) > int(z) or int(values['inpr']) < 1:
                twoupdate('notenoughr', True, 'landing', False)
            else:
                while True:
                    window['table'].update(visible=True)
                    ret, frame = testfile.read()
                    if not ret:
                        window.refresh()
                        if n in [a, b, c, d, e, f, g, h, i, j, k, l, m, y, o, p, q, r, s]:
                            window['landing'].update('The ball landed on ' + str(n), visible=True)
                            z = int(z) + int(values['inpr'])
                            window['balr'].update(str(int(z)))
                            window['winr'].update(visible=True)
                            window.refresh()
                        else:
                            window['landing'].update('The ball landed on ' + str(n), visible=True)
                            z = int(z) - int(values['inpr'])
                            window['balr'].update(str(int(z)))
                            window['lossr'].update(visible=True)
                            window.refresh()
                        if int(z) < 1:
                            threeupdate('overr', True, 'rrestart', True, 'table', False)
                            window.refresh()
                        time.sleep(2)
                        window['videotest'].update(data=None)
                        threeupdate('winr', False, 'landing', False, 'lossr', False)
                        window.refresh()
                        break
                    imgbytes = cv.imencode('.png', frame)[1].tobytes()
                    testfile.set(cv.CAP_PROP_POS_FRAMES, cur_frame)
                    window['videotest'].update(data=imgbytes)
                    cur_frame += 1
                    window.refresh()
    except:
        threeupdate('errorr', True, 'landing', False, 'winr', False)
        window['lossr'].update(visible=False)
        window['videotest'].update(data=None)


def checkwinthird(x, a, b, c, d, e, f, g, h, i, j, k, l):
    global z
    global n
    global cur_frame
    try:
        if event == x:
            window['inpr'].update('')
            twoupdate('unlock', False, 'goto', False)
            twoupdate('winr', False, 'lossr', False)
            twoupdate('errorr', False, 'notenoughr', False)
            window['landing'].update('The ball landed on ' + str(n))
            if int(values['inpr']) > int(z) or int(values['inpr']) < 1:
                twoupdate('notenoughr', True, 'landing', False)
            else:
                while True:
                    window['table'].update(visible=True)
                    ret, frame = testfile.read()
                    if not ret:
                        window.refresh()
                        if n in [a, b, c, d, e, f, g, h, i, j, k, l]:
                            window['landing'].update('The ball landed on ' + str(n), visible=True)
                            z = int(z) + int(values['inpr']) * int(2)
                            window['balr'].update(str(int(z)))
                            window['winr'].update(visible=True)
                            window.refresh()
                        else:
                            window['landing'].update('The ball landed on ' + str(n), visible=True)
                            z = int(z) - int(values['inpr'])
                            window['balr'].update(str(int(z)))
                            window['lossr'].update(visible=True)
                            window.refresh()
                        if int(z) < 1:
                            threeupdate('overr', True, 'rrestart', True, 'table', False)
                            window.refresh()
                        time.sleep(2)
                        window['videotest'].update(data=None)
                        threeupdate('winr', False, 'landing', False, 'lossr', False)
                        window.refresh()
                        break
                    imgbytes = cv.imencode('.png', frame)[1].tobytes()
                    testfile.set(cv.CAP_PROP_POS_FRAMES, cur_frame)
                    window['videotest'].update(data=imgbytes)
                    cur_frame += 1
                    window.refresh()
    except:
        threeupdate('errorr', True, 'winr', False, 'lossr', False)
        window['landing'].update(visible=False)


def sm(x, y):
    slotpossibs = random.randint(1, 4)
    slotimagefilename = '.SaveData\\slotimage' + str(int(slotpossibs)) + '.png'
    window[x].update(filename=slotimagefilename)
    with open(y, 'w') as SaveData345:
        SaveData345.write(str(int(slotpossibs)))


def cheatvisibility(x):
    window['Cheats'].update(visible=x)


keyboard.add_hotkey('ctrl+shift+c', cheatvisibility, args=[True])
keyboard.add_hotkey('ctrl+shift+s', cheatvisibility, args=[False])
slidervalue = 100

oddoreven = 0

while True:
    n = random.randint(0, 36)
    files_name = 'Wheel Roll - ' + str(n) + '.mp4'
    files_pathname = '.SaveData\\' + str(files_name)
    testfile = cv.VideoCapture(files_pathname)
    cur_frame = 0
    event, values = window.read()
    if event is None or event == sg.WIN_CLOSED:
        sg.popup(title='Warning!', grab_anywhere=True, image='.SaveData\\beforeclosing.png', icon='.SaveData\\coin-flip-54.ico')
        if f > 0:
            break
        else:
            with open('.SaveData\\GamblingSimSaveData.txt', 'w') as SaveData:
                SaveData.write(str(z))
            break
    if event == 'Save':
        z = int(values['moners'])
        f = 1
    if event == 'reset':
        with open('.SaveData\\GamblingSimSaveData.txt', 'w') as SaveData:
            SaveData.write('100')
        with open('.SaveData\\GamblingSimSaveData1.txt', 'w') as SaveData1:
            SaveData1.write('0')
        with open('.SaveData\\GamblingSimSaveData2.txt', 'w') as SaveData2:
            SaveData2.write('0')
        f = 2
    elif event == 'refresh':
        window.refresh()
        window['bal'].update(str(int(z)))
        window['balr'].update(str(int(z)))
        with open('.SaveData\\GamblingSimSaveData1.txt', 'r') as SaveData1:
            SaveData1read = SaveData1.read()
        if SaveData1read == 1:
            threeupdate('unlock', False, 'goto', False, 'table', True)
        else:
            threeupdate('table', False, 'rlu', True, 'goto', False)
            window['unlock'].update(visible=False)
    window['bal'].update(str(int(z)))
    window['balr'].update(str(int(z)))
    x = random.randint(1, 2)
    if event == 'bth':
        window['inp'].update('')
        allshowing(False)
        if int(values['inp']) < 1:
            window['notenough'].update(visible=True)
        else:
            try:
                if int(values['inp']) > int(z):
                    allshowing(False)
                    window['notenough'].update(visible=True)
                else:
                    if x == 1:
                        threeupdate('heads', True, 'heads1', True, 'win', True)
                        try:
                            z = int(z) + int(values['inp'])
                            window['bal'].update(str(z))
                        except:
                            allexc()
                    elif x == 2:
                        threeupdate('tails', True, 'tails1', True, 'loss', True)
                        try:
                            z = int(z) - int(values['inp'])
                            window['bal'].update(str(z))
                        except:
                            allexc()
            except:
                window['error'].update(visible=True)
    elif event == 'btt':
        window['inp'].update('')
        allshowing(False)
        try:
            if int(values['inp']) > int(z):
                allshowing(False)
                window['notenough'].update(visible=True)
            else:
                if x == 1:
                    threeupdate('heads', True, 'heads1', True, 'loss', True)
                    try:
                        z = int(z) - int(values['inp'])
                        window['bal'].update(str(z))
                    except:
                        allexc()
                elif x == 2:
                    threeupdate('tails', True, 'tails1', True, 'win', True)
                    try:
                        z = int(z) + int(values['inp'])
                        window['bal'].update(str(z))
                    except:
                        allexc()
        except:
            window['error'].update(visible=True)
    if int(z) < int(1):
        twoupdate('over', True, 'over1', True)
        window['btt'].update(disabled=True)
        window['bth'].update(disabled=True)
    if event == 'over1':
        allshowing(False)
        twoupdate('over', False, 'over1', False)
        window['btt'].update(disabled=False)
        window['bth'].update(disabled=False)
        threeupdate('overr', False, 'rrestart', False, 'table', True)
        z = int(z) - int(z) + int(100)
        window['bal'].update(str(int(z)))
    if event == 'rlu':
        window['table'].update(visible=False)
        with open('.SaveData\\GamblingSimSaveData1.txt', 'r') as SaveData1:
            savedataread = SaveData1.read()
            if int(savedataread) == int(1):
                threeupdate('rlu', False, 'unlock', True, 'goto', True)
                window['roul'].update('Roulette')
                twoupdate('fail', False, 'ok', False)
            else:
                if int(z) > 1000:
                    with open('.SaveData\\GamblingSimSaveData1.txt', 'w') as SaveData1:
                        SaveData1.write('1')
                    z = int(z) - int(1000)
                    window['bal'].update(str(int(z)))
                    threeupdate('rlu', False, 'unlock', True, 'goto', True)
                    window['roul'].update('Roulette')
                elif int(z) < 1001:
                    twoupdate('fail', True, 'ok', True)
    if event == 'slu':
        with open('.SaveData\\GamblingSimSaveData1.txt', 'r') as SaveData1:
            saveedata = SaveData1.read()
            if int(saveedata) == 1:
                with open('.SaveData\\GamblingSimSaveData2.txt', 'r') as SaveData2:
                    savedata2read = SaveData2.read()
                if int(savedata2read) == 1:
                    threeupdate('slu', False, 'sunlocked', True, 'gotos', True)
                    window['sm'].update('Slot Machine')
                    window['fails'].update(visible=False)
                    window['oks'].update(visible=False)
                elif int(z) > 2000:
                    with open('.SaveData\\GamblingSimSaveData2.txt', 'w') as SaveData2:
                        SaveData2.write('1')
                    z = int(z) - int(2000)
                    window['bal'].update(str(int(z)))
                    threeupdate('slu', False, 'sunlocked', True, 'gotos', True)
                    window['sm'].update('Slot Machine')
                elif int(z) < 2001:
                    twoupdate('fails', True, 'oks', True)
            else:
                twoupdate('rl', True, 'oks', True)
    if event == 'ok':
        twoupdate('fail', False, 'ok', False)
    if event == 'oks':
        threeupdate('rl', False, 'fails', False, 'oks', False)
    if event == 'goto':
        threeupdate('unlock', False, 'goto', False, 'title', True)
        twoupdate('inprf', True, 'table', True)
        window['balr'].update(str(int(z)))
        window['bal'].update(str(int(z)))
    elif event == 'gotos':
        threeupdate('sunlocked', False, 'goto', False, 'stitle', True)
        threeupdate('slotbalframe', True, 'actualslot', True, 'gotos', False)
        window['balr'].update(str(int(z)))
        window['bals'].update(str(int(z)))
        window['bal'].update(str(int(z)))
    for i in range(37):
        checkwin(i)
    checkwinrb('RED', 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
    checkwinrb('BLACK', 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)
    checkwineo('EVEN', 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36)
    checkwineo('ODD', 1, 3, 5, 7, 8, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35)
    checkwinrb('1 to 18', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
    checkwinrb('19 to 36', 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36)
    checkwinthird('1st\nrow', 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36)
    checkwinthird('2nd\nrow', 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35)
    checkwinthird('3rd\nrow', 1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34)
    checkwinthird('1st 12', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
    checkwinthird('2nd 12', 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)
    checkwinthird('3rd 12', 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36)
    if event == 'lever':
        timer = time.time()
        try:
            if values['lever'] == 0:
                window['inps'].update('')
                threeupdate('wins', False, 'losss', False, 'errors', False)
                window['jackpot'].update(visible=False)
                window['lever'].update(300)
                if int(values['inps']) < 1:
                    window['errors'].update(visible=True)
                    window['lever'].update(300)
                elif int(z) < 1:
                    twoupdate('overs', True, 'srestart', True)
                    window['lever'].update(disabled=True)
                    window.refresh()
                else:
                    window['lever'].update(300, disabled=True)
                    while time.time() < timer + 3:
                        sm('slotimage1', '.SaveData\\GamblingSimSaveData3.txt')
                        sm('slotimage2', '.SaveData\\GamblingSimSaveData4.txt')
                        sm('slotimage3', '.SaveData\\GamblingSimSaveData5.txt')
                        time.sleep(0.1)
                        window.refresh()
                    window['lever'].update(disabled=False)
                    with open('.SaveData\\GamblingSimSaveData3.txt', 'r') as SaveData3:
                        savedata3read = SaveData3.read()
                    with open('.SaveData\\GamblingSimSaveData4.txt', 'r') as SaveData4:
                        savedata4read = SaveData4.read()
                    with open('.SaveData\\GamblingSimSaveData5.txt', 'r') as SaveData5:
                        savedata5read = SaveData5.read()
                    if int(savedata3read) in [int(savedata4read), int(savedata5read)] or int(savedata4read) in [int(savedata3read), int(savedata5read)] or int(savedata5read) in [int(savedata3read), int(savedata4read)]:
                        window['wins'].update(visible=True)
                        z = int(z) + int(values['inps'])
                        if int(savedata3read) == int(savedata4read) and int(savedata3read) == int(savedata5read):
                            twoupdate('wins', False, 'jackpot', True)
                            z = int(z) + int(values['inps'])
                    else:
                        window['losss'].update(visible=True)
                        z = int(z) - int(values['inps'])
        except:
            window['lever'].update(300)
            window['errors'].update(visible=True)
    window['bal'].update(str(int(z)))
    window['balr'].update(str(int(z)))
    window['bals'].update(str(int(z)))
    if event == 'rrestart':
        threeupdate('overr', False, 'rrestart', False, 'table', True)
        z = int(z) + 100
        window['balr'].update(str(int(z)))
        window['bal'].update(str(int(z)))
        twoupdate('over', False, 'over1', False)
        window['bth'].update(disabled=False)
        window['btt'].update(disabled=False)
    elif event == 'srestart':
        window['lever'].update(disabled=False)
        threeupdate('overs', False, 'srestart', False, 'actualslot', True)
        z = 100
        window['balr'].update(str(int(z)))
        window['bals'].update(str(int(z)))
        window['bal'].update(str(int(z)))
        threeupdate('over', False, 'over1', False, 'overr', False)
        window['rrestart'].update(visible=False)
    if event == 'import':
        prevdata = sg.popup_get_file('Please upload the extracted (not .rar) folder of your previous release:', title='Import save data from a previous release', icon='.SaveData\\coin-flip-54.ico', button_color=('black', 'white'))
        try:
            prevdatapath = prevdata.replace('/', "\\")
            data0 = prevdatapath + '\\.SaveData\\GamblingSimSaveData.txt'
            data1 = prevdatapath + '\\.SaveData\\GamblingSimSaveData1.txt'
            data2 = prevdatapath + '\\.SaveData\\GamblingSimSaveData2.txt'
            with open(data0, 'r') as PrevData0:
                prevmoners = int(PrevData0.read())
            with open('.SaveData\\GamblingSimSaveData.txt', 'w') as SaveData0:
                SaveData0.write(str(prevmoners))
            with open(data1, 'r') as PrevData1:
                prevrunlock = int(PrevData1.read())
            with open('.SaveData\\GamblingSimSaveData1.txt', 'w') as SaveData1:
                SaveData1.write(str(prevrunlock))
            with open(data2, 'r') as SaveData2:
                prevsunlock = int(SaveData2.read())
            with open('.SaveData\\GamblingSimSaveData2.txt', 'w') as SaveData2:
                SaveData2.write(str(prevsunlock))
            z = prevmoners
            window['bal'].update(str(int(z)))
            window['balr'].update(str(int(z)))
            window['bals'].update(str(int(z)))
        except Exception as error:
            errorsplit = str(error).split(' ')
            errorr = 'Error code:\n' + str(error)
            if errorsplit[1] == "2]":
                errorr = 'The folder you attempted to import does not contain the game files\n\n' + errorr
            elif str(error) == "'NoneType' object has no attribute 'replace'":
                errorr = 'Nothing uploaded, import cancelled\n\n' + errorr
            sg.popup(errorr, grab_anywhere=True, icon='.SaveData\\coin-flip-54.ico', button_color=('black', 'white'), title='Error')
    with open('.SaveData\\GamblingSimSaveData1.txt', 'r') as SaveData1:
        SaveData1 = SaveData1.read()
    with open('.SaveData\\GamblingSimSaveData2.txt', 'r') as SaveData2:
        SaveData2 = SaveData2.read()
    window['rouletteunlocktion'].update(str(int(SaveData1)))
    window['slotmachineunlocktion'].update(str(int(SaveData2)))
    if event == 'lbdata':
        oddoreven += 1
    if values['lbdata']:
        twoupdate('username', True, 'susername', True)
    elif not values['lbdata']:
        twoupdate('username', False, 'susername', False)
    if event == 'susername':
        username = values['username']
        with open('.SaveData\\Username.txt', 'w') as lbentry:
            lbentry.write(username)
        window['username'].update('')
window.close()

with open('.SaveData\\GamblingSimSaveData.txt', 'r') as epic:
    lbdata = str(epic.read())
with open('.SaveData\\Username.txt', 'r') as username:
    un = str(username.read())
with open('leaderboard_data.txt', 'w') as fulllbdata:
    fulllbdata.write(lbdata)
    fulllbdata.write('\n' + un)

if (oddoreven % 2) != 0:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 8080))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        break
    epicmoners = open('leaderboard_data.txt', 'rb')
    monersread = epicmoners.read(1024)
    conn.send(monersread)
