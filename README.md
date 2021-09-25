# 代码对拍器

* [代码对拍器](#代码对拍器)
   * [comparator.py 使用说明](#comparatorpy-使用说明)
   * [comparator.sh 使用说明（已废弃）](#comparatorsh-使用说明已废弃)
   * [版本更新](#版本更新)


## comparator.py 使用说明 

> GUI 版本，后续会不停更新~~（应该）~~



GUI 版本下，不同系统没有对应的使用要求

在根目录下打开终端，输入指令

```
python3 comparator.py
```

- 按 `tap` 可以直接在终端显示选择目录下的文件



## comparator.sh 使用说明（已废弃）

> 非 GUI 版本，目前已经停止对此版本的所有更新



首先把两份代码的 `.cpp`文件以及能随机生成输入的 `.cpp`文件放在根目录下

根据系统类型选择对应的操作

- Windows

  在根目录下打开 `Git Bash` ，输入指令
- Linux & macOS

  直接在终端里运行指令

指令如下

```shell
bash comparator.sh input.cpp prog1.cpp prog2.cpp GROUP_NUMBER
```

> `input.cpp` 替换为能随机生成输入的文件名
>
> `prog1.cpp` 替换为第一份代码的文件名
>
> `prog2.cpp` 替换为第二份代码的文件名
>
> `GROUP_NUMBER` 替换为需要对拍的组数，此项是可选的，不输入则会一直对拍直到用户输入 `Ctrl + C` 停止



## 版本更新

|  更新时间  |             更新说明              |
| :--------: | :-------------------------------: |
| 2021.09.24 | 完成 `comparator.sh` 基本对拍功能 |
| 2021.09.24 |      增加设置对拍组数的功能       |
| 2021.09.25 |  完成 `comparator.py` 的基本功能  |
| 2021.09.25 | 取消 GUI 版本中设置对拍组数的功能 |



## 后续开发

- 目前只能支持 `C/C++` 的编译，后续开发支持更多语言
- 美化界面

