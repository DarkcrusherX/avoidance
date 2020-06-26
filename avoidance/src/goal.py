import rospy
from geometry_msgs.msg import PoseStamped
from armf import armtakeoff

rospy.init_node('goal',anonymous=True)

def main():

    print("Enter coordinates x , y and z :")
    x = input(" x coordinate : ")
    y = input(" y coordinate : ")
    #z = input(" z coordinate : ")

    publish = rospy.Publisher('/move_base_simple/goal', PoseStamped,queue_size=10)

    goal = PoseStamped()
    goal.header.frame_id = "local_origin"
    goal.header.stamp = rospy.Time.now()
    goal.pose.position.x = float(x)
    goal.pose.position.y = float(y)
<<<<<<< HEAD
    #goal.pose.position.z = float(z)
    goal.pose.orientation.z = 1
    #for i in range(1000000):
    rospy.sleep(1)
=======
    goal.pose.position.z = float(z)
    publish = rospy.Publisher('/move_base_simple/goal', PoseStamped,queue_size=20)

>>>>>>> 7923942e7d9ae33a6a070eee25e3110bd4a54c11
    publish.publish(goal)

if __name__ == '__main__':
     try:   
            armclass = armtakeoff()
            armclass.arm()
            armclass.takeoff()
            main()

     except rospy.ROSInterruptException:
            pass


