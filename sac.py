#!/usr/bin/env python 
# *-* coding: iso-8859-1 *-*

# Function - Class definitions

import os,sys
from copy import deepcopy
import pylab as pyl
import shutil as sh

def unpack_c(chararray):
        S = ''
        for c in chararray:
                if c == ' ':
                        break
                S+=c
        return S

class sac(object):
	def __init__(self):
		self.delta  =  -12345.
		self.b      =  -12345.
		self.e      =  -12345.
		self.o      =  -12345.
		self.a      =  -12345.
		self.stla   =  -12345.
		self.stlo   =  -12345.
		self.evla   =  -12345.
		self.evlo   =  -12345.
		self.az     =  -12345.
		self.baz    =  -12345.
		self.gcarc  =  -12345.
		self.dist   =  -12345.
		self.nzyear =  -12345
		self.nzjday =  -12345
		self.nzhour =  -12345
		self.nzmin  =  -12345
		self.nzsec  =  -12345
		self.nzmsec =  -12345
		self.npts   =  -12345
		self.kts    =  []
		self.ts     =  []
		self.ko     = '-12345' 	
		self.ka     = '-12345' 
		self.kstnm  = '-12345'
		self.kcmpnm = '-12345'
		self.knetwk = '-12345'
		self.khole  = '-12345'
		self.id     = self.knetwk+'_'+self.kstnm+'_'+self.khole+'_'+self.kcmpnm
		self.depvar =  []
	def rsac(self,FILE,np=-1,datflag=1):
		try:
			fid     = open(FILE,'rb')
			self.delta   = pyl.fromfile(fid,'float32',   1)[0]
			fid.seek(20,0)
			self.b       = pyl.fromfile(fid,'float32',   1)[0]
			self.e       = pyl.fromfile(fid,'float32',   1)[0]
			fid.seek(28,0)
			self.o       = pyl.fromfile(fid,'float32',   1)[0]
			self.a       = pyl.fromfile(fid,'float32',   1)[0]
			fid.seek(40,0)
			self.ts      = pyl.fromfile(fid,'float32',  10)
			fid.seek(124,0)
			self.stla    = pyl.fromfile(fid,'float32',   1)[0]
			self.stlo    = pyl.fromfile(fid,'float32',   1)[0]
			fid.seek(140,0)
			self.evla    = pyl.fromfile(fid,'float32',   1)[0]
			self.evlo    = pyl.fromfile(fid,'float32',   1)[0]
			fid.seek(200,0)
			self.dist    = pyl.fromfile(fid,'float32',   1)[0]
			self.az      = pyl.fromfile(fid,'float32',   1)[0]
			self.baz     = pyl.fromfile(fid,'float32',   1)[0]
			self.gcarc   = pyl.fromfile(fid,'float32',   1)[0]
			fid.seek(280,0);
			self.nzyear  = pyl.fromfile(fid,  'int32',   1)[0]
			self.nzjday  = pyl.fromfile(fid,  'int32',   1)[0]
			self.nzhour  = pyl.fromfile(fid,  'int32',   1)[0]
			self.nzmin   = pyl.fromfile(fid,  'int32',   1)[0]
			self.nzsec   = pyl.fromfile(fid,  'int32',   1)[0]
			self.nzmsec  = pyl.fromfile(fid,  'int32',   1)[0]
			fid.seek(316,0)
			self.npts    = pyl.fromfile(fid,  'int32',   1)[0]
			fid.seek(440,0);
			self.kstnm   = unpack_c(pyl.fromfile(fid,'c',   8))			
			fid.seek(464,0);
			self.khole   = unpack_c(pyl.fromfile(fid,'c',   8))
			self.ko      = unpack_c(pyl.fromfile(fid,'c',   8))
			self.ka      = unpack_c(pyl.fromfile(fid,'c',   8))
			fid.seek(488,0);
			for i in xrange(10):
				self.kts.append(unpack_c(pyl.fromfile(fid,'c',   8)))
			fid.seek(600,0);
			self.kcmpnm  = unpack_c(pyl.fromfile(fid,'c',   8))
			self.knetwk  = unpack_c(pyl.fromfile(fid,'c',   8))
			fid.seek(632,0);
			if self.khole == '':
				self.khole = '--'
			self.id    = self.knetwk+'_'+self.kstnm+'_'+self.khole+'_'+self.kcmpnm
			if not datflag:
				fid.close()
				return
			np = int(np)
			if np < 0 or np > self.npts:
				np = self.npts
			if np > 0:
				self.depvar = pyl.array(pyl.fromfile(fid,'float32',np),dtype='d')
			fid.close()
			
		except IOError:
			sys.stderr.write('error reading file '+FILE+'!!!\n')
			sys.exit(1)


def zero_pad_start(t,sac,t0):
	tmin = t[0]
	dt   = sac.delta
	tpad = pyl.arange(tmin,t0-dt,-dt)
	if tpad[-1]>t0:
		tpad = pyl.append(tpad,tpad[-1]-dt)
	tpad = tpad[1:]
	tpad = tpad[::-1]
	tout = pyl.append(tpad,t)
	gout = pyl.append(0.0*tpad,sac.depvar)
	return tout,gout

