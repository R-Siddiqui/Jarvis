from jarvis import*
# os.startfile("C:\\Users\\rihan\\OneDrive\\Pictures\\dump\\0.jpeg")
os.startfile("C:\\Users\\rihan\\OneDrive\\Pictures\\dump\\4.jpeg")
def image():
    lo = takecommand().lower()
    if "select this" in lo:
        pyautogui.hotkey("ctrl", "shift", "c")
        speak("ok sir i seleted this picture")
        win32clipboard.OpenClipboard()
        m = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        shutil.move(f"{m}", "C:\\Users\\rihan\\OneDrive\\Pictures\\image gen")
        files = glob.glob('C:\\Users\\rihan\\OneDrive\\Pictures\\dump\\*')
        for f in files:
            os.remove(f)
            os.system(f'taskkill /IM PhotosAPP.exe /F')

    elif "regenerate" in lo:
        gen_image()
    elif "ok" in lo:
        speak("yes sir what should i help you")
        taskexecution()
while True:
    image()
       