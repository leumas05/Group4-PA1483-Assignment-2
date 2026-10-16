
##How to reproduce coupling
In Codescene there is a architectural components tab, where you can edit what components are to be used.

I recomend using codescenes "generate components" option while in the correct directory in the architectural components editor.
This will create components of every sub-directory within the directory you choose. 

Here are the components i got:

#Top level components:

pandas/pandas/...

core
io	
plotting	
tseries	
_libs
compat
util	
errors
_config
tests
_testing


#Lower level components


pandas/pandas/core/...

_numba
array_algos
arrays
computation
dtypes
groupby
indexers
indexes
interchange
internals
methods
ops
reshape
sparse
strings
tools
util
window


#Purpose:
This is how different achitectural components where defined in Codescene, in order to perform analysis. 
The top layer is for how different components are coupled for the general system. Lower level is for the components inside the core directory.

