
from core_testfns import stub_fs
import todoinator

# this needs to be unit test or doctest module....

top = stub_fs([
             ('a', ['b',], ['foo.py',]),
             ('a/b', [], ['bar.py',])
            ])

l = list(todoinator.walk_tree(top))
assert('foo.py' in l[0])
assert('bar.py' in l[1])
