import numpy as np


def get_residual_deformation(u_loop: np.ndarray, F_loop: np.ndarray) -> tuple[float, float]:
    """计算滞回环的残余变形

    Args:
        u_loop (np.ndarray): 滞回环的位移序列
        F_loop (np.ndarray): 滞回环的力序列

    Returns:
        tuple[float, float]: 正向、负向的残余变形
    """

    d_pos, d_neg = 0, 0
    for i in range(1, len(u_loop) - 1):
        if F_loop[i] == 0 and u_loop[i] > 0:
            d_pos = u_loop[i]
            continue
        elif F_loop[i] == 0 and u_loop[i] < 0:
            d_neg = u_loop[i]
            continue
        elif F_loop[i] > 0 and F_loop[i + 1] < 0:
            k = (F_loop[i + 1] - F_loop[i]) / (u_loop[i + 1] - u_loop[i])
            d_pos = u_loop[i] - F_loop[i] / k
            continue
        elif F_loop[i] < 0 and F_loop[i + 1] > 0:
            k = (F_loop[i + 1] - F_loop[i]) / (u_loop[i + 1] - u_loop[i])
            d_neg = u_loop[i] - F_loop[i] / k
            continue
    return d_pos, d_neg