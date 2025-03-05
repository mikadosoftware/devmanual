'''
SO I have a big file that I am kind of trying to split the work out into 144 parts

12 parts are *
144 are ** after a *

so parse it a bit
'''
import os

def parse_stars(f):
    
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
    nextlevelsd = {}
    for key, vals in resultsd.items():
        key = key.replace("* ","")
        toplevels.append(key)
        underline = "="*len(key)
        s += f"\n{key}\n{underline}\n"
        for idx, val in enumerate(vals):
            s += f"  {idx}\n"+ val.replace("**","")
            nextlevelsd.setdefault(key, []).append(val)

    report = ''
    report += '\n* ' + '\n* '.join(toplevels)
    report += s
    i = 0
    for onestar, twostars in nextlevelsd.items():
        print(f"* {onestar}")
        for twostar in twostars:
            i+=1
    print("Total two stars:", i)
    output_chapters(nextlevelsd)

def safename(txt):
    import string
    safeletters = string.ascii_letters+string.digits
    tmp = ''

    for char in txt:
        if char in safeletters:
            tmp += char
        if char == ' ':
            tmp += '_'
    if tmp.startswith("_"):
        tmp = tmp[1:]
    tmp = tmp.lower()
    return tmp


root = '/home/pbrian/projects/devmanual/docs/newchapters'

def output_chapters(nextlevelsd):
    for onestar, twostars in nextlevelsd.items():
        s_onestar = safename(onestar)
        thissection = os.path.join(root, s_onestar)
        os.makedirs(thissection)        
        for twostar in twostars:
            s_twostar = safename(twostar)
            path = os.path.join(thissection, s_twostar+".rst")
            with open(path, 'w') as fo:
                title = twostar.replace("*","").strip()
                fo.write(title + "\n" + "="*len(title)+"\n\nTBD\n")

def build_index_rst():
    print("My Book\n=======\n")
    for x in os.listdir(root):
        print(f'''.. toctree::
   :maxdepth: 1
   :caption: {x}:
   :glob: 

   /newchapters/{x}/*

 ''')

if __name__ == '__main__':
    import sys
    f = sys.argv[1]
    if f == 'build_index':
        build_index_rst()
    else:
        parse_stars(f)
