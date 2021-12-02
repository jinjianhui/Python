print("="*20,"欢迎使用员工管理系统","="*20)
# 创建一个列表
staff_messages = ['孙悟空\t500\t男\t花果山']
# 创建一个死循环
while True:
    # 方法1
    # control = ['1、查询员工','2、添加员工','3、删除员工','4、退出系统']
    # for i in control:
    #     print(i)
    # print("请选择要做的操作：")
    # 方法2
    print("\t1、查询员工")
    print("\t2、添加员工")
    print("\t3、删除员工")
    print("\t4、退出系统")
    user_choose = int(input("请选择（1-4）："))
    # 打印一个分割线
    print("="*62)

    if user_choose == 1 :
        # 查询员工
        # 先打印表头
        print('序号\t姓名\t年龄\t性别\t住址')
        # 创建一个变量来显示员工的序号
        staff_number = 1
        # 显示员工信息
        for staff in staff_messages:
            print(f'{staff_number}\t{staff}')
            staff_number += 1
            
    elif user_choose == 2 :
        # 添加员工
        # 获取添加的信息：姓名、年龄、性别、住址
        name = input('姓名：')
        age = int(input('年龄：'))
        gender = input('性别：')
        addr = input('住址：')
        # 创建员工信息
        staff = f'{name}\t{age}\t{gender}\t{addr}'
        # staff_messages.append(name)
        # staff_messages.append(age)
        # staff_messages.append(gender)
        # staff_messages.append(addr)
        # 提示添加员工信息
        print('以下员工将会被添加到系统中')
        print("="*62)
        print('姓名\t年龄\t性别\t住址')
        print(staff)
        print("="*62)
        judge = input('请确认是否进行该操作：Y/N：')
        if judge == 'Y':
            staff_messages.append(staff)
            print('你已经成功添加该员工至系统中')
        elif judge == 'N':
            print('你取消了该员工信息的添加')
        else:
            print('你输入的操作有误，请重新选择')
            break

    elif user_choose == 3 :
        # 删除员工
        # 删除员工需要通过姓名来删除
        del_number = int(input('请输入你要删除的员工序号：'))
        # 判断删除的员工序号
        if del_number <= len(staff_messages):
            # 输入合法，根据序号来获取索引：
            del_i = del_number - 1
            print('以下员工将会被删除')
            print("="*62)
            print('序号\t姓名\t年龄\t性别\t住址')
            print(f'{del_number}\t{staff_messages[del_i]}')
            print(staff)
            print("="*62)
            judge_confirm = input('该操作不可恢复，请确认是否进行该操作：Y/N：')
            if judge_confirm == 'Y':
                staff_messages.remove(del_i)
                print('你已经成功删除该员工')
            elif judge_confirm == 'N':
                print('你取消了该操作！')
            else:
                print('你输入的操作有误，请重新选择')
                break
        else:
            print('您的输入有误，请重新操作！')
        # del_number = del_user - 1
        # for user_number in staff_messages:
        #     del staff_messages[del_number:del_number+4]
        #     break
        # del_number += 4

    elif user_choose == 4 :
        input('感谢使用！再见！点击回车键退出！')
        break

    else :
        print('您的输入有误，请重新选择！')
    print("="*62)



