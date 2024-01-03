# -*- coding: UTF-8 -*-
import datetime as date
import hashlib
import os
import time
import colorama

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
colorama.init(autoreset=True)
select_captcha_url = "http://202.115.47.141/student/courseSelect/selectCourse/getYzmPic"
select_result_url = "http://202.115.47.141/student/courseSelect/selectResult/query"
redis_key_url = 'http://202.115.47.141/student/courseSelect/selectCourses/waitingfor'
login_token_url = 'http://202.115.47.141/login'  # 登录页面新加的token
captcha_url = "http://202.115.47.141//img/captcha.jpg"  # 验证码地址
index_url = "http://202.115.47.141//"  # 主页地址
login_url = "http://202.115.47.141//j_spring_security_check"  # 登录接口
course_select_url = "http://202.115.47.141//student/courseSelect/courseSelect/index"  # tokenValue界面
select_url = "http://202.115.47.141//student/courseSelect/selectCourse/checkInputCodeAndSubmit"  # 选课接口
courseList_url = "http://202.115.47.141//student/courseSelect/freeCourse/courseList"  # 选课剩余查询地址
already_select_course_url = "http://202.115.47.141//student/courseSelect/thisSemesterCurriculum/callback"  # 已选课程查询地址
queryTeacherJL_url = "http://202.115.47.141//student/courseSelect/queryTeacherJL"
selectcourse_xueqi = "2022-2023-1-1" # 学期
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3782.0 Safari/537.36 Edg/76.0.152.0'
}
print(f"{bcolors.HEADER}SCU 抢课脚本: 使用该软件造成的后果与作者无关{bcolors.ENDC}")
time.sleep(1)
print(f"{bcolors.HEADER}当前适配 2024.1.2 版本川大抢课系统{bcolors.ENDC}")
time.sleep(1)
print(f"{bcolors.HEADER}原作者：Junbo2002 当前版本作者：初音过去{bcolors.ENDC}")
time.sleep(1)
print(f"{bcolors.HEADER}有不会用的地方可以找作者！！！\n{bcolors.ENDC}")
time.sleep(1)
if os.path.exists("xkconfig.txt"):
    with open("xkconfig.txt", "r", encoding='utf-8') as f:
        info = f.readlines()
    print(f"{bcolors.OKCYAN}检测到本地配置文件，将使用{bcolors.ENDC}" + info[0].strip('\n') + f"{bcolors.OKCYAN}进行选课\n{bcolors.ENDC}")
    time.sleep(1)
    print("开始登录 ^_^\n")
    j_username = info[0].strip('\n')
    o_password = info[1].strip('\n')
    j_password = hashlib.md5(o_password.encode()).hexdigest()
    fajhh = info[2].strip('\n')
    courseNames = info[3].strip('\n').split(';')
    # 课程号1
    courseNums = info[4].strip('\n').split(';')
    # 课序号
    coursekxhNums = info[5].strip('\n').split(';')
else:
    manchoice = input(f'{bcolors.OKCYAN}\n未检测到本地配置文件，如果你只是想临时使用，请输入 1；如果你想生成一个配置文件以便后续重复使用，请输入 2：{bcolors.ENDC}')
    j_username = input(f'{bcolors.OKGREEN}\n请输入学号：{bcolors.ENDC}')
    o_password = input(f'{bcolors.OKGREEN}\n请输入教务系统密码：{bcolors.ENDC}')
    j_password = hashlib.md5(o_password.encode()).hexdigest()
    fajhh = input(f'{bcolors.OKGREEN}\n请输入培养计划代码：{bcolors.ENDC}')
    # 获取用户输入的课程名称、课程号和课序号
    courseNames_input = input(f'{bcolors.OKGREEN}\n请输入课程名称（如果有多个课程，请用分号分隔名称）：{bcolors.ENDC}')
    courseNums_input = input(f'{bcolors.OKGREEN}\n请输入课程号（如果有多个课程，请用分号分隔课程号）：{bcolors.ENDC}')
    coursekxhNums_input = input(f'{bcolors.OKGREEN}\n请输入课序号（如果有多个课程，请用分号分隔课序号）：{bcolors.ENDC}')

    # 将用户输入的字符串分割成列表
    courseNames = courseNames_input.split(';')
    courseNums = courseNums_input.split(';')
    coursekxhNums = coursekxhNums_input.split(';')

    if manchoice == '1':
        configcontent = [j_username, o_password, fajhh, courseNames_input, courseNums_input, coursekxhNums_input]
    else:
        configcontent = [j_username, o_password, fajhh, courseNames_input, courseNums_input, coursekxhNums_input]

        # 指定要保存的文件名及路径（如果不在当前工作目录）
        file_path = "xkconfig.txt"

        # 打开或创建文件进行写入操作
        with open(file_path, 'w', encoding='utf-8') as file:
            # 遍历内容列表，逐行写入文件
            for line in configcontent:
                file.write(line + "\n")
        print(f"{bcolors.OKCYAN}\n配置文件已保存至程序同文件夹下的 xkconfig.txt 文件中！））\n{bcolors.ENDC}")
        time.sleep(1)
        print("开始登录 ^_^\n")




def secondAppend(time_str, s):
    cnt = time_str.count(':')
    if cnt == 1:  # %H:%M
        time_str += ":"+str(s)  # %H:%M:%S
    if cnt > 2:
        raise "时间格式为: %H:%M 或者 %H:%M:%S"
    return time_str


def check():
    if not (len(j_username) == 13 and j_username.isdigit()):
        raise RuntimeError("学号格式错误（学号为13位数字），你是不是输错啦")
    if not fajhh.isdigit():
        raise RuntimeError("方案计划号错误：为纯数字，不知道的话请来问我")


# 检查格式
# 起止时间
try:
    rawnum = "9:30 21:59" # 九点半到晚十点
    selectTime = rawnum.strip('\n').split(' ')
    # print(selectTime)
    selectTime[0] = secondAppend(selectTime[0], 0)
    selectTime[1] = secondAppend(selectTime[1], 59)
    # print(selectTime)

except Exception:
    print("请检查config.txt中是否在第六行以“9:30 21:59”添加了起止时间，中间以空格分隔")

try:
    check()
except RuntimeError as e:
    print("出错啦！错误内容：" + str(e))

