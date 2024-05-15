import numpy as np


def get_turning_point(u: np.ndarray, window1: int, window2: int) -> tuple[int, list[int]]:
    """识别反向点

    Args:
        u (np.ndarray): 位移序列
        window1 (int): 起始滑块宽度
        window2 (int): 终止滑块宽度

    Returns:
        tuple[int, list[int]]: 反向点的数量，反向点的索引号
    """
    half1 = int(window1 / 2)  # 滑块最小半宽度
    half2 = int(window2 / 2)  # 滑块最大半宽度
    tag = [0]  # 反向点的索引
    sleep = window1
    for i in range(len(u) - 1):
        window = window1 + int(i / (len(u) - half2 - 2) * (window2 - window1))  # 自适应滑动窗口宽度(线性变化)
        half = int(window / 2)
        if sleep > 0:
            sleep = max(0, sleep - 1)
            continue  # 跳过判断，防止出现连续多个卸载点
        idx1 = max(0, i - half)
        idx2 = i + half
        try:
            if u[i] >= max(max(u[idx1: i]), max(u[i + 1: idx2 + 1])):
                # 当前值为窗口区域的最大值时(当前值永远处于滑块中心)
                tag.append(i)
                sleep = window
            elif u[i] <= min(min(u[idx1: i]), min(u[i + 1: idx2 + 1])):
                # 该值为窗口区域的最小值时
                tag.append(i)
                sleep = window
        except:
                print('error 1')
    tag.append(len(u) - 1)
    n = int((len(tag) - 2) / 2)
    return n, tag