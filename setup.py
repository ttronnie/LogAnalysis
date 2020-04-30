import sys  

setup(
    name='logAnalysis',
    version='0.0.1',
    description='使用cxfreeze',
    options={
        'logAnalysis':build_exe_options
    },
    executables=[Executable('logAnalysis.py')]
)