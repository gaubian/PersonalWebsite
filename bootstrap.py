import os
import datetime as dt
import time

def erase_site():
    os.system('rm -rf site/*')

def pandoc(x):
    s = 'pandoc -B includes/head -A includes/foot -o site/' + x[:-3] + '.html src/' + x
    os.system(s)

def routine():
    erase_site()
    for filename in os.listdir('src/'):
        if filename.endswith('.md'):
            pandoc(filename)

while True:
    now = dt.datetime.now()
    time.sleep(1)
    changed = False

    for root, dirs,files in os.walk('.'):  
        for fname in files:
            path = os.path.join(root, fname)
            st = os.stat(path)    
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > now:
                changed = True

    if changed:
        routine()
