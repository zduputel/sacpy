
# SACPY

Sacpy is a simple python module that deals with binary SAC files.


## Dependencies
- python2 or python3
- numpy
- scipy

## Some instructions
To use sacpy, the sacpy directory must be placed in a path pointed by the PYTHONPATH environment variable.

To use sacpy, simply import the sacpy module
```
import sacpy
```
or for example
```
from sacpy import Sac
```
(Sac is the class used to manipulate SAC files)

In the Sac class, attributes have the same name as SAC header variables (see [the SAC documentation](http://ds.iris.edu/files/sac-manual/manual/file_format.html)). For example, the number of data points is given by `sacobj.npts`. The data points are in `sacobj.depvar`

### Reading/Writing SAC 
You can read binary SAC files using
```
sacobj = sacpy.Sac()
sacobj.read("SAC_FILENAME")
```
or
```
sacobj = sacpy.Sac("SAC_FILENAME")
```
In the first case, we first instantiate a Sac object and then read the SAC file. In the second case, we instantiate and read the SAC file on the fly. 

You can write binary SAC files using
```
sacobj.write("SAC_FILENAME")
```

### Copy sac object
To (deep) copy a Sac object sacobj in a new sacobjcopy, you can use:
```
sacobjcopy = sacobj.copy()
```

### Addition, substraction, multiplication
If you have 2 Sac objects sacobj1 and sacobj2 (including the same number of samples), you can add, substract, multiply waveforms of the 2 files using:
```
sacobj3=sacobj1+sacobj2
sacobj3=sacobj1-sacobj2
sacobj3=sacobj1*sacobj2
```
(data points in sacobj3 will be the sum, substraction and multiplication of sacobj1 and sacobj2). 

### Time integration
To perform time-integration, you can use:
```
sacobj.integrate()
```

### Interpolation
To interpolate the data trace to a new sampling step:
```
sacobj.interpolate(delta)
```
where delta is the new sampling step (after interpolation).

We use a sinc interpolation to avoid aliasing issues. This result in longer computation time than a linear interpolation.

### Decimation
To decimate the data:
```
sacobj.decimate(decimation_factor)
```
Currently, only the following decimation factors are available:
1, 2, 3, 5, 10, 20, 25, 30, 40, 50, 60, 75, 80, 90, 100, 120
Decimation includes a proper anti-aliasing FIR filter.

### Filtering
To filter the data:
```
sacobj.filter(freq, order, btype)
```
Applies a butterworth filter to the data. freq is the filter corner frequencie(s) (scalar or list of 2 scalars).
`btype` can be 'lowpass', 'highpass', 'bandpass' and 'bandstop'. Default values are `order=4` and `btype='lowpass'`.

### Instrument correction
To deconvolve, the instrument response using a dictionary of poles and zeros (PZ). 

The PZ dictionary can be built from a poles and zeros file using the function readPZ as follows:
```
import sacpy

s = sacpy.Sac('SAC_FILENAME') 
PZ = readPZ('SAC_PZs_FILENAME')
filtfreq = [0.001,0.005,0.01 0.1]
s.deconvresp(PZ,filtfreq)
```
To deal with the zero response at zero frequency, it is usually necessary to filter the signal during deconvolution.
filtfreq can be used for that by defining four frequencies (f1<f2<f3<f4). Taper is 1 between f2 and f3 and 0 below f1 
and above f4.  Frequencies f1 and f2 specify the high-pass filter while f3 and f4 specify the low-pass filter. 
The filters applied between f1 and f2 and between f3 and f4 are quarter cycles of a cosine wave.


### Dealing with time
To get the reference datetime, you can use:
```
sacobj.getnzdatetime()
```
Similarly, to get the origin, begin, end or arrival datetimes:
```
otime = sacobj.getodatetime()
btime = sacobj.getbdatetime()
etime = sacobj.getarrivaldatetimes()
```

To get a time-vector from the reference datetime:
```
timevec = sacobj.time()
```

To set the origin time, you can use:
```
sacobj.setotime(otime)
```
where otime is a datetime instance


To set arrival times, you can use:
```
sacobj.setarrivaltimes(phase_dict)
```
where phase_dict is a phase pick dictionary {phase_name: arrival_datetime)

### Fourier transform
To do a fourrier transform, you can use:
```
sacobj.fft()
```
The Fourier transform is done using the function numpy.fft.rfft
the result will be returned and also stored in self.depvar. 

If you want to get the corresponding frequency:
```
freqvec = sacobj.freq()
```

### Plot
To plot the seismogram with matplotlib.pyplot:
```
sacobj.plot()
```

To plot the amplitude spectum of the seismogram:
```
sacobj.fft()
sacobj.plot()
```
