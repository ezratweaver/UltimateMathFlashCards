class Utility():
    def button_bg_modify(event, color, 
                    canvas, background_image, 
                    new_backgroud_image):
        event.widget.config(bg=color)
        canvas.itemconfigure(background_image, image=new_backgroud_image)