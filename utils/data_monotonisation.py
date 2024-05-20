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
            u_sublist = get_sublist(u_seg, j, 0.05)
            if abs(u_seg[j] - np.mean(u_sublist)) / abs(np.mean(u_sublist)) > 1:
                continue  # 如果当前位移点与前后5%的点的均值的相对误差超过1，则跳过
            if ((load > 0) and (u_seg[j] > max(u_seg_new))) or ((load < 0) and (u_seg[j] < min(u_seg_new))):
                u_seg_new.append(u_seg[j])
                F_seg_new.append(F_seg[j])
        u_new = np.append(u_new, u_seg_new)
        F_new = np.append(F_new, F_seg_new)
    return u_new, F_new


def get_sublist(data: np.ndarray, central_idx: int, range_: float
        ) -> np.ndarray:
    """获取一维数组data中某个点的前后range_*len(data)长度的子数组

    Args:
        ls (np.ndarray): 原始数组
        central_idx (int): 中心点的索引
        range (float): 子数组范围，如0.2代表取中心点的前20%和后20%的数据，取0~1
    
    Return (np.ndarray): 子数组(不包括中心数)
    """
    idx_range = int(range_ * len(data))
    idx_1 = max(0, central_idx - idx_range)
    idx_2 = min(len(data), central_idx + idx_range)
    return np.append(data[idx_1: central_idx], data[central_idx + 1: idx_2])


if __name__ == "__main__":
    data = np.linspace(0, 1, 100)
    res = get_sublist(data, 50, 0.2)
    print(res)
