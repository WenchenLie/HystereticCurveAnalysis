import numpy as np
from typing import Literal


def get_skeleton(u: np.ndarray, F: np.ndarray, skeleton_method: Literal[1, 2]) -> np.ndarray:
    """获取所有骨架点

    Args:
        u (np.ndarray): 位移序列
        F (np.ndarray): 力序列
        skeleton_method (Literal[1, 2]): 骨架点的确定方法，
        1-通过最大位移对应的力确定骨架点，2-通过最大力确定骨架点

    Returns:
        np.ndarray: 骨架点所对应的索引号
    """
    tag_gujia = []
    i0 = 0
    for i in range(1, len(u) - 1):
        if (u[i+1] - u[i]) * (u[i] - u[i-1]) < 0:
            if skeleton_method == 1:
                tag_gujia.append(i)
            elif skeleton_method == 2:
                if u[i] > u[i-1]:
                    # 正向
                    tag_gujia.append(i0 + np.argmax(F[i0: i]))
                else:
                    # 反向
                    tag_gujia.append(i0 + np.argmin(F[i0: i]))
            else:
                raise ValueError('Error 4')
            i0 = i
    return np.array(tag_gujia)