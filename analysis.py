from collections import namedtuple

import numpy as np

FourierAnalysisResult = namedtuple('FourierAnalysisResult', ['a_cos', 'a_sin', 'a', 'phi'])


def filter_signal(amplitudes, frequency_filter):
    return [amplitudes[i] if frequency_filter(i) else 0 for i in range(len(amplitudes))]


def recover_signal(amplitudes, phases, big_n):
    return polyharmonic_signal(amplitudes, phases, big_n, big_n // 2 - 1)


def polyharmonic_signal(amplitudes, phases, big_n, signals_num):
    return lambda i: sum(amplitudes[j] * np.cos(2 * np.pi * j * i / big_n - phases[j])
                         for j in range(signals_num))


def fourier_analyze(signal_values, big_n):
    fft_result = fft(signal_values)
    return get_fourier_analysis_result(fft_result, big_n)


def get_spectra(fourier_analysis_result):
    return fourier_analysis_result.a_cos, fourier_analysis_result.a_sin


def get_fourier_analysis_result(fft_result, big_n):
    a_sin, a_cos, a, phi = [], [], [], []
    for i, value in enumerate(fft_result):
        re = np.real(value) * 2 / big_n
        im = np.imag(value) * 2 / big_n
        a_cos.append(re)
        a_sin.append(im)
        a.append(np.hypot(re, im))
        phi.append(np.arctan2(-im, re))
    return FourierAnalysisResult(a_cos=a_cos, a_sin=a_sin, a=a, phi=phi)


def fft(x):
    x = np.asarray(x, dtype=float)
    big_n = x.shape[0]

    if big_n % 2 > 0:
        raise ValueError('Size of x must be a power of 2')
    elif big_n <= 32:
        return dft(x)

    x_even = fft(x[::2])
    x_odd = fft(x[1::2])
    factor = np.exp(-2j * np.pi * np.arange(big_n) / big_n)
    return np.concatenate([x_even + factor[:big_n // 2] * x_odd,
                           x_even + factor[big_n // 2:] * x_odd])


def dft(x):
    x = np.asarray(x, dtype=float)
    big_n = x.shape[0]
    n = np.arange(big_n)
    k = n.reshape((big_n, 1))
    big_m = np.exp(-2j * np.pi * k * n / big_n)
    return np.dot(big_m, x)
