# 此为树表的扩展内容(平衡DLC)
# 由于所定插入规则不同,平衡旋转方式也有所不同,故此扩展仅作参考
from PyTree import *


def B_push(head: list, data: int):  # 推入数据
    BalanceJudge(head)
    if len(head) < 3:
        head.append([data])
        BalanceJudge(head)
        return

    if data % head[1][0] == 0:
        B_push(head[1], data)
        BalanceJudge(head)
        return

    elif data % head[2][0] == 0:
        B_push(head[2], data)
        BalanceJudge(head)
        return


def Rotate(tree: list, LOR: int):  # 旋转
    RootTemp = [tree[0]]  # 记录第一个根节点
    if LOR < 0:  # 如果右边高了
        tree[0] = tree[2][0]  # 令右子树的第一个节点成为根节点
        # 如果需要旋转的树存在字节点
        try:
            RootTemp.append(tree[2])
            RootTemp[1].append(tree[2][2])  # 将子树的节点去作为其中一个子节点
            del tree[2][2]  # 删除掉多余的部分
        # 如果没有字节点
        except IndexError:
            pass

        # 更新右子树
        tree[2] = RootTemp

    else:  # 如果左边高了, 操作逻辑和上方一致
        tree[0] = tree[1][0]
        RootTemp.append(tree[2])
        try:
            tree[1][1].append(tree[1][2])
            del tree[1][2]

        except IndexError:
            pass
        tree[1] = tree[1][1]
        tree[2] = RootTemp


# 平衡判断
def BalanceJudge(tree: list):
    # 防止IndexError
    try:
        # 计算左右子树的高度差(平衡因子)
        BalancePoint = HeightCalculate(tree[1]) - HeightCalculate(tree[2])
        # 若出现不平衡现象
        if BalancePoint < -1 or BalancePoint > 1:
            Rotate(tree, BalancePoint)  # 将平衡因子传入旋转函数,由旋转函数自行判断不平衡位置然后旋转

        # 递归判断旋转后的树的平衡性
        BalanceJudge(tree[1])
        BalanceJudge(tree[2])

    # 递归结束
    except IndexError:
        return


a = [1]
b = [1]

for i in range(2, 21):
    push(b, i)

for i in range(2, 21):
    B_push(a, i)

print(f"普通树表:{b}")
print(f"平衡树表:{a}")
