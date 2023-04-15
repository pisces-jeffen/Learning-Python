"""
这是学习信息管理系统的工具程序
"""

student_info = []  # 用来保存学员信息
# 测试数据
# student_info = [{'id': '1', 'name': '张三', 'sex': '男', 'hobby': 'rap'},
#                 {'id': '2', 'name': '李四', 'sex': '女', 'hobby': '篮球'},
#                 {'id': '3', 'name': '张三', 'sex': '女', 'hobby': '跑步'}]

header = ["id", "姓名", "性别", "爱好"]


def show_menu():
    """
    显示系统菜单
    :return:
    """
    print("欢迎使用【学员信息管理系统】V1.0".center(24, "="))
    print("1. 新增学员信息")
    print("2. 删除学员信息")
    print("3. 修改学员信息")
    print("4. 查询学员信息")
    print("5. 显示全部学员信息")
    print("6. 退出系统")
    print("=" * 24)


def add_student():
    """
    新增学员信息
    :return:
    """
    # 1. 提示用户添加学员信息
    print("新增学员信息".center(24, "="))
    id = input("请输入学员id：")
    # 判断id是否重复，id不能重复
    for students in student_info:
        if students['id'] == id:
            print("【该id已存在，请重新输入！】")
            add_student()
            return
    name = input("请输入学员姓名：")
    sex = input("请输入学员性别：")
    hobby = input("请输入学员爱好：")
    # 2. 将输入的信息，保存为一个字典
    students = {
        "id": id,
        "name": name,
        "sex": sex,
        "hobby": hobby
    }
    # 3. 将学员信息的字典追加到列表中
    student_info.append(students)
    # 4. 提示用户添加成功
    print(f"【添加序号{id}，姓名: {name} 成功！】")
    info = input("是否继续添加？(1.继续 2.返回上一级)")
    if info == "1":
        add_student()
    else:
        return


def del_student():
    """
    删除学员信息
    :return:
    """
    print("删除学员信息".center(24, "="))
    # 1. 提示用户输入要删除的学员id
    del_id = input("请输入要删除的学员id：")
    # 2. 遍历学员信息列表，找到要删除的学员信息
    for students in student_info:
        if students['id'] == del_id:
            # 3. 删除学员信息
            student_info.remove(students)
            # 4. 提示用户删除成功
            print(f"【删除序号{del_id}成功！】")
            info = input("是否继续删除？(1.继续 2.返回上一级)")
            if info == "1":
                del_student()
            else:
                return
    else:
        print("【该id不存在，请重新输入！】")
        del_student()


def modify_student():
    """
    修改学员信息
    可全部修改，也可单独修改
    :return:
    """
    # 执行修改操作
    students = input("请输入要修改的学员id：")
    for find_students in student_info:
        if find_students['id'] == students:
            find_students["id"] = input_students_info(
                find_students["id"], "id[回车键不修改]：")
            find_students["name"] = input_students_info(
                find_students["name"], "姓名[回车键不修改]：")
            find_students['sex'] = input_students_info(
                find_students["sex"], "性别[回车键不修改]：")
            find_students['hobby'] = input_students_info(
                find_students["hobby"], "爱好[回车键不修改]：")
    print("【修改学员信息成功！】")


def input_students_info(value, tip_message):
    """
    输入学员信息
    :param value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 如果用户输入了内容，就返回内容，否则返回字典中原有的值
    """
    # 1. 提示用户输入内容
    result_str = input(tip_message)
    # 2. 针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3. 如果用户没有输入内容，返回字典中原有的值
    else:
        return value


def search_student():
    """
    查询学员信息
    根据姓名查找(如果有两个张三，则全部显示，如果只有一个，则显示一个)
    :return:
    """
    print(f"{'搜索学员信息':=^24}")
    nameList = []
    # 1. 提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")
    for students in student_info:
        if students['name'] == find_name:
            # 打印表头
            for title in header:
                print(title, end="\t\t")
            print()
            print('-' * 28)
            # 打印学员的详细信息
            for value in students.values():
                print(f"{value}", end="\t\t")
            print()
            # 提示用户对于找到的信息，进行操作选择
            # deal_students(students)
            # break
            nameList.append(students)
    else:
        if len(nameList) == 0:
            print("【该学员不存在，请重新输入！】")
            search_student()
        else:
            deal_students(nameList)


def show_all_student():
    """
    显示全部学员信息
    :return:
    """
    print("显示全部信息".center(46, "="))
    # 判断学员信息列表是否为空
    if len(student_info) == 0:
        print("【当前没有任何的学员信息记录，请使用新增功能添加学员信息！】")
        return
    # 打印表头
    for title in header:
        print(title, end="\t\t")
    print()
    print('-' * 52)
    # 逐一打印列表中的每个学员信息
    for students in student_info:
        for value in students.values():
            print(f"{value}", end="\t\t")
        print()


def deal_students(find_students):
    """
    处理查找到的学员信息
    :param find_students: 查找到的学员信息
    :return:
    """
    action = input("请选择要执行的操作：[1] 修改 [2] 删除 [0] 返回上级菜单")
    if action == "1":
        # 执行修改操作
        find_students["id"] = input_students_info(
            find_students["id"], "id[回车键不修改]：")
        find_students["name"] = input_students_info(
            find_students["name"], "姓名[回车键不修改]：")
        find_students["sex"] = input_students_info(
            find_students["sex"], "性别[回车键不修改]：")
        find_students["hobby"] = input_students_info(
            find_students["hobby"], "爱好[回车键不修改]：")
        print("【修改学员信息成功！】")
    elif action == "2":
        # 执行删除操作
        student_info.remove(find_students)
        print("【删除学员信息成功！】")
    elif action == "0" or action == "":
        return
    else:
        print("【您输入的不正确，请重新选择】")
        deal_students(find_students)


if __name__ == '__main__':
    # show_menu()
    # add_student()
    # del_student()
    modify_student()
    # search_student()
    show_all_student()
