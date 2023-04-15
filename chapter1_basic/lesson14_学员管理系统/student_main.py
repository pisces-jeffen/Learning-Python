"""
学员管理系统
系统简介
需求：进⼊系统显示系统功能界⾯，功能如下：
添加学员
删除学员
修改学员信息
    完善修改学员信息: 可全部修改，也可单独修改
查询学员信息
    完善查找学员信息: 根据姓名查找(如果有两个张三，则全部显示，如果只有一个，则显示一个)
显示所有学员信息
退出系统
"""
"""
这是宠物信息管理系统的主程序
"""

# 导入学员管理系统的功能模块
from student_tools import *


def main():
    # 1. 显示系统功能界面
    while True:
        show_menu()
        # 2. 获取用户的选择
        action_str = input("请选择希望执行的操作：")
        print(f"您选择的操作是【{action_str}】")
        # 3. 根据用户的数据执行相应的功能
        if action_str in ["1", "2", "3", "4", "5", "6"]:
            # 添加学员
            if action_str == "1":
                add_student()
            # 删除学员
            elif action_str == "2":
                del_student()
            # 修改学员信息
            elif action_str == "3":
                modify_student()
            # 查询学员信息
            elif action_str == "4":
                search_student()
            # 显示所有学员信息
            elif action_str == "5":
                show_all_student()
            # 退出系统
            elif action_str == "6":
                print("欢迎再次使用【学习信息管理系统】")
                break
        else:
            print("您输入的不正确，请重新选择")


if __name__ == '__main__':
    main()
