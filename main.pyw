from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Separator
from threading import Thread
from time import sleep, localtime
from webbrowser import open_new_tab
from keyboard import add_hotkey, remove_hotkey

root = Tk()
root.title("Parody Desktop")
root.geometry("1000x680+100+100")
root.config(bg="light blue", cursor=f'@{"images/cursors/normal_select.cur"}')
root.resizable(False, False)
root.overrideredirect(True)
root.attributes("-topmost", True)

#custom title bar

titlebar = Frame(root, height=30, bg="#222", cursor="arrow")
titlebar.pack(fill=X)
titlebar.propagate(False)

x = Label(titlebar, text="Parody Desktop", bg="#222", font=("TkDefaultFont", 12, "bold"), fg="white"); x.pack(expand=True)
titlebar.bind("<B1-Motion>", lambda e: root.geometry(f"+{e.x_root-500}+{e.y_root-5}"))
x.bind("<B1-Motion>", lambda e: root.geometry(f"+{e.x_root-500}+{e.y_root-5}"))

#/custom title bar

background1 = PhotoImage("background1", file="images/background1.png")
background2 = PhotoImage("background2", file="images/background2.png")
bg_label = Label(root, image=background1); bg_label.place(x=0, y=0, relwidth=1, relheight=1)
titlebar.tkraise()

#dock
dock = Frame(root, bg="#222", height=45)
dock.pack(fill=X, side=BOTTOM)
dock.propagate(False)

hamburger_menu = PhotoImage("hamburgerMenu", file="images/icons/hmenu.png")
menu_button = Label(dock, text="", width=30, height=30, bg="#222", image=hamburger_menu, cursor=f"@{"images/cursors/link.cur"}")
menu_button.pack(side=LEFT, padx=3)

time_frame = Frame(dock, bg="#222", width=80)
time_frame.pack(side=RIGHT, fill=Y, pady=3, padx=3)
time_frame.propagate(False)

def tf_onHover(e):
    time_frame.config(bg="#333")
    time_label.config(bg="#333")
    date_label.config(bg="#333")

def tf_onLeave(e):
    time_frame.config(bg="#222")
    time_label.config(bg="#222")
    date_label.config(bg="#222")

time_frame.bind("<Enter>", tf_onHover)
time_frame.bind("<Leave>", tf_onLeave)

def update_tf():
    LocalTime = localtime()
    time = f"{LocalTime.tm_hour:02}:{LocalTime.tm_min:02}:{LocalTime.tm_sec:02}"
    date = f"{LocalTime.tm_mon:02}/{LocalTime.tm_mday:02}/{LocalTime.tm_year}"

    time_label.config(text=time)
    date_label.config(text=date)

    root.after(500, update_tf)

time_label = Label(time_frame, font=('Tahoma', 10, "bold"), text="Testing", fg="white", bg="#222")
time_label.pack()

date_label = Label(time_frame, font=('Tahoma', 7, "bold"), text="Testing", fg="white", bg="#222")
date_label.pack()

update_tf()

#/dock

#menu
menu = Frame(root, width=250, height=100, bg="#333")
menu.propagate(False)
start_pos, end_pos = IntVar(root, 642), IntVar(root, 540)
menu.place(y=start_pos.get())
dock.tkraise()
menu_shown = False

Label(menu, text="Made by PabloMyLove, BFPS: 7B!!!", fg="white", bg="#333", font=("Tahoma", 8)).pack(pady=2)

menu_buttons = Frame(menu, bg="#333")
menu_buttons.pack(expand=True)

def mb_hovered(button: Button, hint: str, img: PhotoImage | None = None):
    button.config(bg="#444", image=img)
    hint_label.config(text=hint)
def mb_left(button: Button, img: PhotoImage | None = None):
    button.config(bg="#333", image=img)
    hint_label.config(text=" ")

white_exit, red_exit = PhotoImage("white exit", file="images/icons/whiteexit.png"), PhotoImage("red exit", file="images/icons/redexit.png")
exit_button = Label(menu_buttons, width=36, height=36, bg="#333", cursor=f"@{"images/cursors/link.cur"}", image=white_exit)
exit_button.pack(side=LEFT, padx=5)
exit_button.bind("<Enter>", lambda e: mb_hovered(exit_button, "Exit Parody Desktop.", red_exit))
exit_button.bind("<Leave>", lambda e: mb_left(exit_button, white_exit))
def Quit(e):
    root.quit()
    root.destroy()
exit_button.bind("<Button-1>", Quit)

sleep_image = PhotoImage("sleep", file="images/icons/moon.png")
sleep_button = Label(menu_buttons, width=36, height=36, bg="#333", cursor=f"@{"images/cursors/link.cur"}", image=sleep_image)
sleep_button.pack(side=LEFT, padx=5)
sleep_button.bind("<Enter>", lambda e: mb_hovered(sleep_button, "Hide Parody Desktop. Ctrl+Alt+S to bring it back!"))
sleep_button.bind("<Leave>", lambda e: mb_left(sleep_button))
def hide(e):
    root.withdraw()
    def show():
        root.deiconify()
        remove_hotkey("ctrl+alt+s")
    add_hotkey("ctrl+alt+s", show)
sleep_button.bind("<Button-1>", hide)

link_image = PhotoImage("link", file="images/icons/link.png")
linktree_button = Label(menu_buttons, width=36, height=36, bg="#333", cursor=f"@{"images/cursors/link.cur"}", image=link_image)
linktree_button.pack(side=LEFT, padx=5)
linktree_button.bind("<Enter>", lambda e: mb_hovered(linktree_button, "Visit my linktree!"))
linktree_button.bind("<Leave>", lambda e: mb_left(linktree_button))
linktree_button.bind("<Button-1>", lambda e: open_new_tab("https://pablomydarling.github.io/linktree/"))

fullscreen = PhotoImage("fullscreen", file="images/icons/fullscreen.png")
minimize = PhotoImage("minimize", file="images/icons/minimize.png")
fullscreen_button = Label(menu_buttons, width=36, height=36, bg="#333", cursor=f"@{"images/cursors/link.cur"}", image=fullscreen)
fullscreen_button.pack(side=LEFT, padx=5)
fullscreen_button.bind("<Enter>", lambda e: mb_hovered(fullscreen_button, "Go fullscreen on Parody Desktop."))
fullscreen_button.bind("<Leave>", lambda e: mb_left(fullscreen_button))
def go_fullscreen(e):
    if root.attributes("-fullscreen"):
        root.overrideredirect(True)
        root.attributes("-fullscreen", False)
        start_pos.set(642)
        end_pos.set(540)
        show_menu(None)
        fullscreen_button.config(image=fullscreen)
        fullscreen_button.unbind("<Enter>")
        fullscreen_button.bind("<Enter>", lambda e: mb_hovered(fullscreen_button, "Go fullscreen on Parody Desktop."))
        bg_label.config(image=background1)
    else:
        root.overrideredirect(False)
        root.attributes("-fullscreen", True)
        start_pos.set(root.winfo_screenheight() - dock.cget("height") + 1)
        end_pos.set(root.winfo_screenheight() - menu.cget("height") - 45)
        show_menu(None)
        fullscreen_button.config(image=minimize)
        fullscreen_button.unbind("<Enter>")
        fullscreen_button.bind("<Enter>", lambda e: mb_hovered(fullscreen_button, "Window Parody Desktop."))
        bg_label.config(image=background2)
fullscreen_button.bind("<Button-1>", go_fullscreen)

def show_menu(e):
    global menu_shown
    if not menu_shown:
        def x():
            global menu_shown
            for n in range(start_pos.get(), end_pos.get(), -1):
                menu.place_configure(y=n)
                sleep(.0001)
            menu_shown = True
        Thread(target=x).start()
    else:
        def x():
            global menu_shown
            for n in range(end_pos.get(), start_pos.get()):
                menu.place_configure(y=n)
                sleep(.00001)
            menu_shown = False
        Thread(target=x).start()

hint_label = Label(menu, text=" ", fg="white", bg="#333", font=("Tahoma", 7, "normal", "italic"))
hint_label.pack(side=BOTTOM, pady=3)

menu_button.bind("<Enter>", lambda e: menu_button.config(bg="#444"))
menu_button.bind("<Leave>", lambda e: menu_button.config(bg="#222"))
menu_button.bind("<Button-1>", show_menu)
#/menu

#right click menu
right_click_menu = Frame(root, bg="#333", width=225, height=200, highlightbackground="#999", highlightthickness=3)
right_click_menu.propagate(False)

bg_label.bind("<Button-3>", lambda e: right_click_menu.place(x=e.x, y=e.y))
bg_label.bind("<Button-1>", lambda e: right_click_menu.place_forget())

def hover(button: Label): button.config(bg="#555")
def hover_off(button: Label): button.config(bg="#333")

font = Font(size=12, family="Tahoma")
button1 = Label(right_click_menu, justify=LEFT, anchor=W, cursor=f"@{"images/cursors/link.cur"}", bg="#333", text="Cool button", fg="white", font=font)
button1.pack(pady=2, fill=X)
button1.bind("<Enter>", lambda e: hover(button1))
button1.bind("<Leave>", lambda e: hover_off(button1))
button1.bind("<Button-1>", lambda e: right_click_menu.place_forget())

button2 = Label(right_click_menu, justify=LEFT, anchor=W, cursor=f"@{"images/cursors/link.cur"}", bg="#333", text="Another cool button", fg="white", font=font)
button2.pack(pady=2, fill=X)
button2.bind("<Enter>", lambda e: hover(button2))
button2.bind("<Leave>", lambda e: hover_off(button2))
button2.bind("<Button-1>", lambda e: right_click_menu.place_forget())

Separator(right_click_menu).pack(fill=X, pady=2)

button3 = Label(right_click_menu, justify=LEFT, anchor=W, cursor=f"@{"images/cursors/link.cur"}", bg="#333", text="And another cool button", fg="white", font=font)
button3.pack(pady=2, fill=X)
button3.bind("<Enter>", lambda e: hover(button3))
button3.bind("<Leave>", lambda e: hover_off(button3))
button3.bind("<Button-1>", lambda e: right_click_menu.place_forget())

#/right click menu

mainloop()
