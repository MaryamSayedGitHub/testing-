import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import tkinter as tk

def generate_signals(amplitude, phase_shift, analog_freq, sampling_freq, signal_type):
    # Generate time axiss
    # duration = 1.0  # Duration of the signal in seconds
    t = np.linspace(0, 13, 1000)

    # Generate analog signals
    if signal_type == "Sine":
        analog_signal = amplitude * np.sin(2 * np.pi * analog_freq * t + phase_shift)
    else:
        analog_signal = amplitude * np.cos(2 * np.pi * analog_freq * t + phase_shift)

    # digital_signal = signal.resample(analog_signal, len(t))

    return analog_signal, digital_signal

def plot_signals(amplitude, phase_shift, analog_freq, sampling_freq, signal_type):
    analog_signal, digital_signal = generate_signals(amplitude, phase_shift, analog_freq, sampling_freq, signal_type)

    # Plot analog and digital signals
    plt.figure(figsize=(10, 4))
    plt.subplot(2, 1, 1)
    plt.plot(analog_signal[:len(analog_signal)//15], color='blue')
    plt.title('Analog Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    if (sampling_freq==0) and (sampling_freq<2*analog_freq):
        print("no digital signal")
    else:
        plt.subplot(2, 1, 2)
        plt.stem(digital_signal[:len(analog_signal)//15], markerfmt='ro', linefmt='r-')
        plt.title('Digital Signal')
        plt.xlabel('Time')
        plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()

def generate_button_clicked():
    amplitude = float(amplitude_entry.get())
    phase_shift = float(phase_shift_entry.get())
    analog_freq = float(analog_freq_entry.get())
    sampling_freq = float(sampling_freq_entry.get())
    signal_type = signal_type_var.get()

    plot_signals(amplitude, phase_shift, analog_freq, sampling_freq, signal_type)

# Create the GUI
window = tk.Tk()
window.title("Signal Generator")

amplitude_label = tk.Label(window, text="Amplitude:")
amplitude_label.pack()
amplitude_entry = tk.Entry(window)
amplitude_entry.pack()

phase_shift_label = tk.Label(window, text="Phase Shift:")
phase_shift_label.pack()
phase_shift_entry = tk.Entry(window)
phase_shift_entry.pack()

analog_freq_label = tk.Label(window, text="Analog Frequency:")
analog_freq_label.pack()
analog_freq_entry = tk.Entry(window)
analog_freq_entry.pack()

sampling_freq_label = tk.Label(window, text="Sampling Frequency:")
sampling_freq_label.pack()
sampling_freq_entry = tk.Entry(window)
sampling_freq_entry.pack()

signal_type_label = tk.Label(window, text="Signal Type:")
signal_type_label.pack()

signal_type_var = tk.StringVar(value="Sine")
sine_radio_button = tk.Radiobutton(window, text="Sine", variable=signal_type_var, value="Sine")
sine_radio_button.pack()

cosine_radio_button = tk.Radiobutton(window, text="Cosine", variable=signal_type_var, value="Cosine")
cosine_radio_button.pack()

generate_button = tk.Button(window, text="Generate Signals", command=generate_button_clicked)
generate_button.pack()

window.mainloop()