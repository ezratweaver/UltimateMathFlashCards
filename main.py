import controller

# TODO: Get memory to work
# TODO: Link screens with controller

if __name__ == "__main__":
    controller.screen_objects["user_screen"].show_canvas()
    controller.user_screen_init()
    controller.assets.root.mainloop()
