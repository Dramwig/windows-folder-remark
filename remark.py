# -*- coding: utf-8 -*
# Filename: comment.py

__author__ = 'Piratf'

import sys
import os
from subprocess import run

# 获取系统编码，确保备注不会出现乱码
defEncoding = sys.getfilesystemencoding()


# 将代码中的字符转换为系统编码
def sys_encode(content):
    return content.encode(defEncoding).decode(defEncoding)


def run_command(command):
    #print(f"sys运行:{command}")
    run(command,shell=True)


def get_setting_file_path(fpath):
    return fpath + os.sep + 'desktop.ini'


def update_folder_comment(fpath, comment):
    content = sys_encode(u'[.ShellClassInfo]' + os.linesep + 'InfoTip=')
    # 开始设置备注信息
    setting_file_path = get_setting_file_path(fpath)
    with open(setting_file_path, 'w') as f:
        f.write(content)
        f.write(sys_encode(comment + os.linesep))

    # 添加保护
    run_command('attrib \"' + setting_file_path + '\" +s +h')
    run_command('attrib \"' + fpath + '\" +s ')


def add_comment(fpath=None, comment=None):

    # 输入文件夹路径
    if fpath is None:
        return "输入目标文件夹路径"

    # 去除路径左右两端的引号
    fpath = fpath.strip('\"')
    fpath = fpath.strip('\'')

    # 判断路径是否存在文件夹
    if not os.path.isdir(fpath):
        print("你输入的不是一个正确路径")
        return "你输入的不是一个正确路径"

    setting_file_path = get_setting_file_path(fpath)

    # 判断设置文件是否已经存在
    if os.path.exists(setting_file_path):
        # 去除保护属性
        run_command('attrib \"' + setting_file_path + '\" -s -h')

    if not comment:
        print("备注不要为空哦")
        return "备注不要为空哦"

    update_folder_comment(fpath, comment)

    print("备注添加成功")
    return "备注添加成功"


if __name__ == '__main__':
    if len(sys.argv) == 3:
        add_comment(sys.argv[1], sys.argv[2])
