from cffi import FFI
import numpy as np
import matplotlib.pyplot as plt

# Inicjalizacja CFFI
ffi = FFI()

# Ładowanie biblioteki Advantech DAQ
bdaqctrl = ffi.dlopen("libbiodaq.so")

# Utworzenie struktury DeviceInformation
info = ffi.new("DeviceInformation *")
info.Description = "PCI-1756, BID#0"  # Zastąp to opisem swojego urządzenia
info.DeviceNumber = -1
info.DeviceMode = bdaqctrl.ModeWriteWithReset
info.ModuleIndex = 0

# Utworzenie kontrolera wejścia/wyjścia
di = bdaqctrl.AdxInstantDiCtrlCreate()
do = bdaqctrl.AdxInstantDoCtrlCreate()

# Ustawienie urządzenia
bdaqctrl.InstantDiCtrl_setSelectedDevice(di, info)
bdaqctrl.InstantDoCtrl_setSelectedDevice(do, info)

# Generowanie sygnału
fs = 44100  # Częstotliwość próbkowania
duration = 3  # Czas trwania sygnału
t = np.linspace(0, duration, int(fs * duration), endpoint=False)
freq = 440  # Częstotliwość generowanego sygnału
y = 0.5 * np.sin(2 * np.pi * freq * t)

# Wyświetlanie sygnału
plt.figure(figsize=(15, 5))
plt.plot(t, y)
plt.title('Wykres sygnału dźwiękowego')
plt.ylabel('Amplituda')
plt.xlabel('Czas [s]')
plt.show()
