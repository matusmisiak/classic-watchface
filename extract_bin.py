import os
import glob
import zipfile
import shutil

def get_filename(path):
    return os.path.splitext(os.path.split(path)[1])[0]

bindir = 'dist/'
result = bindir

temp = os.path.join(bindir, 'temp/')

for path in glob.glob(os.path.join(bindir, '*.zab')):
    dir = os.path.split(path)[0]
    os.mkdir(temp)
    with zipfile.ZipFile(path, 'r') as zab:
        zab.extractall(temp)
    for path in glob.glob(os.path.join(temp, '*.zpk')):
        with zipfile.ZipFile(path, 'r') as zpk:
            zpk.extract('device.zip', temp)
        shutil.copyfile(
            os.path.join(temp, 'device.zip'),
            os.path.join(result, get_filename(path)+'.bin')
        )
    shutil.rmtree(temp)

os.rename(os.path.join(result, 'l66.bin'), os.path.join(result, 'EUKAUnKtyVwphnAmfCbDoimbkKjswdTg.bin'))
