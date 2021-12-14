# coding=utf-8
import subprocess, os, codecs, json


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


def buildui(name, output, md5):
    _infile = '{n}.ui'.format(n=name)
    if not os.path.exists(_infile):
        print(f'\033[94m{_infile} not existed \033[0m')
        return
    newmd5 = getFileMd5(_infile)
    if md5 == newmd5:
        print(f'\033[92m{_infile} ignored \033[0m')
        return None

    _outfile = os.path.join(output, '{n}.py'.format(n=name))
    p = subprocess.Popen(['pyuic5', _infile, '-o', _outfile], cwd='.')
    print('\033[91m' + name + ' changed ' + '\033[0m')
    p.wait()

    with codecs.open(_outfile, 'r', 'utf-8') as f:
        _old = f.read()
    _new = _old.replace('import yukina_rc', '').replace('import img_rc', '')
    with codecs.open(_outfile, 'w', 'utf-8') as f:
        f.write(_new)

    return newmd5


def buildqrc(name, output):
    _outfile = os.path.join(output, '{n}_rc.py'.format(n=name))
    p = subprocess.Popen(['pyrcc5', '{n}.qrc'.format(n=name), '-o', _outfile], cwd='.')
    p.wait()


if __name__ == '__main__':
    _uics = []
    for i in os.listdir('.'):
        _n, _p = os.path.splitext(i)
        if _p == '.ui':
            _uics.append(_n)
    if not os.path.exists('cache.md5'):
        md5s = {}
        for i in _uics:
            _infile = '{n}.ui'.format(n=i)
            md5s[i] = 1
        md5s['yukina'] = 1
        md5s = md5s
    else:
        with codecs.open('cache.md5', 'r', 'utf-8') as f:
            md5s = json.loads(f.read())

    for i in _uics:
        if i not in md5s:
            md5s[i] = '0'
        changed = buildui(i, r'..\auto_ui', md5s[i])
        if changed:
            md5s[i] = changed
    yukina_md5 = getFileMd5('img.qrc')
    if 'img' not in md5s or md5s['img'] != yukina_md5:
        buildqrc('img', r'..\auto_ui')
        md5s['img'] = yukina_md5
        print('\033[91m' + 'qrc file' + ' changed ' + '\033[0m')
    else:
        print(f'\033[92mqrc file ignored \033[0m')
    with codecs.open('cache.md5', 'w', 'utf-8') as f:
        f.write(json.dumps(md5s))
