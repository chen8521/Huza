import os

try:
    import readline
except ImportError as e:
    pass
from huza.scripts.img2base64 import image2base64


def main():
    """命令行入口
    """
    base = os.path.abspath(os.path.dirname(__file__))
    import argparse
    parser = argparse.ArgumentParser()
    parser.description = 'Huza 命令行工具'
    parser.add_argument("-genimg", help="生成图片集文件", action='store_true')
    parser.add_argument('-i', "--input", help="输入目录", default='.')
    parser.add_argument('-o', "--output", help="输出目录", default='.')

    args = parser.parse_args()
    if args.genimg:
        image2base64(args.input, args.output)
    else:
        parser.print_help()
