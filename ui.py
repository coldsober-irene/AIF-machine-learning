from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox, PhotoImage
from time import sleep
import pyautogui

list_object = []

win = Tk()
win.title("Machine learning User interface By Irene")
win.state("zoomed")
win.config(bg = "gray90")

# SCREEN SIZE
s_width, s_height = pyautogui.size()

# TRANSFER INFO IN ANOTHER WIDGET AFTER ANOTHER IS CLICKED OR ITEM IS SELECTED
def info_passer(receiver, message, combo = False):
    receiver.insert(END, message)

def label_entry(parent, label, index, list_object, num_entries = None, ipadx = 0, add_btn = False, is_combo = False, combo_values = None):
    """list_object: a list to hold data from entry-box,
    index: is the position of the entry in the list_object
    label: thr=e text to appear prior the entry box
    parent: Parent frame or window to hold the entry box
    num_entries: number of entries we need to produce
    """
    if num_entries:
        list_object = [0]*num_entries
    ent = None
    if not is_combo:
        Label(parent, text = label).pack(side = TOP, fill = X)
        ent = Entry(parent)
        ent.bind("<KeyRelease>", lambda e: grab_value())
        ent.pack(side = TOP, fill = X, ipadx = ipadx)
    else:
        Label(parent, text=label).pack(side=TOP, fill=X)
        ent = ttk.Combobox(parent, values = combo_values)
        ent.bind("<<ComboboxSelected>>", lambda e: grab_value())
        ent.pack(side=TOP, fill=X, ipadx=ipadx)

    def grab_value():
        list_object[index] = ent.get()

    if add_btn:
        py = 1
        train = ttk.Button(parent, text = "Train model")
        train.pack(side = TOP, fill = X, pady = py)

        predict = ttk.Button(parent, text="Predict")
        predict.pack(side=TOP, fill=X, pady = py)

        accuracy = ttk.Button(parent, text="Accuracy")
        accuracy.pack(side=TOP, fill=X, pady = py)

        save_model = ttk.Button(parent, text="Save Model")
        save_model.pack(side=TOP, fill=X, pady = py)

        return train, predict, accuracy, save_model

def setup():
    p_width = 200
    parent_frame1 = Frame(win,bg = "gray90")
    parent_frame1.place(x = 2, y = 2, width = p_width, height = 400)

    # WORKPLACE
    workplace = Frame(win, bg="gray70")
    workplace.place(x=p_width+2, y=2, width=s_width-p_width-2, height=s_height-2)

    sel_width = 200
    sel_side = TOP
    sel_padx = 2
    sel_pady = 2

    # FILE SELECTION
    file_selection = LabelFrame(parent_frame1, width = sel_width, text = "Select file")
    file_selection.pack(side = sel_side, padx = sel_padx, pady = sel_pady, fill = X)

    Label(file_selection, text = "File").pack(side = TOP, fill = BOTH, expand = True)
    file_entry = Entry(file_selection, width = 60)
    file_entry.pack(side = TOP, fill = BOTH, expand = True)

    Label(file_selection, text="File extension").pack(side=TOP, fill=BOTH, expand=True)
    file_ext = Entry(file_selection, width= 60)
    file_ext.pack(side=TOP, expand=True, anchor = W)

    # MODEL SELECTION FRAME
    model_selection = LabelFrame(parent_frame1, width=sel_width, text="Select Model")
    model_selection.pack(side = sel_side, padx = sel_padx, pady = sel_pady, fill = X)

    # ALGORITHM SELECTION
    Label(model_selection, text="Algorithm").pack(side=TOP, fill=BOTH, expand=True)
    algo_entry = ttk.Combobox(model_selection, width=60, state="readonly")
    algo_entry.pack(side=TOP, fill=BOTH, expand=True)

    # MODEL SELECTION
    Label(model_selection, text="Model").pack(side=TOP, fill=BOTH, expand=True)
    model_entry = ttk.Combobox(model_selection, width=60, state = "readonly")
    model_entry.pack(side=TOP, fill=BOTH, expand=True)

    # MODEL TYPE
    Label(model_selection, text="Model type").pack(side=TOP, fill=BOTH, expand=True)
    model_type = Entry(model_selection, width=60)
    model_type.pack(side=TOP, expand=True, anchor=W)

    # MODEL INFO
    Label(model_selection, text="Model application areas").pack(side=TOP, fill=X, expand=True)
    model_usage = Text(model_selection, width=60, height = 10)
    model_usage.pack(side=TOP, expand=True, anchor=W)

    # HYPERPARAMETERS TUNING
    parent_frame2 = LabelFrame(win, bg="gray80", text = "Tuning")
    parent_frame2.place(x=2, y=401, width=p_width, height=300)

    # CANVAS
    canv = Canvas(parent_frame2, width = p_width-20, bg = "maroon")
    scr1 = ttk.Scrollbar(parent_frame2, orient=VERTICAL, command=canv.yview)
    scr2 = ttk.Scrollbar(parent_frame2, orient=HORIZONTAL, command=canv.xview)
    scrol_frame = Frame(canv)

    scrol_frame.bind("<Configure>", lambda e: canv.configure(scrollregion=canv.bbox("all")))
    canv.create_window((0, 0), window=scrol_frame, anchor="nw")
    canv.config(yscrollcommand=scr1.set)
    canv.config(xscrollcommand=scr2.set)
    canv.pack(side=LEFT, fill=Y, expand=True, pady=1)
    scr1.pack(side=LEFT, pady=1, fill=Y)
    # scr2.pack(side=BOTTOM, pady=pady, fill=X, anchor=SW)

    for i in range(10):
        decision = False
        if i == 9:
            decision = True
        label_entry(scrol_frame, "label "+str(i), i, list_object, num_entries=10, ipadx = 20, add_btn=decision)

setup()
win.mainloop()