DATS = ['0.0.dat', '0.1.dat', '0.2.dat', '0.3.dat', '0.4.dat', '0.5.dat', '0.6.dat', '0.7.dat', '0.8.dat', '0.9.dat',
        '1.0.dat', '1.1.dat', '1.2.dat', '1.3.dat', '1.4.dat', '1.5.dat', '1.6.dat', '1.7.dat', '1.8.dat', '1.9.dat',
        '2.0.dat', '2.1.dat', '2.2.dat']

path = r'C:\Users\hufei\Desktop\water'
if __name__ == '__main__':
    import os
    import pickle

    dts = {}
    for i in DATS:
        print(i)
        file = os.path.join(path, i)
        with open(file, 'rb') as f:
            dts[i] = f.read()

    with open('cache.dt', 'wb') as f:
        pickle.dump(dts, f)
