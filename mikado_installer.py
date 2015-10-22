

# trivial install helper
# aim is to run apt-get --dry-run first, grab what should be installed and add to a archive
# then run isntall 

# for sudo issues I may need shell=True to pass my permissions to child process

import subprocess
import sys

def archivelog(txt):
    f = '/var/mikado/mikado-installer.log'
    fo = open(f, "a")
    fo.write(txt)
    fo.close()

def parserun(pkgs, dryrun=True):
    archive = ''
    output = ''
    for pkg in pkgs:
        if dryrun:
            cmd = ['apt-get', '-s', 'install', pkg]
        else:
            cmd = ['apt-get', '-y', 'install', pkg]
        archive += "\n" + pkg 
        o = subprocess.check_output(cmd)
        for line in o.split("\n"):
            if line.find("Inst") == 0:
                archive += "\n" + line
        print archive
        print o
        
        archivelog(archive)
        archivelog(o)
  

if __name__ == '__main__':
    pkgs = sys.argv[1:]
    parserun(pkgs)
    parserun(pkgs, dryrun=False)

