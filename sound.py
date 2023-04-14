from pygame import mixer


class sound_class():
    mixer.init()
    sound_correct = mixer.Sound("assets/sounds/correct.wav")
    sound_countdown_tick = mixer.Sound("assets/sounds/countdowntick.wav")
    sound_timer_tick = mixer.Sound("assets/sounds/timertick.wav")
    sound_wrong = mixer.Sound("assets/sounds/wrong.wav")
    sound_buttonpress = mixer.Sound("assets/sounds/buttonpress.wav")
    sound_win = mixer.Sound("assets/sounds/win.wav")
    sound_times_up = mixer.Sound("assets/sounds/timesup.wav")

    def muted_all_sounds(volume):
        sound_class.sound_correct.set_volume(volume)
        sound_class.sound_countdown_tick.set_volume(volume)
        sound_class.sound_timer_tick.set_volume(volume)
        sound_class.sound_wrong.set_volume(volume)
        sound_class.sound_buttonpress.set_volume(volume)
        sound_class.sound_win.set_volume(volume)
        sound_class.sound_times_up.set_volume(volume)
