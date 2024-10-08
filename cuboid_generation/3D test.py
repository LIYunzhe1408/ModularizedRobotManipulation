import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial.transform import Rotation as R

# Function to generate random cuboid volumes
def random_cuboid_volume(total_volume, num_cuboids):
    volumes = np.random.rand(num_cuboids)
    volumes = volumes / np.sum(volumes) * total_volume
    return volumes

# Generate random cuboids with volumes summing to 0.1 m^3
volumes = random_cuboid_volume(0.1, 10)

# Function to generate random cuboids with random orientations
def generate_random_cuboid(vol, max_dim=1.0):
    dims = np.random.rand(3)
    dims = dims / np.prod(dims) * vol  # Adjust dimensions to match volume
    dims = np.cbrt(dims)               # Ensure valid scaling
    rotation = R.random().as_matrix()  # Random 3D rotation
    return dims, rotation

# Function to create and plot cuboids in a 3D environment
def plot_cuboids():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for vol in volumes:
        dims, rotation = generate_random_cuboid(vol)
        # Define cuboid corners in local space
        corners = np.array([[0, 0, 0], [dims[0], 0, 0], [dims[0], dims[1], 0], [0, dims[1], 0],
                            [0, 0, dims[2]], [dims[0], 0, dims[2]], [dims[0], dims[1], dims[2]], [0, dims[1], dims[2]]])
        # Apply random rotation and translation
        rotated_corners = np.dot(rotation, corners.T).T
        ax.scatter(rotated_corners[:, 0], rotated_corners[:, 1], rotated_corners[:, 2])

    plt.show()

# Plot cuboids
plot_cuboids()
