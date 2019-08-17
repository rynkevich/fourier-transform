import matplotlib.pyplot as plt


def plot_signal_analysis_and_filtering(filtered_signal_values, spectra, window_title, suptitle):
    fig, axes = plt.subplots(3)
    fig.canvas.set_window_title(window_title)
    fig.suptitle(suptitle)

    set_ax_title(axes[0], 'Filtered Signal')
    axes[0].plot(filtered_signal_values, color='orange')

    amplitude_spectrum, phase_spectrum = spectra

    set_ax_title(axes[1], 'Amplitude Spectrum')
    axes[1].stem(amplitude_spectrum, markerfmt=' ', use_line_collection=True)

    set_ax_title(axes[2], 'Phase Spectrum')
    axes[2].stem(phase_spectrum, markerfmt=' ', use_line_collection=True)

    plt.tight_layout(rect=(0, 0, 1, 0.9))
    plt.subplots_adjust(hspace=1)


def plot_signal_analysis_and_recovering(signal_values, spectra, recovered_signals_info, window_title, suptitle):
    fig, axes = plt.subplots(2, 2, figsize=(5, 5))
    fig.canvas.set_window_title(window_title)
    fig.suptitle(suptitle)

    set_ax_title(axes[0][0], 'Original Signal')
    axes[0][0].plot(signal_values, color='firebrick')

    amplitude_spectrum, phase_spectrum = spectra

    set_ax_title(axes[1][0], 'Amplitude Spectrum')
    axes[1][0].stem(amplitude_spectrum, markerfmt=' ', use_line_collection=True, linefmt='seagreen')

    set_ax_title(axes[1][1], 'Phase Spectrum')
    axes[1][1].stem(phase_spectrum, markerfmt=' ', use_line_collection=True, linefmt='seagreen')

    should_draw_legend = False
    set_ax_title(axes[0][1], 'Recovered Signal')
    for recovered_signal_values, recovered_signal_label in recovered_signals_info:
        axes[0][1].plot(recovered_signal_values, label=recovered_signal_label)
        if recovered_signal_label:
            should_draw_legend = True

    if should_draw_legend:
        axes[0][1].legend(loc=3, prop={'size': 9})

    plt.tight_layout(rect=(0, 0, 1, 0.9))
    plt.subplots_adjust(hspace=0.5, wspace=0.3)


def set_ax_title(ax, title):
    ax.set_title(title, pad='15', fontsize='10')
