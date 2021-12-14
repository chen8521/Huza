# coding=utf-8
import re
from collections import namedtuple

LOGFILE = 'frog.log'

FLOAT_RE = re.compile('^[+-]?\d+$|^[-+]?\d*\.\d+$|^[+-]?\d+\.\d+[Ee]{1}[+-]?\d+$')

# SIGNAL
SINGNAL_SETDIR = 'setdir'  # 设置显示目录的信号
SINGNAL_VIEWTEXT = 'viewtext'  # 显示文本

SINGNAL_SHOW_MODEL_LIST = 'show_model_list'  # 点击模型子节点的回调
SINGNAL_SHOW_MODEL_MORE = 'show_model_more'  # 点击模型子节点的回调
SINGNAL_DEMO = 'demo'  # 显示demo
SINGNAL_CHANGE_SETTING = 'change_setting'  # 显示demo
SINGNAL_CHANGE_MESH = 'change_mesh'  # 切换网格显示
SINGNAL_IMPORT_MESH = 'import_mesh'
SINGNAL_SHOW_FILE_LIST = 'show_file_list'  # 显示demo
SINGNAL_RUN = 'run'  # 计算
SINGNAL_RUN3D = 'run3d'
SINGNAL_STOP = 'stop_run'
SINGNAL_SHOW_TEXT = 'ShowText'
SINGNAL_FLOW_VIEW = 'FlowView'

FLAG_MESH = 'mesh'  # 左侧导航主节点-模型
FLAG_MESH_LIST = 'mesh_list'  # 模型子节点

FLAG_SETTING = 'setting'  # 左侧导航主节点-几何

FLAG_GRID = 'grid'  # 左侧导航主节点-网格
FLAG_GRID_LIST = 'grid_list'
FLAG_GRID_MORE = 'grid_more'

FLAG_TLMX = 'tlmx'
FLAG_DXLMX = 'dxlmx'
FLAG_JZTXSZ = 'jztxsz'
FLAG_JZZX = 'jzzx'
FLAG_BJTJSZ = 'bjtjsz'
FLAG_ZYMWZ = 'zymwz'
FLAG_DWGSZ = 'dwgsz'
FLAG_JSCSSZ = 'jscssz'
FLAG_IMPORTMESH = 'importmesh'

FLAG_RUN = 'run'
FLAG_RUN_LIST = 'run_list'

FLAG_RESULT = 'result'
FLAG_RESULT_FILE_LIST = 'result_file_list'  # 模型子节点
FLAG_RESULT_FLOW_LIST = 'result_flow_list'  # 模型子节点
