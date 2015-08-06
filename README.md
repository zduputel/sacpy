
#SACPY

Sacpy is a simple python module that deals with binary SAC files.

### Dependencies
- Numpy

### Some instructions
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

####Reading/Writing SAC 
You can read binary SAC files using
```
sacobj = sacpy.sac()
sacobj.rsac("SAC_FILENAME")
```
or
```
sacobj = sacpy.sac("SAC_FILENAME")
```
In the first case, we first instantiate a sac object and then read the SAC file. In the second case, we instantiate and read the sac file on the fly. 

You can write binary SAC files using
```
sacobj.wsac("SAC_FILENAME")
```

####Copy sac object
To (deep) copy a sac object sacobj in a new sacobjcopy, you can use:
```
sacobjcopy = sacobj.copy()
```

####Addition, substraction, multiplication
If you have 2 sac objects sacobj1 and sacobj2 (including the same number of samples), you can add, substract, multiply waveforms of the 2 files using:
```
sacobj3=sacobj1+sacobj2
sacobj3=sacobj1-sacobj2
sacobj3=sacobj1*sacobj2
```
(data in sacobj3 will be the sum, substraction and multiplication of sacobj1 and sacobj2). 

####Time integration
To perform time-integration, you can use:
```
sacobj.integrate()
```

####Time
To get the reference datetime, you can use:
```
sacobj.getnzdatetime()
```

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





