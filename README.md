4. Start the URDF File
Every URDF file must start with a declaration that it's an XML document:
<?xml version="1.0"?>

Then, you define the root tag of the URDF <robot>, which must include a name attribute:
<robot name="four_wheel_robot">
</robot>

So far, your full file should look like this:
<?xml version="1.0"?>
<robot name="four_wheel_robot">

</robot>

You’ve now created a valid (though empty) URDF robot structure
Understanding the Robot Structure
A robot description is built from two main elements:
Links → the physical parts of the robot
Joints → the connections between links
Think of links as LEGO pieces and joints as the connections that hold them together.
We will start by creating the main body of the robot.
5. Create the Robot Body
Add base_link
The main body of almost every robot is called base_link.
All wheels, sensors, and other components will eventually connect to this link.
Add the following inside the <robot> tag:
<link name="base_link">
    <visual>
      <geometry>
        <box size="0.6 0.4 0.2"/>
      </geometry>
      <material name="chassis_color">
        <color rgba="0.1 0.5 0.8 1.0"/>
      </material>
    </visual>
    <collision>
      <geometry>
        <box size="0.6 0.4 0.2"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="5.0"/>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <inertia ixx="0.083333" ixy="0.0" ixz="0.0"
               iyy="0.166667" iyz="0.0"
               izz="0.216667"/>
    </inertial>
  </link>

Understanding Visual Elements
The <visual> section defines how the robot looks.
<visual>

Inside it, we define a shape:
<geometry>
  <box size="0.6 0.4 0.2"/>
</geometry>

This creates a box with:
Length = 0.6 m
Width = 0.4 m
Height = 0.2 m
We also define a material:
<material name="blue">
  <color rgba="0.1 0.5 0.8 1.0"/>
</material>

which gives the robot its color.
Add Collision Geometry
The visual shape is only used for display.
Simulators also need a collision shape for physics calculations.
Add:
<collision>
  <geometry>
    <box size="0.6 0.4 0.2"/>
  </geometry>
</collision>

inside base_link.
Add Inertial Properties
The inertial section defines the robot mass and physical properties.
    <inertial>
      <mass value="5.0"/>
      <origin xyz="0 0 0" rpy="0 0 0"/>
      <inertia ixx="0.083333" ixy="0.0" ixz="0.0"
               iyy="0.166667" iyz="0.0"
               izz="0.216667"/>
    </inertial>

img
1- For a solid box of mass m with length L (x), width W (y), and height H (z), centered at its own center of mass, the formulas are:
ixx = (1/12) m (W² + H²)
iyy = (1/12) m (L² + H²)
izz = (1/12) m (L² + W²)
2- For a solid cylinder of mass m, radius r, and length h, with its symmetry axis along its own z, the standard formulas are:
izz (along the spin axis) = (1/2) m r²
ixx = iyy (perpendicular to the spin axis) = (1/12) m (3r² + h²)
Visualize the Robot Base
Use the URDF Visualizer extension in VS Code.
Open the command palette:
Ctrl + Shift + P

Select:
URDF Visualizer: Preview URDF

You should now see the robot body displayed as a blue box.
img
Add a Ground Reference Frame
Add base_footprint
Many mobile robots use a frame called base_footprint.
This frame sits on the ground directly underneath the robot.
Add:
<link name="base_footprint"/>

Connect base_footprint and base_link
Add the following joint:
<joint name="base_footprint_joint" type="fixed">

  <parent link="base_footprint"/>

  <child link="base_link"/>

  <origin xyz="0 0 0.15" rpy="0 0 0"/>

</joint>

This creates a fixed connection between the ground frame and the robot body.
The body is positioned 0.15 meters above the ground.
Why Do Robots Use base_footprint?
base_footprint represents the robot position on the floor.
base_link represents the actual robot body.
Add the Front Left Wheel
Create the Wheel Link
Add:
  <link name="front_left_wheel_link">
    <visual>
      <origin xyz="0 0 0" rpy="1.570796 0 0"/>
      <geometry>
        <cylinder radius="0.1" length="0.05"/>
      </geometry>
      <material name="wheel_color">
        <color rgba="0.1 0.1 0.1 1.0"/>
      </material>
    </visual>
    <collision>
      <origin xyz="0 0 0" rpy="1.570796 0 0"/>
      <geometry>
        <cylinder radius="0.1" length="0.05"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="0.5"/>
      <origin xyz="0 0 0" rpy="1.570796 0 0"/>
      <inertia ixx="0.001354" ixy="0.0" ixz="0.0"
               iyy="0.001354" iyz="0.0"
               izz="0.0025"/>
    </inertial>
  </link>

Understanding Wheel Orientation
By default, cylinders are aligned along the Z-axis.
Robot wheels rotate around the Y-axis.
Rotating the cylinder by 90° around X aligns it correctly:
rpy="1.57 0 0"

This makes the cylinder look like a wheel.
Create the Wheel Joint
  <joint name="front_left_wheel_joint" type="continuous">
    <parent link="base_link"/>
    <child link="front_left_wheel_link"/>
    <origin xyz="0.2 0.225 -0.05" rpy="0 0 0"/>
    <axis xyz="0 1 0"/>
  </joint>

The wheel can now rotate around the Y-axis.
img
Continue the exact same process for:
Add the Front Right Wheel
origin xyz="0.2 -0.225 -0.05"

Add the Rear Left Wheel
origin xyz="-0.2 0.225 -0.05"

Add the Rear Right Wheel
origin xyz="-0.2 -0.225 -0.05"

At this point, the robot is complete and should contain:
Robot Tree :
base_footprint
└── base_link
    ├── front_left_wheel_link
    ├── front_right_wheel_link
    ├── rear_left_wheel_link
    └── rear_right_wheel_link

img
