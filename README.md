# 代码对拍器

* [代码对拍器](#代码对拍器)
   * [comparator.py 使用说明](#comparatorpy-使用说明)
   * [随机数的生成](#随机数的生成)
   * [后续开发](#后续开发)
   * [comparator.sh 使用说明（已废弃）](#comparatorsh-使用说明已废弃)


## comparator.py 使用说明 

> GUI 版本，后续会不停更新~~（应该）~~

GUI 版本下，不同系统没有对应的使用要求

在根目录下打开终端，输入指令

```
python3 comparator.py
```

- 按 `TAB` 可以直接在终端显示选择目录下的文件



## 随机数的生成

随机数的生成推荐使用如下代码

```c++
#include <chrono>

auto getRandom(int n) {
    // For Windows
    auto random = std::chrono::duration_cast<std::chrono::milliseconds>(
                      std::chrono::system_clock::now().time_since_epoch())
                      .count();

    // For all systems except Windows
    // auto random = std::chrono::duration_cast<std::chrono::nanoseconds>(
    //                   std::chrono::system_clock::now().time_since_epoch())
    //                   .count();

    return random % n;
}
```



Windows 系统下不建议使用 `nanoseconds` 生成随机数，因为它前面的数字和 `milliseconds` 是相等的，但在后面增加了三个 0。

```
// In Windows
auto randomMilli = duration_cast<milliseconds>(system_clock::now().time_since_epoch()).count();
cout << randomMilli << endl; // result: 1632628461956

auto randomNano = duration_cast<nanoseconds>(system_clock::now().time_since_epoch()).count();
cout << randomNano << endl; // result: 1632628461956000
```




## 后续开发

- [x] 开发 GUI 版本
- [ ] 目前只能支持 `C/C++` 的编译，后续开发支持更多语言
- [ ] 美化界面



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
