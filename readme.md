# Windows 下给文件夹添加注释

forked from [piratf/windows-folder-remark](https://github.com/piratf/windows-folder-remark)

## 如何使用

本工具提供 exe 版本和 python 源码版本，exe 版本为 dist/remark.exe，可以直接双击运行，源码版本支持的版本为 Python 3.x

以下通过展示 exe 版本的使用方法，python 源码版本用法相同。

有两种典型的使用方式：

```txt
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