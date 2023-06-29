import rospy

joint_states = rospy.wait_for_message("joint_states", JointState)
for i in joint_states:
    print("{}".format(i))
