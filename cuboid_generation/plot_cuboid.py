import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial.transform import Rotation as R

# Function to generate cuboid vertices
def cuboid_data(origin, size):
    """ Create cuboid vertices based on the origin and size. """
    x = [origin[0], origin[0] + size[0]]
    y = [origin[1], origin[1] + size[1]]
    z = [origin[2], origin[2] + size[2]]
    return np.array([[x[0], y[0], z[0]],
                     [x[1], y[0], z[0]],
                     [x[1], y[1], z[0]],
                     [x[0], y[1], z[0]],
                     [x[0], y[0], z[1]],
                     [x[1], y[0], z[1]],
                     [x[1], y[1], z[1]],
                     [x[0], y[1], z[1]]])

# Function to plot cuboid
def plot_cuboid(ax, cuboid):
    """ Plot cuboid using its vertices. """
    vertices = [[cuboid[0], cuboid[1], cuboid[2], cuboid[3]],
                [cuboid[4], cuboid[5], cuboid[6], cuboid[7]],
                [cuboid[0], cuboid[1], cuboid[5], cuboid[4]],
                [cuboid[2], cuboid[3], cuboid[7], cuboid[6]],
                [cuboid[1], cuboid[2], cuboid[6], cuboid[5]],
                [cuboid[4], cuboid[7], cuboid[3], cuboid[0]]]

    faces = Poly3DCollection(vertices, linewidths=1, edgecolors='r', alpha=.25)
    ax.add_collection3d(faces)

# Function to check for overlap between two cuboids using their axis-aligned bounding boxes (AABB)
def check_overlap(cub1_min, cub1_max, cub2_min, cub2_max):
    """ Check if two cuboids overlap based on their AABBs (axis-aligned bounding boxes). """
    return not (cub1_max[0] < cub2_min[0] or cub1_min[0] > cub2_max[0] or
                cub1_max[1] < cub2_min[1] or cub1_min[1] > cub2_max[1] or
                cub1_max[2] < cub2_min[2] or cub1_min[2] > cub2_max[2])

# Random cuboid volume generation
def random_cuboid_volume(total_volume, num_cuboids):
    volumes = np.random.rand(num_cuboids)
    volumes = volumes / np.sum(volumes) * total_volume
    return volumes

# Function to generate cuboid size, ensuring it fits within the space and respects a maximum size
def generate_random_cuboid(vol, max_size, space_size=(1.0, 1.0, 1.0)):
    """ Generates random cuboid dimensions, ensuring that no dimension exceeds the maximum size. """
    dims = np.random.rand(3)
    dims = dims / np.prod(dims) * vol  # Ensure the product equals the cuboid volume
    dims = np.cbrt(dims)               # Adjust dimensions to ensure valid scaling
    dims = np.minimum(dims, max_size)  # Apply maximum size constraint to each dimension
    return dims

# Plot cuboids and ensure no overlap
def plot_random_cuboids(num_cuboids=20, total_volume=0.001, space_size=(1.0, 1.0, 1.0), max_size=(0.5, 0.5, 0.5)):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    cuboids = []
    volumes = random_cuboid_volume(total_volume, num_cuboids)
    attempts = 0

    while len(cuboids) < num_cuboids and attempts < 1000:
        vol = volumes[len(cuboids)]
        dims = generate_random_cuboid(vol, max_size)

        # Generate random position ensuring the cuboid is within space boundaries
        origin = np.random.rand(3) * (np.array(space_size) - dims)

        # Calculate min and max corners for the AABB
        cub_min = origin
        cub_max = origin + dims

        # Check for overlap with all previously placed cuboids
        if all(not check_overlap(cub_min, cub_max, cub[0], cub[1]) for cub in cuboids):
            cuboids.append((cub_min, cub_max))
            cuboid = cuboid_data(cub_min, dims)
            plot_cuboid(ax, cuboid)
        attempts += 1

    # Set axis labels and limits
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([0, space_size[0]])
    ax.set_ylim([0, space_size[1]])
    ax.set_zlim([0, space_size[2]])
    plt.show()

# Plot the cuboids with a maximum size of 0.5 in each dimension
plot_random_cuboids(max_size=(0.2, 0.3, 0.2))