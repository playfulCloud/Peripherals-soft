import matplotlib
import sounddevice as sd
import tkinter as tk
from tkinter import filedialog

from scipy.io.wavfile import write
import matplotlib
matplotlib.use('TkAgg')
import librosa
import matplotlib.pyplot as plt
import numpy as np

from pydub import AudioSegment

# Load the mp3 file



pause = False

def choose_file():
    root = tk.Tk()
    root.withdraw()  # ukryj okno głównego
    file_path = filedialog.askopenfilename()  # otwórz okno dialogowe wyboru pliku
    return file_path

# Wywołaj funkcję choose_file() i zapisz zwróconą ścieżkę pliku




print("1 - Nagrywanie własnego dźwięku za pomocą dowolonego urządzenia dźwiękowego rozpoznawalnego przez komputer")
print("2 - Wybranie dowolnego pliku na komputerze w formacie mp3 ")
gate = int(input(": "))

if gate == 1:
    # Wyświetlanie dostępnych urządzeń
    devices = sd.query_devices()
    for i, device in enumerate(devices):
        print(f"Device #{i}: {device['name']}")


    deviceToPick = input("Wybierz odpowiednie narzędzie do nagrywania: ")

    sd.default.device = int(deviceToPick), sd.default.device[1]

    # Wybór domyślnego urządzenia do nagrywania
    default_device = sd.default.device
    default_input_device, default_output_device = sd.default.device


    print(f"\nDefault input device is {default_input_device}: {devices[default_input_device]['name']}")
    print(f"Default output device is {default_output_device}: {devices[default_output_device]['name']}")

    fs = int(input("Wybierz częstotliwość próbkowania proponowana wartość 44100: "))
    seconds = int(input("Wpisz czas nagraywania proponowana wartość to 3 sekudny: "))

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Czekamy aż nagranie się zakończy
    write('output.wav', fs, myrecording)  # Zapisujemy nagranie jako plik WAV
else:
    myAudioFilename = choose_file()
    audio = AudioSegment.from_mp3(myAudioFilename)
    audio.export("output.wav",   format="wav")

myAudioFilename = 'output.wav'
# odczyt danych audio
y, sr = librosa.load(myAudioFilename)

# czas trwania dźwięku
duration = len(y) / sr

# wektor czasu
time = np.arange(0, duration, 1/sr)

# wygenerowanie wykresu
plt.figure(figsize=(15, 5))
plt.plot(time, y)
plt.title('Wykres sygnału dźwiękowego')
plt.ylabel('Amplituda')
plt.xlabel('Czas [s]')
plt.xlim(0, duration)  # ograniczenie osi x do czasu trwania dźwięku
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

# create slider
slider_ax = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = matplotlib.widgets.Slider(slider_ax, 'Time', 0.0, duration, valinit=0)

# create button
button_right = plt.axes([0.6, 0.025, 0.1, 0.04])
button = matplotlib.widgets.Button(button_right, '>')

button_pause = plt.axes([0.5, 0.025, 0.1, 0.04])
button2 = matplotlib.widgets.Button(button_pause, 'Pause')


button_left = plt.axes([0.4, 0.025, 0.1, 0.04])
button3 = matplotlib.widgets.Button(button_left, '<')

import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Definiowanie przycisku play
button_play = plt.axes([0.7, 0.025, 0.1, 0.04])
button4 = Button(button_play, 'Play')

# Definiowanie funkcji do przesuwania wykresu

def update_play(val):
    global pause
    pause = False
    start = slider.val
    while not pause and slider.val < duration:
        start = slider.val
        slider.val += (duration / 50)
        end = slider.val
        ax.set_xlim([start, end])
        fig.canvas.draw_idle()
        slider.set_val(slider.val)
        plt.pause(0.05)

def update(val):
    if 0 <= slider.val <= duration:
        start = slider.val
        slider.val += (duration / 10)
        end = slider.val
        ax.set_xlim([start, end])
        fig.canvas.draw_idle()
        slider.set_val(slider.val)


def update_pause(val):
    global pause
    pause = True



def update2(val):
    if 0 < slider.val <= duration:
        end = slider.val
        slider.val -= (duration / 10)
        start = slider.val
        ax.set_xlim([start, end])
        fig.canvas.draw_idle()
        slider.set_val(slider.val)




button.on_clicked(update)
button3.on_clicked(update2)
button2.on_clicked(update_pause)
button4.on_clicked(update_play)


# plot audio signal
ax.plot(time, y)
plt.show()







