def initTree(tree: list, data: int = 1):  # 初始化,可以不用...
    tree.append(data)


def push(head: list, data: int):  # 推入数据
    if len(head) < 3:
        head.append([data])
        return

    if data % head[1][0] == 0:
        push(head[1], data)
        return

    elif data % head[2][0] == 0:
        push(head[2], data)
        return


def print_tree(head, indent=0):  # 以树状图输出结构
    if isinstance(head, list):
        print(' ' * indent + str(head[0]))
        for child in head[1:]:
            print_tree(child, indent + 4)


def search(head: list, data: int, temp: list = None) -> list:  # 搜索
    try:
        if temp is None:
            temp = []

        if head[0] == data:
            return temp

        if data % head[1][0] == 0:
            temp = [1]
            temp += search(head[1], data, temp)

        elif data % head[2][0] == 0:
            temp = [2]
            temp += search(head[2], data, temp)

        return temp
    except IndexError:
        print("This data doesn't exits")
        return [-1]


def remove(head: list, data: int):  # 删除
    if head[1][0] == data:
        head.remove(head[1])
        return

    if data % head[1][0] == 0:
        remove(head[1], data)

    elif data % head[2][0] == 0:
        remove(head[2], data)

    else:
        print("-1")
        return
