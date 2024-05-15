import numpy as np


def get_dissipated_energy(u_loops, F_loops, EnergyMethod=1):
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