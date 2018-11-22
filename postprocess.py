import subprocess

def main():
    """
    """
    #build the marketingsite
    #its fixed HTML - need to improve it.
    
    #grab html from book put into marketingsite
    subprocess.call("cp -r docs/_build/html/* marketingsite/softwaremind/",
                     shell=True)
    
    #upload marketing site to AWS

    

if __name__ == '__main__':
    main()
