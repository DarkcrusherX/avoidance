
import rospy
import sys
import copy
import rospy
import actionlib
from armf import armtakeoff
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


rospy.init_node('points',anonymous=True)

def main():

    client = actionlib.SimpleActionClient('move_base_simple',MoveBaseAction)
    client.wait_for_server()

    print("Enter coordinates x , y and z :")
    x = input(" x coordinate : ")
    y = input(" y coordinate : ")
    z = input(" z coordinate : ")

    goal = MoveBaseGoal()

    # goal = PoseStamped()
    # goal.header.frame_id = "local_origin"
    # goal.header.stamp = rospy.Time.now()
    # goal.pose.position.x = float(x)
    # goal.pose.position.y = float(y)
    # goal.pose.position.z = float(z)
    # goal.pose.orientation.w = 1.0
    # publish = rospy.Publisher('/global_temp_goal', PointStamped,queue_size=20)
    # while True:
    #     publish.publish(goal)

    goal.target_pose.header.frame_id = "local_origin"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = float(x)
    goal.target_pose.pose.position.y = float(y)
    goal.target_pose.pose.position.z = float(z)
    goal.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal)
    return client.get_result()


if __name__ == '__main__':
     try:
            result = main()
            if result:
                rospy.loginfo("Goal execution done!")
            armclass = armtakeoff()
            armclass.arm()
            armclass.takeoff()

     except rospy.ROSInterruptException:
            pass




