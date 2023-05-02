import math

PI = math.pi


def main():
    """this program calculates and prints the storage efficiency of different types of cans based on their dimensions"""
    create_can("#1 Picnic", 6.83, 10.16)
    create_can("#2", 8.73, 11.59)
    create_can("#2.5", 10.32, 11.91)
    create_can("#3 Cylinder", 10.79, 17.78)
    create_can("#5", 13.02, 14.29)
    create_can("#6Z", 5.4, 8.89)
    create_can("#8Z short", 6.83, 7.62)
    create_can("#10", 15.72, 17.78)
    create_can("#211", 6.83, 12.38)
    create_can("#300", 7.62, 11.27)
    create_can("#303", 8.1, 11.11)


def create_can(name: str, radius: float, height: float):
    """Create a can with the given name, radius, and height."""
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print_results(name, storage_efficiency)


def compute_volume(radius: float, height: float):
    """Compute and return the volume of a cylinder."""
    volume = PI * radius**2 * height
    return volume


def compute_surface_area(radius: float, height: float):
    """Compute and return the surface area of a cylinder."""
    surface_area = 2 * PI * radius * (radius + height)
    return surface_area


def compute_storage_efficiency(volume: float, surface: float):
    """Compute and return the storage efficiency."""
    storage_efficiency = volume/surface
    return storage_efficiency


def print_results(name: str, storage: float):
    """ prints results"""
    print(f"{name} {storage:.2f}")


if __name__ == "__main__":
    main()
