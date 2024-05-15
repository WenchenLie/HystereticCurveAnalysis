import numpy as np

def data_monotonisation(u: np.ndarray, F: np.ndarray, tag: list[int]
        ) -> tuple[np.ndarray, np.ndarray]:
    """数据分段，并单调化

    Args:
        u (np.ndarray): 位移序列
        F (np.ndarray): 力序列
        tag (list[int]): 所有反向点的索引号

    Returns:
        tuple[np.ndarray, np.ndarray]: _description_
    """
    u_new, F_new = np.array([]), np.array([])
    for i in range(len(tag) - 1):
        tag1, tag2 = tag[i], tag[i + 1]
        load = u[tag2] - u[tag1]  # 加载方向（通过正负判断）
        u_seg, F_seg = u[tag1: tag2+1], F[tag1: tag2+1]
        u_seg_new, F_seg_new = [u_seg[0]], [F_seg[0]]
        for j in range(1, len(u_seg) - 1):
            if ((load > 0) and (u_seg[j] > max(u_seg_new))) or ((load < 0) and (u_seg[j] < min(u_seg_new))):
                u_seg_new.append(u_seg[j])
                F_seg_new.append(F_seg[j])
        u_new = np.append(u_new, u_seg_new)
        F_new = np.append(F_new, F_seg_new)
    return u_new, F_new
