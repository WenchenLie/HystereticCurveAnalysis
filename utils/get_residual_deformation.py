def get_residual_deformation(u_loop, F_loop):

    d_pos, d_neg = 0, 0
    for i in range(1, len(u_loop) - 1):
        if F_loop[i] == 0 and u_loop[i] > 0:
            d_pos = u_loop[i]
            continue
        elif F_loop[i] == 0 and u_loop[i] < 0:
            d_neg = u_loop[i]
            continue
        elif F_loop[i] > 0 and F_loop[i + 1] < 0:
            k = (F_loop[i + 1] - F_loop[i]) / (u_loop[i + 1] - u_loop[i])
            d_pos = u_loop[i] - F_loop[i] / k
            continue
        elif F_loop[i] < 0 and F_loop[i + 1] > 0:
            k = (F_loop[i + 1] - F_loop[i]) / (u_loop[i + 1] - u_loop[i])
            d_neg = u_loop[i] - F_loop[i] / k
            continue
    # print(d_pos, d_neg)
    # if 23 < d_pos < 24:
    #     plt.plot(u_loop, F_loop)
    #     plt.plot([d_pos, d_neg], [0, 0], 'o')
    #     plt.show()
    return d_pos, d_neg