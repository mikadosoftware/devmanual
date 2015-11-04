
'''
Core mikado test functions

Useful things for unit testing


'''
import tempfile
import os

def stub_fs(simpletriple):
    '''

    files as triples expects a triple 
    (currdirpath_relative, dirs_in_currdir, files_in_currdir)
    [('a', ['b',], ['foo.py',]),
     ('a/b', [], ['bar.py',]) 
    ]
    '''
    top = tempfile.mkdtemp()
    for currdir, dirs_in_currdir, files_in_currdir in simpletriple:
        currdirpath = os.path.join(top, currdir)
        try:
            os.makedirs(currdirpath)
        except:
            pass
        
        for file in files_in_currdir:
            filepath = os.path.join(currdirpath, file)
            open(filepath, 'w')
        for dir in dirs_in_currdir:
            dirpath = os.path.join(currdirpath, dir)
            os.makedirs(dirpath)
    return top

if __name__ == '__main__':
    print stub_fs([
             ('a', ['b',], ['foo.py',]),
             ('a/b', [], ['bar.py',])
            ])
    
