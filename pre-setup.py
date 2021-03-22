import os, subprocess, sys

scriptPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, scriptPath)

# Install wheels first
whlPath = os.path.join(scriptPath, 'wheels')
depend_links = os.listdir(whlPath)

# Make sure GDAL is installed prior to fiona
ind = [i for i,s in enumerate(depend_links) if 'GDAL' in s]
ind = ind[0]
depend_links.insert(0, depend_links.pop(ind))
for whl in depend_links:
    whl = os.path.join(whlPath, whl)
    subprocess.call(['python', '-m', 'pip', 'install', whl])

# Once finished, call full setup
subprocess.call(['pip', 'install', '-e', '.'])