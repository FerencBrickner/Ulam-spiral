import matplotlib.pyplot as plt
from sympy import isprime
from typing import Final


def generate_ulam_spiral(
    *,
    GRID_SIZE: Final[int] = 301,
    DIRECTIONS: Final[list[tuple]] = [
        right := (1, 0),
        up := (0, -1),
        left := (-1, 0),
        down := (0, 1),
    ],
    current_number: int = 1,
    steps_in_direction: int = 1,
    direction_index: int = 0,
) -> list[list[int]]:
    assert GRID_SIZE % 2 == 1
    spiral = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    current_x_coordinate: int = GRID_SIZE // 2
    current_y_coordinate: int = GRID_SIZE // 2
    NUMBER_OF_DIRECTIONS: Final[int] = len(DIRECTIONS)
    SPIRAL_SIZE: Final[int] = GRID_SIZE**2
    while current_number <= SPIRAL_SIZE:
        for _ in range(2):
            for _ in range(steps_in_direction):
                try:
                    spiral[current_y_coordinate][current_x_coordinate] = isprime(
                        current_number
                    )
                except IndexError:
                    "we stepped out of the spiral"
                    return spiral
                current_x_coordinate += DIRECTIONS[direction_index][0]
                current_y_coordinate += DIRECTIONS[direction_index][1]
                current_number += 1
            direction_index += 1
            direction_index %= NUMBER_OF_DIRECTIONS
        steps_in_direction += 1


def plot_ulam_spiral(*, spiral, color_scheme: str = "binary") -> None:
    plt.imshow(spiral, cmap=color_scheme)


def setup_plot(
    *,
    plot_title: str = "Ulam Spiral",
    figure_size: int = 10,
) -> None:
    plt.figure(figsize=(figure_size, figure_size))
    plt.title(plot_title)
    plt.axis("off")


def main(*args, **kwargs) -> None:
    """
    Drawing the Ulam spiral.
    https://en.wikipedia.org/wiki/Ulam_spiral
    """
    setup_plot()
    ulam_spiral: list[list[int]] = generate_ulam_spiral()
    plot_ulam_spiral(spiral=ulam_spiral)
    plt.show()


if __name__ == "__main__":
    main()
