import pyautogui

# Some Message Box

info = pyautogui.alert('some', 'SOME SOME SOM') # Just info window
ok_info = pyautogui.confirm('hoo', 'YOUUU SOLJA BOY') # Info window with ok button
string_info = pyautogui.prompt('AOao', 'My window', default='write here') # Window with string input
password = pyautogui.password('Type a password', 'PAROOL', mask='*')
print(string_info)
print('Your password - ', password)
