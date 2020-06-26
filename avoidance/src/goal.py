
import rospy
from geometry_msgs.msg import PoseStamped
from armf import armtakeoff

rospy.init_node('goal',anonymous=True)

def main():

    print("Enter coordinates x , y and z :")
    x = input(" x coordinate : ")
    y = input(" y coordinate : ")
    z = input(" z coordinate : ")

    goal = PoseStamped()
    goal.header.frame_id = "local_origin"
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = float(x)
    goal.pose.position.y = float(y)
    goal.pose.position.z = float(z)
    publish = rospy.Publisher('/move_base_simple/goal ', PoseStamped,queue_size=20)

    publish.publish(goal)

if __name__ == '__main__':
     try:   
            main()
            armclass = armtakeoff()
            armclass.arm()
            armclass.takeoff()

     except rospy.ROSInterruptException:
            pass




