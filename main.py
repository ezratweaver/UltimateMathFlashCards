from controller import userscreen, root

if __name__ == "__main__":
    userscreen.show_canvas()
    userscreen.run_gui()
    root.geometry("800x500")
    root.title("")
    root.resizable(False, False)
    root.mainloop()