import numpy as np


def get_skeleton_curve_1(
        gujia_u: np.ndarray,
        gujia_F: np.ndarray,
        gujia_d: np.ndarray,
        idx: int,
        previous_round: bool=False
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """采用预设方案选择滞回环

    Args:
        gujia_u (np.ndarray): 所有骨架点的横坐标序列
        gujia_F (np.ndarray): 所有骨架点的纵坐标序列
        gujia_d (np.ndarray): 所有骨架点的附属数据序列
        idx (int): 预设方案的索引号，从0到8
        previous_round (bool, optional): 当前方案是否存在上一圈滞回环，默认False

    Returns:
        tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: 骨架曲线横坐标、纵坐标及附属数据对应骨架曲线方案所采用的滞回环索引号
    """
    n = np.arange(1, 100, 1)
    if idx == 0:
        N = 3 * n - 2
    elif idx == 1:
        N = 3 * n - 1
    elif idx == 2:
        N = 3 * n
    elif idx == 3:
        N = 2 * n - 1
    elif idx == 4:
        N = 2 * n
    elif idx == 5:
        N = n
    elif idx == 6:
        N = np.array([6, 12, 16, 18])
        N = np.append(N, 2 * n[n > 9])
    elif idx == 7:
        N = np.array([5, 11, 15, 17])
        N = np.append(N, 2 * n[n > 9] - 1)
    elif idx == 8:
        N = np.array([1, 2, 3, 6, 9])
        N = np.append(N, 3 * n[n > 3]) 
    else:
        raise ValueError('下拉列表索引不存在')
    N -= 1
    if previous_round:
        N -= 1  # 采用上一圈的数据（强度退化）
    skt_u, skt_F, skt_d = np.array([]), np.array([]), np.zeros((0, gujia_d.shape[1]))
    for i in N:
        try:
            gujia_u[2 * i + 1]  # 先执行语句捕获异常，否则会导致skt_u和skt_F长度不一致
            skt_u = np.append(skt_u, gujia_u[2 * i])
            skt_u = np.append(skt_u, gujia_u[2 * i + 1])
            skt_F = np.append(skt_F, gujia_F[2 * i])
            skt_F = np.append(skt_F, gujia_F[2 * i + 1])
            skt_d = np.append(skt_d, gujia_d[2 * i, np.newaxis], axis=0)
            skt_d = np.append(skt_d, gujia_d[2 * i + 1, np.newaxis], axis=0)
        except Exception as error:
            if not type(error) is IndexError:
                raise error
    sorted_idx = np.argsort(skt_u)
    skt_u = skt_u[sorted_idx]
    skt_F = skt_F[sorted_idx]
    skt_d = skt_d[sorted_idx]
    return skt_u, skt_F, skt_d, N


def get_skeleton_curve_2(
        gujia_u: np.ndarray,
        gujia_F: np.ndarray,
        gujia_d: np.ndarray,
        idx_list: list[list],
        previous_round: bool=False
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """采用手动方案选择滞回环

    Args:
        gujia_u (np.ndarray): 所有骨架点的横坐标序列
        gujia_F (np.ndarray): 所有骨架点的纵坐标序列
        gujia_d (np.ndarray): 所有骨架点的附属数据序列
        idx_list (list[list]): 要用来计算骨架曲线的滞回环的索引号
        previous_round (bool, optional): 当前方案是否存在上一圈滞回环，默认False

    Returns:
        tuple[np.ndarray, np.ndarray, np.ndarray]: 骨架曲线横坐标、纵坐标及附属数据对应骨架曲线方案所采用的滞回环索引号
    """
    # 采用手动方案选择滞回环
    N = np.array(idx_list) - 1
    if previous_round:
        N -= 1  # 采用上一圈的数据（强度退化）
    skt_u, skt_F, skt_d = np.array([]), np.array([]), np.zeros((0, gujia_d.shape[1]))
    for i in N:
        try:
            skt_u = np.append(skt_u, gujia_u[2 * i])
            skt_u = np.append(skt_u, gujia_u[2 * i + 1])
            skt_F = np.append(skt_F, gujia_F[2 * i])
            skt_F = np.append(skt_F, gujia_F[2 * i + 1])
            skt_d = np.append(skt_d, gujia_d[2 * i, np.newaxis], axis=0)
            skt_d = np.append(skt_d, gujia_d[2 * i + 1, np.newaxis], axis=0)
        except Exception as error:
            if not type(error) is IndexError:
                raise error
    sorted_idx = np.argsort(skt_u)
    skt_u = skt_u[sorted_idx]
    skt_F = skt_F[sorted_idx]
    skt_d = skt_d[sorted_idx]
    return skt_u, skt_F, skt_d, N    


if __name__ == "__main__":
    # N = get_skeleton_curve_1(1, 1, 0)
    N = get_skeleton_curve_2(1, 1, [1, 4, 7, 10, 13])
    print(N)

