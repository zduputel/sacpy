
#SACPY

Sacpy is a simple python module that deals with binary SAC files.


## Dependencies
- python2 or python3
- numpy

## Some instructions
To use sacpy, the sacpy directory must be placed in a path pointed by the PYTHONPATH environment variable.

To use sacpy, simply import the sacpy module
```
import sacpy
```
or 
```
from sacpy import sac
```
(sac is the class used to manipulate SAC files)

In the sac class, attributes have the same name as sac header variables (see [the SAC documentation](http://ds.iris.edu/files/sac-manual/manual/file_format.html)). For example, the number of data points is given by:
```
sacobj.npts
```

###Reading/Writing SAC 
You can read binary SAC files using
```
sacobj = sacpy.sac()
sacobj.read("SAC_FILENAME")
```
or
```
sacobj = sacpy.sac("SAC_FILENAME")
```
In the first case, we first instantiate a sac object and then read the SAC file. In the second case, we instantiate and read the sac file on the fly. 

You can write binary SAC files using
```
sacobj.write("SAC_FILENAME")
```

###Copy sac object
To (deep) copy a sac object sacobj in a new sacobjcopy, you can use:
```
sacobjcopy = sacobj.copy()
```

###Addition, substraction, multiplication
If you have 2 sac objects sacobj1 and sacobj2 (including the same number of samples), you can add, substract, multiply waveforms of the 2 files using:
```
sacobj3=sacobj1+sacobj2
sacobj3=sacobj1-sacobj2
sacobj3=sacobj1*sacobj2
```
(data in sacobj3 will be the sum, substraction and multiplication of sacobj1 and sacobj2). 

###Time integration
To perform time-integration, you can use:
```
sacobj.integrate()
```

###Interpolation
To (linearly) interpolate the data trace to a new sampling step:
```
sacobj.interpolate(delta)
```
where delta is the new sampling step (after interpolation). 

###Decimation
To decimate the data:
```
sacobj.decimate(decimation_factor)
```
Currently, only the following decimation factors are available:
1, 2, 3, 5, 10, 20, 25, 30, 40, 50, 60, 75, 80, 90, 100, 120
Decimation includes a proper anti-aliasing FIR filter.

###Time
To get the reference datetime, you can use:
```
sacobj.getnzdatetime()
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



