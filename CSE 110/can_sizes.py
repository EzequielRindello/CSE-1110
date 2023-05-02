import math


def main():

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


def create_can(name, radius, height):
    volume = compute_volume(radius, height)
    surface = compute_surface_area(radius, height)
    storage = storage_efficiency(volume, surface)
    print_results(name, storage)


def compute_volume(radius, height):
    """Compute and return the volume of a cylinder."""
    volume = math.pi * radius**2 * height
    return volume


def compute_surface_area(radius, height):
    """Compute and return the surface area of a cylinder."""
    surface = 2 * math.pi * radius * (radius + height)
    return surface


def storage_efficiency(volume, surface):
    """Compute and return the storage efficiency."""
    storage = volume/surface
    return storage


def print_results(name, storage):
    """ prints results"""
    print(f"{name} {storage:.2f}")


if __name__ == "__main__":
    main()
