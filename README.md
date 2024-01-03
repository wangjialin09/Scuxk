# 四川大学选课
Scu选课脚本

该项目改进自：https://github.com/Junbo2002/scu-course-select

全网能找到的最原始版本为：https://github.com/MEHANTA/SCUCourseSelectHelper

感谢以上两位大佬！

## 使用须知
- 本项目只适用于编程学习用途，不得用于实际选课阶段，请在下载后24小时内删除！
- 不得随意传播本项目至任何公开场合（包括但不限于QQ群、微信群、贴吧论坛等）
- 因用户使用或修改项目源码而产生的一切责任与本人无关，本人不负任何连带责任
- 若不同意以上使用条例，请停止clone本项目并不得通过任何途径使用本项目
- 本项目源码以及条例解释权归本人所有

## 如何使用

### 熟悉python的同学

如果使用者熟悉python，可直接下载本项目主目录下的四个文件：`main.py` `fun.py` `config.py` `xkconfig.txt` 。
- 运行环境 `python3.11` ，其他版本不知道运行成啥样

项目支持配置文件直接启动，配置示例见 `xkconfig.txt`

配置好 `xkconfig.txt`后，在该目录下，控制台运行指令 `python main.py`即可运行。当然也可以用 `pycharm` 等编辑器打开运行。

### 不熟悉python的同学

为防止过度滥用，可以联系开发者给你发.exe文件哦

### 使用须知

- 本程序抢课的原理就是不断刷新课余量，一旦有课余量就选择该课程；简而言之，代替了人工'蹲课'的行为。
- 运行程序前请务必确认满足所选课程要求（年级限制、专业限制、课程时间等），否则程序会判断有课余量然后一直发送选课请求，一直选课失败，从而被教务处发现。
- 请谨慎使用本程序，如被教务处请喝茶，与作者无关。

## 常见问题：

- Q：什么是*方案计划号* ？

  A：是教务处区别不同培养方案计划的代号，开发者已整理好 2019级-2023级 所有的培养计划，详情见 [19-23方案计划号](https://kdocs.cn/l/cnVkzaJklCO7) 。找到自己专业对应的方案计划号后填入 `config.txt` 即可。
  

- Q：抢课脚本和教务管理系统可以同时登陆吗？

  A：运行抢课脚本后，本地的教务系统会被踢出去；如果本地再次输入学号密码登录，脚本则会运行异常退出。所以答案是，不可以！



- 更多问题欢迎留言： wjlfish@qq.com



## 支持我们

​	请给本项目点个 **star**

