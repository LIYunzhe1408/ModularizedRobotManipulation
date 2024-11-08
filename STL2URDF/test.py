import numpy as np
from urdfpy import URDF, Link, Joint, Visual, Geometry, Mesh, Inertial, Collision, JointLimit

# Define a 4x4 identity matrix with translation for origin
origin_matrix = np.eye(4)
origin_matrix[:3, 3] = [0, 0, 0]  # translation part


inertial = Inertial(
    mass=1.0,  # mass in kg
    inertia=np.eye(3)
)

# Define the base link (parent link for the joint)
base_link = Link(
    name="base_link",  # Use this name as the parent link in the joint
    inertial=inertial,
    visuals=[],  # No visuals for the base link if not needed
    collisions=[]
)

# collision geometry
collision = Collision(
    name="collision_name",
    geometry=Geometry(mesh=Mesh(filename='../Stl/Stl/Base v2.stl')),
    origin=origin_matrix
)

# visual geometry
visual = Visual(
    geometry=Geometry(mesh=Mesh(filename='../Stl/Stl/Base v2.stl')),
    origin=origin_matrix
)

link = Link(
    name="child_link",  # Child link for the joint
    inertial=inertial,
    visuals=[visual],
    collisions=[collision]
)

limit = JointLimit(
    lower=-3.14,  # minimum rotation in rad
    upper=3.14,   # maximum rotation in rad
    effort=1.0,   # ?
    velocity=1.0  # max velocity
)

joint = Joint(
    name="joint_name",
    parent="base_link",
    child="child_link",
    joint_type="revolute",
    axis=(0, 0, 1),
    origin=origin_matrix,
    limit=limit
)


robot = URDF(
    name="robot_name",
    links=[base_link, link],
    joints=[joint]
)

# Write the URDF model to a file
robot.save('./robot.urdf')
