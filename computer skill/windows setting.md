# 如何在右键菜单中添加应用
例如将便携版的vscode加到右键菜单

1. 打开注册表编辑器regedit
2. 计算机\HKEY_CLASSES_ROOT\Directory\Background\shell
3. 新建项（实际上是个文件夹）
4. 点击文件夹，右侧有一`(默认)`的值，其值即是 右键菜单中显示的名字
5. 在该界面，新建一个`字符串值`，命名为`Icon`，即是右键菜单中显示的icon，值为vscode的`code.exe`的路径，或者某一个icon的路径
6. 在该项（文件夹）下新建项，命名为`command`
7. `command`中也有一个`(默认)`，将其值改为所需执行的命令`"C:\Program Files\VSCode\Code.exe" "."`

大功告成