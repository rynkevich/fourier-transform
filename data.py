from math import cos, pi

N = 256
HARMONICS_IN_POLYHARMONIC_SIGNAL = 30
LOW_CUT = 5
HIGH_CUT = 20

SIGNALS = [
    lambda i: 10 * cos(2 * pi * i / N),
    lambda i: 10 * cos(2 * pi * i / N - pi / 2),
    lambda i: 20 * cos(2 * pi * 10 * i / N),
    lambda i: 100 * cos(2 * pi * 20 * i / N - pi / 4),
    lambda i: 30 * cos(2 * pi * i / N - 3 * pi / 4),
    lambda i: 50 * cos(2 * pi * i / N - pi / 3)
]

SIGNAL_LABELS = [
    r'$x(i) = 10\cos(\frac{2 \pi i}{N})$',
    r'$x(i) = 10\cos(\frac{2 \pi i}{N} - \frac{\pi}{2})$',
    r'$x(i) = 20\cos(\frac{2 \pi 10 i}{N})$',
    r'$x(i) = 100\cos(\frac{2 \pi 20 i}{N} - \frac{\pi}{4})$',
    r'$x(i) = 30\cos(\frac{2 \pi i}{N} - \frac{3\pi}{4})$',
    r'$x(i) = 50\cos(\frac{2 \pi i}{N} - \frac{\pi}{3})$',
]

AMPLITUDES = [
    [1, 3, 5, 8, 10, 12, 16],
    [1, 2, 5, 7, 9, 13, 18],
    [1, 3, 4, 10, 11, 14, 17],
    [2, 3, 5, 9, 10, 12, 15],
    [3, 5, 6, 8, 10, 13, 16],
    [1, 5, 7, 8, 9, 10, 17]
]

PHASES = [
    [pi / 6, pi / 4, pi / 3, pi / 2, 3 * pi / 4, pi],
    [pi / 6, pi / 4, pi / 3, pi / 2, 3 * pi / 4, pi],
    [pi / 6, pi / 4, pi / 3, pi / 2, 3 * pi / 4, pi],
    [pi / 6, pi / 4, pi / 3, pi / 2, 3 * pi / 4, pi],
    [pi / 6, pi / 4, pi / 3, pi / 2, 3 * pi / 4, pi],
    [pi / 6, pi / 4, pi / 3, pi / 2, 3 * pi / 4, pi]
]


def get_initial_data(variant):
    return SIGNALS[variant - 1], SIGNAL_LABELS[variant - 1], AMPLITUDES[variant - 1], PHASES[variant - 1]
