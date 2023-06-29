# ur5_ws
ur5 robot with gazebo simulation and physical driver

## env
ubuntu20.04
ros noetic

## install

查看ros依赖

```commandline
rosdep check --from-paths src --ignore-src -r -y
```

安装依赖

```commandline
rosdep install --from-paths src --ignore-src -r -y
```

## use
### 1.仿真操作命令:

1.启动ur5 gazebo仿真

```comandline
source ./devel/setup.bash
roslaunch ur_gazebo ur5.launch
```
2.运行moveit规划程序

```comandline
roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true
```
3.运行rviz可视化配置界面

```comandline
roslaunch ur5_moveit_config moveit_rviz.launch config:=true
```
