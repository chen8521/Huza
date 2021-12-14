from loguru import logger
from util.cache import output_data, all_json_data
from util.cache2 import output_data_3d, all_json_data_3d


def split_data(_str):
    import re
    _str = _str.strip()
    _splied = [i.strip() for i in re.split('\s+', _str)]
    if len(_splied) == 10 and re.match('\d+', _splied[0]) and re.match('\d+', _splied[-1]) and re.match('\d+:\d+:\d+',
                                                                                                        _splied[-2]):
        return [float(i) for i in _splied[:8]]
    return None


output_data_split = output_data.split('\n')

output_data_split_3d = output_data_3d.split('\n')

def get_data2(slice, alltime):
    pd = output_data_split[:int((len(output_data_split) / alltime) * (slice + 1))][-600:]
    pd2 = all_json_data[:int((len(all_json_data) / alltime) * (slice + 1))]
    return pd2, '\n'.join(pd)

def get_data_3d(slice, alltime):
    pd = output_data_split_3d[:int((len(output_data_split_3d) / alltime) * (slice + 1))][-600:]
    pd2 = all_json_data_3d[:int((len(all_json_data_3d) / alltime) * (slice + 1))]
    return pd2, '\n'.join(pd)

if __name__ == '__main__':
    last = 0
    for i in range(10000):
        a, b = get_data2(i, 3600)

        if last != len(a):
            last = len(a)
        else:
            print(i)
            print(last)
