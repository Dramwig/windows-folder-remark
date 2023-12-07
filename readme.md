# windows-folder-remark
Windows 下给文件夹添加注释

## 基本介绍

本工具提供 exe 版本和 python 源码版本，exe 版本为 dist/Remark.exe，可以直接双击运行，源码版本支持的版本为 Python 3.x。

remark.py修改于[piratf](https://github.com/piratf/windows-folder-remark)提供的py程序，仅保留了 `./remark.exe [路径] [备注内容]` 方法。

ui.py为图形化界面的入口程序，提供了一个简陋的图形化界面，支持拖拽文件夹输入，文本框能正常打字。

## 使用方式

- 使用Python命令行运行"[remark.py](http://remark.py/)"脚本，并传递了两个参数，一个是文件路径"path"，另一个是消息"msg"。

  如：`python -u "remark.py" D:\path msg` 

- 执行名为"Remark.exe"的可执行文件。通过双击该可执行文件，你可以直接运行它，并按照程序给出的提示进行操作。

## 注意

该脚本会修改文件夹下隐藏的 Desktop.ini 文件，并为文件夹修饰系统属性

## 致谢

基于或依赖于以下项目:

- [piratf/windows-folder-remark](https://github.com/piratf/windows-folder-remark)
