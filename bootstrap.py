import os

def erase_site():
    os.system('rm -rf site/*')

def pandoc(x):
    s = 'pandoc -B includes/head -A includes/foot -o site/' + x[:-3] + '.html src/' + x
    os.system(s)

erase_site()
for filename in os.listdir('src/'):
    if filename.endswith('.md'):
        pandoc(filename)
