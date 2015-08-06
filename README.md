
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

####Reading SAC file
You can read binary SAC files using
```
sacobj = sacpy.sac("SAC_FILENAME")
```
or 
```
sacobj = sacpy.sac()
sacobj.rsac("SAC_FILENAME")
```

####Writing SAC file
You can write binary SAC files using
```
sacobj.wsac("SAC_FILENAME")
```

