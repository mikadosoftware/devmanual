'''
SO I have a big file that I am kind of trying to split the work out into 144 parts

12 parts are *
144 are ** after a *

so parse it a bit
'''

def foo():
    f = 'index.pre'
    with open(f) as fo:
        txt = fo.read()
    currenttop=None
    resultsd = {}
    for line in txt.split("\n"):
        line=line.strip()
        if line.startswith('*') and not line.startswith('**'):
            currenttop=line
            resultsd.setdefault(line,[])
        if line.startswith('**'):
           resultsd[currenttop].append(line)
    show(resultsd)

def show(resultsd):
    s = ''
    toplevels = []
    for key, vals in resultsd.items():
        key = key.replace("* ","")
        toplevels.append(key)
        underline = "="*len(key)
        s += f"\n{key}\n{underline}\n"
        for idx, val in enumerate(vals):
            s += f"  {idx}\n"+ val.replace("**","")
    report = ''
    report += '\n* ' + '\n* '.join(toplevels)
    report += s
    print(report)
 
if __name__ == '__main__':
    foo()
