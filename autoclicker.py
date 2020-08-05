import pyautogui as pygui
from pynput import keyboard as k
import sys


try:
    # Configurações
    tempo = 2  # em segundos
    resume_key = k.Key.f1
    pause_key = k.Key.f2
    exit_key = k.Key.esc

    pause = True
    running = True

    def on_press(key):
        global running, pause

        if key == resume_key:
            pause = False
            print("[Retomado]")
        elif key == pause_key:
            pause = True
            print("[Pausado]")
        elif key == exit_key:
            running = False
            print("[Sair]")


    def display_controls():
        print("Configurações: ")
         print('Pressione F1 para iniciar...')


    def main():
        lis = k.Listener(on_press=on_press)
        lis.start()

        display_controls()
        while running:
            if not pause:
                pygui.click(pygui.position())
                pygui.PAUSE = tempo
        lis.stop()


    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    sys.exit()