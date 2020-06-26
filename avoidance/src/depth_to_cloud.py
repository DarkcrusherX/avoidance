
import rospy
from sensor_msgs.msg import PointCloud2

rospy.init_node('cloudpoints',anonymous=True)

points= PointCloud2()


def callback(msg):

    publish.publish(points)
    print(points)


publish = rospy.Publisher("/trial", PointCloud2,queue_size=20)
subscriber = rospy.Subscriber("/camera/depth/points",PointCloud2,callback)

rospy.spin()




