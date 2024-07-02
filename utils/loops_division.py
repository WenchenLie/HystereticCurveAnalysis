import numpy as np
from typing import Literal


def loops_division(
        u: np.ndarray,
        F: np.ndarray,
        d: np.ndarray,
        skip: Literal[0, 1]=0,
        method: Literal['a', 'b']='a'
    ) -> tuple[list[np.ndarray], list[np.ndarray], list[np.ndarray], int]:
    """滞回曲线分圈 (skip=1时跳过最后一圈，防止最后一圈不完整)

    Args:
        u (np.ndarray): 原始数据的位移序列
        F (np.ndarray): 原始数据的力序列
        d (np.ndarray): 原始数据的附属数据(二维)
        skip (Literal[0, 1], optional): 是否跳过跳过最后一圈，为1时跳过
        method (Literal['a', 'b'], optional): 分圈的方法，
        a-以滞回与y轴的交点作为圈的端点，b-以滞回环的反向点作为圈的端点，默认a

    Returns:
        tuple[list[np.ndarray], list[np.ndarray], list[np.ndarray], int]: 各圈的位移序列，力序列，附属数据，数据总长度
    """
    u_loops, F_loops, d_loops = [], [], []

    if method == 'a':
        length = 2  # 数据总长度
        u_seg, F_seg, d_seg = u[: 2].tolist(), F[: 2].tolist(), d[: 2]
        for i in range(2, len(u)):
            if (u[i] == 0 and u[i - 1] < 0):
                u_loops.append(u_seg)
                F_loops.append(F_seg)
                d_loops.append(d_seg)
                length += len(u_seg)
                u_seg, F_seg = [u[i]], [F[i]]
            elif u[i] > 0 and u[i - 1] < 0:
                u_loops.append(u_seg)
                F_loops.append(F_seg)
                d_loops.append(d_seg)
                length += len(u_seg)
                u_seg, F_seg, d_seg = [u[i]], [F[i]], d[i, np.newaxis]
            else:
                u_seg.append(u[i])
                F_seg.append(F[i])
                d_seg = np.append(d_seg, d[i, np.newaxis], axis=0)
        else:
            if skip == 0 and len(u_seg) > 1:
                u_loops.append(u_seg)
                F_loops.append(F_seg)
                d_loops.append(d_seg)
                length += len(u_seg)

    elif method == 'b':
        length = 2  # 数据总长度
        u_seg, F_seg, d_seg = u[: 2].tolist(), F[: 2].tolist(), d[: 2]
        flag = 0
        for i in range(2, len(u) - 1):
            if (u[i] >= u[i - 1] and u[i] >= u[i + 1]) or (u[i] <= u[i - 1] and u[i] <= u[i + 1]) or (i == len(u) - 2):
                # 当前点为反向点
                if flag == 0:
                    flag = 1
                    continue
                else:
                    u_loops.append(u_seg)
                    F_loops.append(F_seg)
                    d_loops.append(d_seg)
                    length += len(u_seg)
                    u_seg, F_seg, d_seg = [u[i]], [F[i]], d[i, np.newaxis]
                    flag = 0
            else:
                # 当前点不是反向点
                u_seg.append(u[i])
                F_seg.append(F[i])
                d_seg = np.append(d_seg, d[i, np.newaxis], axis=0)
        else:
            if skip == 0 and len(u_seg) > 1:
                u_loops.append(u_seg)
                F_loops.append(F_seg)
                d_loops.append(d_seg)
                length += len(u_seg)

    u_loops = [np.array(loop) for loop in u_loops]
    F_loops = [np.array(loop) for loop in F_loops]
    return u_loops, F_loops, d_loops, length
