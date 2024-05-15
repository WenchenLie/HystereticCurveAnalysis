import numpy as np

def smooth(u: np.ndarray, F: np.ndarray, window_size: int) -> tuple[np.ndarray, np.ndarray]:
    """采用简单移动平均算法平滑曲线(simple_moving_average)

    Args:
        u (np.ndarray): 位移序列
        F (np.ndarray): 力序列
        window_size (int): 窗口尺寸

    Returns:
        tuple[np.ndarray, np.ndarray]: 平滑前、平滑后的力序列
    """
    i0 = 0
    F_new = F.copy()
    for i in range(1, len(u) - 1):
        if (u[i + 1] - u[i]) * (u[i] - u[i - 1]) < 0:
            F_seg = F[i0: i + 1]
            F_seg_new = _SMA(F_seg, window_size)
            F_new[i0: i + 1] = F_seg_new
            i0 = i
    F_new[i0:] = _SMA(F[i0:], window_size)
    return F, F_new


def _SMA(data: np.ndarray, window_size: int) -> list[float]:
    """简单移动平均算法

    Args:
        data (np.ndarray): 待平滑数据序列
        window_size (int): 窗口尺寸

    Returns:
        list[float]: 平滑后数据
    """
    data_smooth = []
    window_half = int(window_size / 2)
    for i in range(len(data)):
        if i - window_half >= 0 and i + window_half <= len(data):
            data_smooth.append(np.average(data[i - window_half: i + window_half]))
        elif i - window_half < 0:
            if i == 0:
                data_smooth.append(data[0])
            else:
                data_smooth.append(np.average(data[: 2 * i]))
        elif window_half + i > len(data):
            data_smooth.append(np.average(data[2 * i - (len(data) -1 ):]))
        else:
            raise ValueError('1')
    return data_smooth