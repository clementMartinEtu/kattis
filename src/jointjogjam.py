import math

#https://open.kattis.com/problems/jointjogjam?editresubmit=18872489

def compute_max_distance(x1, y1, x2, y2, x3, y3, x4, y4):
    dx = (x3 - x1) - (x4 - x2)
    dy = (y3 - y1) - (y4 - y2)
    X0 = x1 - x2
    Y0 = y1 - y2

    a = dx*dx + dy*dy
    b = 2 * (X0*dx + Y0*dy)
    c = X0*X0 + Y0*Y0
    if a == 0:
        t_candidates = [0, 1] 
    else:
        t_vertex = -b / (2*a)
        t_vertex = max(0, min(1, t_vertex))
        t_candidates = [0, 1, t_vertex]

    Dmax2 = max((X0 + dx*t)**2 + (Y0 + dy*t)**2 for t in t_candidates)
    Dmax = math.sqrt(Dmax2)

    return Dmax

compute_max_distance(0, 0, 0, 0, 1, 1, 2, 2)