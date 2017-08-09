"""Shell redirecting is often painful to remember

0 - file descriptor for stdin
1 - file descriptor for stdout
2 - file descriptor for stderr

> - redirect
&X - the stream as represented by file descriptor X
     (this needs a little explaining - )


    $ python demo.py 
    Countdown 5
    Countdown 5
    Countdown 5
    Countdown 5
    Countdown 5
    ^CTraceback (most recent call last):
      File "demo.py", line 24, in <module>
        run()
      File "demo.py", line 21, in run
        time.sleep(0.5)
    KeyboardInterrupt

    $ python demo.py 
    Countdown 5
    Countdown 4
    Countdown 3
    Countdown 2
    Countdown 1
    Traceback (most recent call last):
      File "demo.py", line 25, in <module>
        run()
      File "demo.py", line 23, in run
        raise IOError("Fake error")
    IOError: Fake error

    $ python demo.py > stdin.log
    Traceback (most recent call last):
      File "demo.py", line 25, in <module>
        run()
      File "demo.py", line 23, in run
        raise IOError("Fake error")
    IOError: Fake error

    $ python demo.py 1> stdin.log
    Traceback (most recent call last):
      File "demo.py", line 25, in <module>
        run()
      File "demo.py", line 23, in run
        raise IOError("Fake error")
    IOError: Fake error

    $ python demo.py 2> stderr.log
    Countdown 5
    Countdown 4
    Countdown 3
    Countdown 2
    Countdown 1

    $ cat stderr.log 
    Traceback (most recent call last):
      File "demo.py", line 25, in <module>
        run()
      File "demo.py", line 23, in run
        raise IOError("Fake error")
    IOError: Fake error

    $ python demo.py 2>&1 outAndErr.log
    Countdown 5
    Countdown 4
    Countdown 3
    Countdown 2
    Countdown 1
    Traceback (most recent call last):
      File "demo.py", line 25, in <module>
        run()
      File "demo.py", line 23, in run
        raise IOError("Fake error")
    IOError: Fake error

    $ python demo.py 2>&1 > outAndErr.log
    Traceback (most recent call last):
      File "demo.py", line 25, in <module>
        run()
      File "demo.py", line 23, in run
        raise IOError("Fake error")
    IOError: Fake error


But those last two are supposed to work right????

No

    $ python demo.py &> err.log
    $ cat err.log 
    Countdown 5
    Countdown 4
    Countdown 3
    Countdown 2
    Countdown 1
    Traceback (most recent call last):
      File "demo.py", line 25, in <module>
        run()
      File "demo.py", line 23, in run
        raise IOError("Fake error")
    IOError: Fake error

    `&>` is a bash-4-ism that redirects stderr and stdout to the file after.

    `2&>1` redirects stderr to the stdout stream.  `> file` then redirects the 1
    stream to file.  The first redirect is saying "send the errors to console".
    Then we say "send the stdout to a file."  There is no clever work that then
    goes back to fix it for what we meant.

    1 is not a fixed memory address, it is a pointer to a memory address / file.
    This means we can change the value of 1

    $ python demo.py > stderr.log 2&>1
    $ 

    Now that does work ....



Capturing FIle handles
----------------------



http://www.tldp.org/LDP/abs/html/io-redirection.html

"""

##simple "program" - send some output, then error.
import time
def run():
   c = 5
   while c > 0:
      print "Countdown %s" % c
      c -= 1
      time.sleep(0.5)
   raise IOError("Fake error")

run()