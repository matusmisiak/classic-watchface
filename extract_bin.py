import os
import glob
import zipfile
import shutil

def get_filename(path):
    return os.path.splitext(os.path.split(path)[1])[0]

app_id = 'EUKAUnKtyVwphnAmfCbDoimbkKjswdTg'
bindir = 'dist/'
result = os.path.join(bindir, app_id)

temp = os.path.join(bindir, 'temp/')

os.mkdir(result)

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

os.rename(glob.glob(os.path.join(result, 'l66*.bin'))[0], os.path.join(result, app_id+'.bin'))

shutil.copyfile('assets/l66/images/icon.png', os.path.join(result, 'icon.png'))
shutil.copyfile('infos.xml', os.path.join(result, 'infos.xml'))
