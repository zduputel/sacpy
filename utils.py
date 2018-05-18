'''
Some utils for sacpy
'''
import numpy as np

def readPZ(ifile):
    ''' 
    Read Pole-zero file
    Args: 
        * ifile: PZ file name
    Returns a PZ dictionary
    '''

    # Read file
    f = open(ifile,'rt')
    L = f.readlines()
    f.close()
    
    # Main loop
    Nl = len(L)
    PZ = {}
    k = 0
    while k<Nl:
        l = L[k]
        # Commented line
        if l[0]=='*' or l[0]=='#':
            k += 1
            continue
        # Parse line
        items = l.strip().split()
        key = items[0]
        if key == 'ZEROS':
            nzeros = int(items[1])
            PZ['zeros'] = np.zeros((nzeros,))*0j
            for i in range(nzeros):
                try:
                    z = L[k+i+1].strip().split()
                    zr = float(z[0])
                    zc = float(z[1])
                    PZ['zeros'][i] = zr + zc*1.j
                except:
                    k += i
                    break
        elif key == 'POLES':
            npoles = int(items[1])
            PZ['poles'] = np.zeros((npoles,))*0j
            for i in range(npoles):
                try:
                    p = L[k+i+1].strip().split()
                    pr = float(p[0])
                    pc = float(p[1])
                    PZ['poles'][i] = pr + pc*1.j
                except:
                    k += i
                    break
        elif key == 'CONSTANT':
            PZ['Const'] = float(items[1])
        k += 1

    # Check if PZ is complete
    assert 'zeros' in PZ, 'zeros key must be specified in the PZ dictionary'
    assert 'poles' in PZ, 'poles key must be specified in the PZ dictionary'
    assert 'Const' in PZ, 'Const key must be specified in the PZ dictionary'
    
    # All done
    return PZ
