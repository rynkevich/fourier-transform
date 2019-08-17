import random
import sys
import matplotlib.pyplot as plt

from analysis import fourier_analyze, recover_signal, polyharmonic_signal, filter_signal, get_spectra
from data import N, HARMONICS_IN_POLYHARMONIC_SIGNAL, LOW_CUT, HIGH_CUT, get_initial_data
from plotter import plot_signal_analysis_and_recovering, plot_signal_analysis_and_filtering

POLYHARMONIC_SIGNAL_LABEL = r'$x(i) = \sum_{j=1}^{30} B_j\cos(\frac{2 \pi j i}{N} - \phi_j)$'


def main():
    variant = int(sys.argv[1])
    test_signal, test_signal_label, amplitudes, phases = get_initial_data(variant)

    polyharmonic_test_signal = random_signal(amplitudes, phases)
    polyharmonic_test_signal_values = tuple(polyharmonic_test_signal(i) for i in range(N))
    fourier_analysis_result = fourier_analyze(polyharmonic_test_signal_values, N)

    task_5(fourier_analysis_result.a, fourier_analysis_result.phi)
    task_3(polyharmonic_test_signal_values, fourier_analysis_result)
    task_2(test_signal, test_signal_label)

    plt.show()


def task_2(test_signal, test_signal_label):
    signal_values = tuple(test_signal(i) for i in range(N))
    fourier_analysis_result = fourier_analyze(signal_values, N)
    recovered_test_signal = recover_signal(fourier_analysis_result.a, fourier_analysis_result.phi, N)
    recovered_signal_values = tuple(recovered_test_signal(i) for i in range(N))

    plot_signal_analysis_and_recovering(signal_values, get_spectra(fourier_analysis_result),
                                        [(recovered_signal_values, None)],
                                        'Signal Analysis - Discrete Fourier Transform (#1)',
                                        test_signal_label)


def task_3(signal_values, fourier_analysis_result):
    recovered_signal = recover_signal(fourier_analysis_result.a, fourier_analysis_result.phi, N)
    recovered_signal_values = tuple(recovered_signal(i) for i in range(N))
    recovered_without_phases_signal = recover_signal(fourier_analysis_result.a, [0] * N, N)
    recovered_without_phases_signal_values = tuple(recovered_without_phases_signal(i) for i in range(N))

    recovered_signals_info = [
        (recovered_signal_values, 'With phases'),
        (recovered_without_phases_signal_values, 'W/o phases')
    ]
    plot_signal_analysis_and_recovering(signal_values, get_spectra(fourier_analysis_result), recovered_signals_info,
                                        'Signal Analysis - Discrete Fourier Transform (#2)',
                                        POLYHARMONIC_SIGNAL_LABEL)


def task_5(amplitudes, phases):
    high_pass_filter = lambda freq: freq >= LOW_CUT
    low_pass_filter = lambda freq: freq <= HIGH_CUT
    band_pass_filter = lambda freq: LOW_CUT <= freq <= HIGH_CUT

    demonstrate_signal_filtering(amplitudes, phases, band_pass_filter, 5,
                                 f'{POLYHARMONIC_SIGNAL_LABEL} (Band-Pass Filter)')
    demonstrate_signal_filtering(amplitudes, phases, low_pass_filter, 4,
                                 f'{POLYHARMONIC_SIGNAL_LABEL} (Low-Pass Filter)')
    demonstrate_signal_filtering(amplitudes, phases, high_pass_filter, 3,
                                 f'{POLYHARMONIC_SIGNAL_LABEL} (High-Pass Filter)')


def demonstrate_signal_filtering(amplitudes, phases, frequency_filter, figure_num, suptitle):
    filtered_signal_amplitudes = filter_signal(amplitudes, frequency_filter)
    filtered_signal = recover_signal(filtered_signal_amplitudes, phases, N)
    filtered_signal_values = tuple(filtered_signal(i) for i in range(N))
    fourier_analysis_result = fourier_analyze(filtered_signal_values, N)
    spectra = get_spectra(fourier_analysis_result)

    plot_signal_analysis_and_filtering(filtered_signal_values, spectra,
                                       f'Signal Analysis - Discrete Fourier Transform (#{figure_num})',
                                       suptitle)


def random_signal(amplitudes, phases):
    harmonic_amplitudes = tuple(random.choice(amplitudes) for _ in range(HARMONICS_IN_POLYHARMONIC_SIGNAL))
    harmonic_phases = tuple(random.choice(phases) for _ in range(HARMONICS_IN_POLYHARMONIC_SIGNAL))
    return polyharmonic_signal(harmonic_amplitudes, harmonic_phases, N, HARMONICS_IN_POLYHARMONIC_SIGNAL)


if __name__ == '__main__':
    main()
