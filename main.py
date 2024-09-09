import tkinter as tk
import pyperclip
import keyboard

def copy_to_clipboard(spcl_ltter):
    pyperclip.copy(spcl_ltter)
    keyboard.write(spcl_ltter)

def bind_global_shortcuts():
    keyboard.add_hotkey('ctrl+1', lambda: copy_to_clipboard('ñ'))
    keyboard.add_hotkey('ctrl+2', lambda: copy_to_clipboard('à'))
    keyboard.add_hotkey('ctrl+3', lambda: copy_to_clipboard('ä'))
    keyboard.add_hotkey('ctrl+4', lambda: copy_to_clipboard('ā'))

root = tk.Tk()
root.title("Special Characters")
root.geometry("300x250")

root.wm_attributes("-alpha", 0.8)
root.wm_attributes("-topmost", True)

# Add a label for demonstration
label = tk.Label(root, text="Press Ctrl+1 for ñ, Ctrl+2 for à, Ctrl+3 for ä, Ctrl+4 for ā")
label.pack(pady=20)

# Add buttons for special characters
characters = ['ñ', 'à', 'ä', 'ā']
for spcl_ltter in characters:
    button = tk.Button(root, text=spcl_ltter, command=lambda spcl_ltter=spcl_ltter: copy_to_clipboard(spcl_ltter))
    button.pack(pady=5)

bind_global_shortcuts()
root.mainloop()
keyboard.wait()
