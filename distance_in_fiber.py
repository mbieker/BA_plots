
import numpy as np

def distance_in_fiber(x , fiber_radius):
    if(abs(x)>fiber_radius):
        return 0
    return 2*np.sqrt(fiber_radius**2-x**2)


def distance_in_mat(x , fiber_radius, fiber_pitch, num_layers):
    
    #Pattern is periodic with fiber pitch
    x = x % fiber_pitch
    num_s = int(num_layers/2)
    num_u= num_layers-num_s
    #First Fibers in unshifted rows
    output = num_u*distance_in_fiber(x,fiber_radius)
    #Fiber in shifted rows bootom right shifted rows
    output += num_s*distance_in_fiber(x-fiber_pitch/2,fiber_radius)
    #Nex fibers to ther right in unshited rows
    output += num_u*distance_in_fiber(x-fiber_pitch, fiber_radius) 
    #calculate total length traveled in mat
    total = 2*fiber_radius+(num_layers-1)*0.21
    return output/total
distance_in_mat = np.vectorize(distance_in_mat)

