import matplotlib.pyplot as plt

def plot_ecg(signal, title="ECG Signal", limit=2000):
    plt.figure(figsize=(12,4))
    plt.plot(signal[:limit])
    plt.title(title)
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.show()
    input("Press Enter to continue...")  # 👈 FORCE WAIT

def plot_r_peaks(signal, peaks, limit=2000):
    plt.figure(figsize=(12,4))
    plt.plot(signal[:limit])
    valid_peaks = peaks[peaks < limit]
    plt.plot(valid_peaks, signal[valid_peaks], "ro")
    plt.title("R-Peak Detection")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.show()
    input("Press Enter to continue...")  # 👈 FORCE WAIT
