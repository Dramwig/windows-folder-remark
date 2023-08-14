# Windows 下给文件夹添加注释

## 如何使用

本工具提供 exe 版本和 python 源码版本，exe 版本为 dist/Remark.exe，可以直接双击运行，源码版本支持的版本为 Python 3.x。

remark.py修改于[piratf](https://github.com/piratf/windows-folder-remark)提供的py程序，仅保留了 `./remark.exe [路径] [备注内容]` 方法。

ui.py为图形化界面的入口程序。

### V1.2

提供了一个简陋的图形化界面，支持拖拽文件夹输入，文本框能正常打字。

使用方式：

- `./remark.exe [路径] [备注内容]` 需自行编译remark.py。
- dist/Remark.exe 点击即用，根据提示操作即可。

### v1.1

以下通过展示 exe 版本的使用方法，python 源码版本用法相同。

有两种典型的使用方式：

```bat
# 1. 直接运行程序的方式
# 运行后根据提示操作即可
# 这种方式适合手动给一些文件夹进行备注
./remark.exe

# 2. 带参数运行程序的方式
# 运行后会立即为输入的文件夹加上备注
# 适合被其他程序或脚本批量调用使用
./remark.exe [路径] [备注内容]
```

## 注意

该脚本会修改文件夹下隐藏的 Desktop.ini 文件，并为文件夹修饰系统属性

## 致谢

基于或依赖于以下项目

- [piratf/windows-folder-remark](https://github.com/piratf/windows-folder-remark)