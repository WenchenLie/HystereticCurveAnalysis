import numpy as np


def get_residual_deformation(u_loop: np.ndarray, F_loop: np.ndarray) -> tuple[float, float]:
    """计算滞回环的残余变形

    Args:
        u_loop (np.ndarray): 滞回环的位移序列
        F_loop (np.ndarray): 滞回环的力序列

    Returns:
        tuple[float, float]: 正向、负向的残余变形
    """

    d_pos, d_neg = None, None
    for i in range(1, len(u_loop) - 1):
        if d_pos is not None and d_neg is not None:
            break
        ui, uj = u_loop[i], u_loop[i + 1]
        Fi, Fj = F_loop[i], F_loop[i + 1]
        if ui >= 0 and d_pos is None:
            if Fi == 0:
                d_pos = ui
            elif Fi > 0 and Fj < 0:
                d_pos = ui + (uj - ui) * (0 - Fi) / (Fj - Fi)
        elif ui < 0 and d_neg is None:
            if Fi == 0:
                d_neg = ui
            elif Fi < 0 and Fj > 0:
                d_neg = ui + (uj - ui) * (0 - Fi) / (Fj - Fi)
    d_pos = 0 if d_pos is None else d_pos
    d_neg = 0 if d_neg is None else d_neg
    return d_pos, d_neg
