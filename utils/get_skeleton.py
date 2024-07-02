import numpy as np
from typing import Literal


def get_skeleton(u: np.ndarray, F: np.ndarray, skeleton_method: Literal[1, 2, 3]) -> np.ndarray:
    """获取所有骨架点

    Args:
        u (np.ndarray): 位移序列
        F (np.ndarray): 力序列
        skeleton_method (Literal[1, 2]): 骨架点的确定方法，
        1-通过最大位移对应的力确定，2-通过最大力确定，3-通过最远点确定

    Returns:
        np.ndarray: 骨架点所对应的索引号
    """
    tag_gujia = []
    i0 = 0
    for i in range(1, len(u) - 1):
        if (u[i+1] - u[i]) * (u[i] - u[i-1]) < 0:
            # 位移反向点
            if skeleton_method == 1:
                tag_gujia.append(i)
            elif skeleton_method == 2:
                if u[i] > u[i-1]:
                    # 正向
                    tag_gujia.append(i0 + np.argmax(F[i0: i]))
                else:
                    # 反向
                    tag_gujia.append(i0 + np.argmin(F[i0: i]))
            elif skeleton_method == 3:
                direction = 'p' if u[i] > u[i-1] else 'n'
                tag_gujia.append(i0 + get_farthest_point_idx(u[i0: i], F[i0: i], direction))
            else:
                raise ValueError('Error 4')
            i0 = i
    return np.array(tag_gujia)


def get_farthest_point_idx(x: np.ndarray, y: np.ndarray, direction: Literal['p', 'n']) -> int:
    """获得滞回曲线半循环曲线最远点对应的索引，最远点定义为：将位移和力数据归一化后求平方和(l=x^2+y^2)，返回序列l最大或最小的点的索引

    Args:
        x (np.ndarray): 位移序列
        y (np.ndarray): 力序列
        direction (Literal['p', 'n']): 位移方向，p-正向，n-负向

    Returns:
        int: 最远点索引号
    """
    if direction == 'p':
        x_norm = x / max(x)
        y_norm = y / max(y)
    elif direction == 'n':
        x_norm = x / min(x)
        y_norm = y / min(y)
    x_norm[x_norm<0] = 0
    y_norm[y_norm<0] = 0
    l = x_norm ** 2 + y_norm ** 2
    return np.argmax(l)
