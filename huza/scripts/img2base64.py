def image2base64(image_path, output_path):
    """

    :param image_path: 图片路径
    :type image_path: str
    :return:
    :rtype:
    """
    import os, base64, json
    _all_data = {}
    for root, dirs, files in os.walk(image_path):
        for f in files:
            _file = os.path.join(root, f)
            _, filename = os.path.split(_file)
            filename_nofix, _ = os.path.splitext(filename)
            _, pofix = os.path.splitext(_file)
            if pofix.lower() in ('.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp'):
                with open(_file, "rb") as f:
                    base64_data = str(base64.b64encode(f.read()), encoding='utf-8')
                print(f'\033[92m{_file} success \033[0m')
                _all_data[filename_nofix] = (base64_data, pofix.upper().strip('.'))
    dt_s = json.dumps(_all_data)
    with open(os.path.join(output_path, 'img.py'), 'w') as f:
        f.write(f'image_dict={dt_s}')


if __name__ == '__main__':
    image2base64(r'C:\Users\hufei\Desktop\db')
