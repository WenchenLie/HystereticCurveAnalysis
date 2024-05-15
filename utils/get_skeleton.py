import numpy as np

def get_skeleton(u, F, SkeletonMethod):
    tag_gujia = []
    i0 = 0
    for i in range(1, len(u) - 1):
        if (u[i+1] - u[i]) * (u[i] - u[i-1]) < 0:
            if SkeletonMethod == 1:
                # 通过最大位移对应的力确定骨架点
                tag_gujia.append(i)
            elif SkeletonMethod == 2:
                # 通过最大力确定骨架点
                if u[i] > u[i-1]:
                    # 正向
                    tag_gujia.append(i0 + np.argmax(F[i0: i]))
                else:
                    # 反向
                    tag_gujia.append(i0 + np.argmin(F[i0: i]))
            else:
                raise ValueError('Error 4')
            i0 = i
    return np.array(tag_gujia)