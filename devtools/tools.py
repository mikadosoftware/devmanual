
#parse out the pkg names needed to install the basics I want then download them

import subprocess

def extract_deps(toppkg):
    cmd = ['apt-rdepends', toppkg]
    out = subprocess.check_output(cmd)
    installorder_guess = []
    for l in out.split("\n"):
        if l.find("Depends:")>-1:
            pkgname = l.split()[1]
            installorder_guess.append(pkgname)

    return sorted(set(installorder_guess), reverse=True)

if __name__ =='__main__':
    for pkg in ['wireless-tools', 'firmware-realtek', 'wpasupplicant',
               ]:
        deps = extract_deps(pkg)
        deps.append(pkg)
        for p in deps:
            print "apt-get -d download %s" % p

