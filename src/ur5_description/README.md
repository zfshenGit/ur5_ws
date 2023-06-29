# Using

## 1.在当前工作空间下

```commandlind
source ./devel/setup.bash
roscd ur5_description/urdf/
# xacro转urdf
rosrun xacro xacro ur5_robot.urdf.xacro > ur5.urdf --inorder
# check urdf
check_urdf ur5.urdf
# 写入pdf
urdf_to_graphiz agv.urdf
# rviz可视化
roslaunch ur5_description ur5_rviz.launch
```
