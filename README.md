# PyIIR2

A Python IIR filters library. Currently it has Butterworth, Bessel Chebyshev 1/2 type of filters. All of them have been implemented as cascaded 2nd order filters.

## Getting Started



### Prerequisites

This software requires that the Python 'scipy' library is available on the computer to be ran. Everything else is self-contained within the repository.

### Installing

1) Clone the repository.

2) Include the relevant filter type class in your project.
```
from Bessel import Bessel
```

3) Create a new instance of the class.
```
my_filter = Bessel()
```

4) Set it up as the filter that you intend to use (lowpass, highpass, etc.)
```
my_filter.bandPass(6, 40, 60, 1000)
```

5) Run the filter command on the scalar data to be filtered.
```
result = my_filter.filter(input)
```

And repeat until finished.

### Example

Test.py script reads in an ECG dat file and filter out the 50Hz harmonic using a 4th order lowpass Chebyshev 2 filter. Simply clone the repository, run the script and observe the graphs to notice the diminished 50Hz harmonic and the cleaner ECG signal.

Feel free to play around with it :)

### Function signatures

All Bessel and Butterworth have the following function signatures:
```
(order, cut_off, sampling_frequency)
```
except the band filters:
```
(order, cut_off1, cut_off2, sampling_frequency)
```

Both Chebyshev type filters have an extra parameter to specify the passband ripple or attenuation of the filter.
```
(order, ripple, cut_off1, cut_off2, sampling_frequency)
```

## Authors

* **Borislav Gachev** - *Initial work* - [dunker4o](https://github.com/dunker4o)

## License

This project is licensed under the MIT License - see the [Open Source MIT](https://opensource.org/licenses/MIT) file for details

## Acknowledgments

* Bernd Porr for motivating me to publish this work online and supporting my learning process to do it in first place
* Martin Podlubny for opening my eyes to Sourcetree
* My soft bed which I've been avoiding lately...
