import numpy as np
from typing import Literal


def get_dissipated_energy(u_loops: list[np.ndarray], F_loops: list[np.ndarray], EnergyMethod: Literal[1, 2, 3]
        ) -> tuple[list[float], list[float], list[float]]:
    """计算耗能 (EnergyMethod=1时，等效弹性弹簧的应变能Es按该圈最大力算，=2时按该圈最大位移对应的力算，=3时按最大力和最大位移)

    Args:
        u_loops (list[np.ndarray]): 各圈滞回环的位移序列
        F_loops (list[np.ndarray]): 各圈滞回环的力序列
        EnergyMethod (Literal[1, 2, 3]): 等效弹性应变能Es的计算方法，1-Es按该圈最大力算，
        2-按该圈最大位移对应的力算，3-按最大力和最大位移

    Returns:
        tuple[list[float], list[float], list[float]]: 单圈耗能，累积耗能，等效阻尼
    """
    # 计算耗能 (EnergyMethod=1时，等效弹性弹簧的应变能Es按该圈最大力算，=2时按该圈最大位移对应的力算，=3时按最大力和最大位移)
    Es, Ea, zeta = [0], [0], [0]  # 单圈耗能，累积耗能，等效阻尼
    for i in range(len(u_loops)):
        u_seg, F_seg = u_loops[i], F_loops[i]
        S = np.sum((F_seg[: -1] + F_seg[1: ]) * (u_seg[1:] - u_seg[: -1]) / 2)
        Es.append(S)
        Ea.append(Ea[-1] + S)
        if EnergyMethod == 1:
            Ee = 0.5 * ((max(u_seg) * F_seg[np.argmax(u_seg)]) + (min(u_seg) * F_seg[np.argmin(u_seg)]))
        elif EnergyMethod == 2:
            Ee = 0.5 * ((u_seg[np.argmax(F_seg)] * max(F_seg)) + (u_seg[np.argmin(F_seg)] * min(F_seg)))
        elif EnergyMethod == 3:
            Ee = 0.5 * ((max(u_seg) * max(F_seg)) + (min(u_seg) * min(F_seg)))
        else:
            raise ValueError('EnergyMethod error')
        zeta.append(0.5 / np.pi * S / Ee)
    return Es, Ea, zeta