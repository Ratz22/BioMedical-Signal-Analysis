from data.ecg_loader import load_ecg
import matplotlib.pyplot as plt

signal, fs = load_ecg()

plt.plot(signal[:2000])
plt.title("ECG Signal Test")
plt.show()
