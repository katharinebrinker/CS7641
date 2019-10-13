Code can be located at: 
https://github.com/katharinebrinker/cs7641-p2

Required for running the code:

install jython https://www.jython.org/
-- note: requires <= python 2.7
-- note: jython 2.7.1 didn't work on windows (DLL issue) -> use 2.7.0 instead

The ABAGAIL jar used is included with the code

Add jython to the path environment variable

To run these files in PyCharm (or another IDE), add jython as the project interpreter

You may need to change the jar location in the code, if the relative path doesn't work

print_graphs will have to be run in a different pycharm project / from the terminal because jython doesn't play nice with pandas / numpy
(you will need to change the relative paths to csv / png files)

The algorithm comparisons and neural network comparisons can be run with:
jython continuous-peaks.py
jython flipflop.py
jython salesman.py
jython neural-nets-wine.py





