# coding=utf-8
import subprocess, os, codecs, json
from loguru import logger


def getFileMd5(filename):
    import hashlib
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename, 'rb')
    while 1:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()


def buildui(input, name, output, md5):
    _infile = os.path.join(input, '{n}.ui'.format(n=name))
    if not os.path.exists(_infile):
        logger.warning(f'{name}.ui not existed')
        return
    newmd5 = getFileMd5(_infile)
    if md5 == newmd5:
        logger.info(f'{name}.ui ignored')
        return None

    _outfile = os.path.join(output, '{n}.py'.format(n=name))
    p = subprocess.Popen(['pyuic5', _infile, '-o', _outfile], cwd='.')
    logger.warning(f'{name}.ui changed')
    p.wait()

    with codecs.open(_outfile, 'r', 'utf-8') as f:
        _old = f.read()

    return newmd5


def is_include_all_file(uics, outpath):
    all_autoui_file = []
    for i in os.listdir(outpath):
        f = os.path.join(outpath, i)
        if os.path.isfile(f):
            all_autoui_file.append(i)

    for i in uics:
        py_f = f'{i}.py'
        if py_f not in all_autoui_file:
            return False

    return True


def build_uidir(uipath, outpath):
    if not os.path.exists(outpath):
        os.makedirs(outpath)
        with open(os.path.join(outpath, '__init__.py'), 'w') as f:
            f.write('import os')
    _uics = []
    list_ui_path = os.listdir(uipath)
    for i in list_ui_path:
        _n, _p = os.path.splitext(i)
        if _p == '.ui':
            _uics.append(_n)
    if not os.path.exists('cache.md5'):
        md5s = {}
        for i in _uics:
            _infile = '{n}.ui'.format(n=i)
            md5s[i] = 1
        md5s = md5s
    else:
        with codecs.open('cache.md5', 'r', 'utf-8') as f:
            md5s = json.loads(f.read())
        if not is_include_all_file(_uics, outpath):
            md5s = {}
            for i in _uics:
                _infile = '{n}.ui'.format(n=i)
                md5s[i] = 1
            md5s = md5s

    for i in _uics:
        if i not in md5s:
            md5s[i] = '0'
        changed = buildui(uipath, i, outpath, md5s[i])
        if changed:
            md5s[i] = changed
    with codecs.open('cache.md5', 'w', 'utf-8') as f:
        f.write(json.dumps(md5s))
