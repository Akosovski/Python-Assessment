
import math
def angle(opp, adj):
    # Use the arctangent function to calculate the angle
    angle_rad = math.atan2(opp, adj)
    
    # Convert the angle from radians to degrees
    angle_deg = math.degrees(angle_rad)
    
    return angle_deg

print(angle(3,4))