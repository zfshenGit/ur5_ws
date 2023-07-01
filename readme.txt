source ./devel/setup.bash

仿真操作命令:
	1.启动ur5 gazebo仿真
		roslaunch ur_gazebo ur5.launch
		roslaunch ur_gazebo my_ur5.launch
	2.运行moveit规划程序
		roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch sim:=true
	3.运行rviz可视化配置界面
		roslaunch ur5_moveit_config moveit_rviz.launch config:=true		

实物操作命令:
	1.启动ur5驱动
		roslaunch ur_modern_driver ur5_bringup.launch
	2.运行moveit规划程序
		roslaunch ur5_moveit_config ur5_moveit_planning_execution.launch limited:=true
	3.运行rviz可视化配置界面
		roslaunch ur5_moveit_config moveit_rviz.launch config:=true
