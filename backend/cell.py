from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class Cell:
    x: int
    y: int

    NEIGHBOUR_OFFSETS: ClassVar[tuple[tuple[int, int], ...]] = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    )

    def neighbours(self) -> tuple["Cell", ...]:
        return tuple(
            Cell(self.x + x_offset, self.y + y_offset)
            for x_offset, y_offset in Cell.NEIGHBOUR_OFFSETS
        )
