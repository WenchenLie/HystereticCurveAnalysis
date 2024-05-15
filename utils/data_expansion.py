import numpy as np

def data_expansion(u, F, min_du):
    # 数据扩充
    def LinearInterpolation(P1, P2, n):
        # 线性插值函数（n为分割段数）
        x1, y1 = P1
        x2, y2 = P2
        k = (y2 - y1) / (x2 - x1)
        dx = (x2 - x1) / n
        x_add = [x1 + i * dx for i in range(1, n)]
        y_add = [y1 + i * dx * k for i in range(1, n)]
        return (x_add, y_add)
    u_new, F_new = np.array([u[0]]), np.array([F[0]])
    for i in range(1, len(u)):
        P1, P2 = (u_new[-1], F_new[-1]), (u[i], F[i])
        n = int(abs((u[i] - u_new[-1]) / min_du)) + 1
        if n > 1:
            u_new = np.append(u_new, LinearInterpolation(P1, P2, n)[0])
            F_new = np.append(F_new, LinearInterpolation(P1, P2, n)[1])
        u_new = np.append(u_new, u[i])
        F_new = np.append(F_new, F[i])
    return u_new, F_new