import numpy as np

def loops_division(u, F, skip=0):
    # 滞回曲线分圈 (skip=1时跳过最后一圈，防止最后一圈不完整)
    u_loops, F_loops = [], []
    length = 2  # 数据总长度
    u_seg, F_seg = u[: 2].tolist(), F[: 2].tolist()
    for i in range(2, len(u)):
        if (u[i] == 0 and u[i - 1] < 0):
            u_loops.append(u_seg)
            F_loops.append(F_seg)
            length += len(u_seg)
            u_seg, F_seg = [u[i]], [F[i]]
        elif u[i] > 0 and u[i - 1] < 0:
            u_loops.append(u_seg)
            F_loops.append(F_seg)
            length += len(u_seg)
            u_seg, F_seg = [u[i]], [F[i]]
        else:
            u_seg.append(u[i])
            F_seg.append(F[i])
    else:
        if skip == 0 and len(u_seg) > 1:
            u_loops.append(u_seg)
            F_loops.append(F_seg)
            length += len(u_seg)
    u_loops = [np.array(loop) for loop in u_loops]
    F_loops = [np.array(loop) for loop in F_loops]
    return u_loops, F_loops, length