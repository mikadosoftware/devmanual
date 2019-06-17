import subprocess

def main():
    """
    """
    #build the marketingsite
    #its fixed HTML - need to improve it.
    
    #grab html from book put into marketingsite
    subprocess.call("rm -rf /tmp/marketingsite",
                     shell=True)
    subprocess.call("mkdir -p /tmp/marketingsite/softwaremind",
                     shell=True)
    subprocess.call("cp -r docs/_build/html/* /tmp/marketingsite/softwaremind",
                     shell=True)
    subprocess.call("cp -r marketingsite/* /tmp/marketingsite/",
                     shell=True)

    #move pdf ver to maretingsite
    subprocess.call("cp -r docs/_build/latex/*.pdf /tmp/marketingsite/",
                     shell=True)

    
    #We have index.pre which is preprocesses into .rst
    #cann0t remeber why but kill it off after all generation
    subprocess.call("rm docs/index.rst",
                     shell=True)

    #upload marketing site to AWS

    

if __name__ == '__main__':
    main()
