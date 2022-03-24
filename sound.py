import winsound
#from pynput.keyboard import Key
winsound.PlaySound("alarm.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )

st = input(' Press enter to stop ')

if st=='':
    print('Stoping.....')
    winsound.PlaySound(None, winsound.SND_ASYNC)