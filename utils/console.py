import os
import sys
import time


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def sleep(delay=1):
    time.sleep(delay)


def show_loading(text="Carregando", duration=1.5, interval=0.3):
    end_time = time.time() + duration

    while time.time() < end_time:
        for dots in ("", ".", "..", "..."):
            sys.stdout.write(f"\r{text}{dots}   ")
            sys.stdout.flush()
            time.sleep(interval)
            if time.time() >= end_time:
                break

    sys.stdout.write("\r" + " " * (len(text) + 6) + "\r")
    sys.stdout.flush()

def pause(message="Pressione Enter para continuar..."):
    input(message)