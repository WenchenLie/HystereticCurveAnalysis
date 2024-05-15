import numpy as np

def get_skeleton_curve_1(gujia_u, gujia_F, idx: int, previous_round=False):
    # 采用预设方案选择滞回环
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
    skt_u, skt_F = np.array([]), np.array([])
    for i in N:
        try:
            gujia_u[2 * i]
            gujia_u[2 * i + 1]
            gujia_F[2 * i]
            gujia_F[2 * i + 1]
            skt_u = np.append(skt_u, gujia_u[2 * i])
            skt_u = np.append(skt_u, gujia_u[2 * i + 1])
            skt_F = np.append(skt_F, gujia_F[2 * i])
            skt_F = np.append(skt_F, gujia_F[2 * i + 1])
        except:
            pass
    sorted_idx = np.argsort(skt_u)
    skt_u = skt_u[sorted_idx]
    skt_F = skt_F[sorted_idx]
    return skt_u, skt_F, N


def get_skeleton_curve_2(gujia_u, gujia_F, idx_list: list[list], previous_round=False):
    # 采用手动方案选择滞回环
    N = np.array(idx_list) - 1
    if previous_round:
        N -= 1  # 采用上一圈的数据（强度退化）
    skt_u, skt_F = np.array([]), np.array([])
    for i in N:
        try:
            gujia_u[2 * i]
            gujia_u[2 * i + 1]
            gujia_F[2 * i]
            gujia_F[2 * i + 1]
            skt_u = np.append(skt_u, gujia_u[2 * i])
            skt_u = np.append(skt_u, gujia_u[2 * i + 1])
            skt_F = np.append(skt_F, gujia_F[2 * i])
            skt_F = np.append(skt_F, gujia_F[2 * i + 1])
        except:
            pass
    sorted_idx = np.argsort(skt_u)
    skt_u = skt_u[sorted_idx]
    skt_F = skt_F[sorted_idx]
    return skt_u, skt_F, N    


if __name__ == "__main__":
    # N = get_skeleton_curve_1(1, 1, 0)
    N = get_skeleton_curve_2(1, 1, [1, 4, 7, 10, 13])
    # print(N)

