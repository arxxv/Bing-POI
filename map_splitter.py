def map_points(points3):
    p1, p2, p3 = points3
    x_o, y_o, x_e, y_e = [], [], [], []
    conv = 1.0/111.0 #to convert latitude/longitude to km

    px, py = p1[0], p1[1]
    while px <= p3[0]:
        x_o.append(px)
        px += 2 * conv
    
    px = p1[0] + conv
    while px <= p3[0]:
        x_e.append(px)
        px += 2 * conv
    
    while py >= p2[1]:
        y_o.append(py)
        py -= 2 * conv
    
    py = p1[1] - conv
    while py >= p2[1]:
        y_e.append(py)
        py -= 2 * conv

    p_e, p_o = [[str(i),str(j)] for i in x_e for j in y_e], [[str(k),str(l)] for k in x_o for l in y_o]
    
    return p_e + p_o


