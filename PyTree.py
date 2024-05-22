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

        temp[-1] = 0

        return temp
    except IndexError:
        print("This data doesn't exits")
        return [-1]


def remove(head: list, data: int):  # 删除
    if head[0] == data:
        if len(head) >= 2:
            try:
                temp = head[2]
                head[0] = head[1][0]
                head[2] = temp
                head[1] = head[1][1]

            except IndexError:
                head[0] = head[1][0]
                head.remove(head[1])
            return

        else:
            del head[0]
            return

    if data % head[1][0] == 0:
        remove(head[1], data)

        if len(head[1]) == 0:
            head.remove(head[1])
        elif len(head[1]) == 0:
            head.remove(head[2])

        return

    elif data % head[2][0] == 0:
        remove(head[2], data)

        if len(head[1]) == 0:
            head.remove(head[1])
        elif len(head[2]) == 0:
            head.remove(head[2])

        return


#  关于树高度的计算,由于是常用操作,故不归入Extension中
def HeightCalculate(tree: list, p: int = 0) -> int:
    try:  # 检测当前表是否读完
        point = 0  # 默认高度
        # 比较子树预估高度大小,因为len()无法精确的计算出一个树表的高度,正常来说,高度比较大的那边便是书的最终高度
        biggest = max(len(tree[1]), len(tree[2]))
        if biggest == len(tree[1]):  # 当最高的一方是左边时
            point += HeightCalculate(tree[1], point + 1)  # 每进到一层高度就加1,当递归操作结束时,让当前树的默认高度加上字数的高度
            return point

        else:  # 当最高的一方为右边时
            point += HeightCalculate(tree[2], point + 1)  # 每进到一层高度就加1,当递归操作结束时,让当前树的默认高度加上字数的高度
            return point  # 返回最终值

    # 当当前表遍历完时
    except IndexError:
        return p + len(tree)  # 返回最终子树的高度
