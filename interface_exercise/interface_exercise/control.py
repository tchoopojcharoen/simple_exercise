import math

# go-to-goal control law
def go2goal(p,q,p_goal,Kv=1.0,Kw=5.0):
    p_err = [p_goal[0]-p[0],p_goal[1]-p[1]]
    #q_err = [p_err[0]*q[0]+p_err[1]*q[1],p_err[1]*q[0]-p_err[0]*q[1]]
    v = Kv*math.sqrt(p_err[0]**2+p_err[1]**2)
    w = Kw*(p_err[1]*q[0]-p_err[0]*q[1])
    return v,w
