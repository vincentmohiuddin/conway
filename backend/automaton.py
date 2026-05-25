import logging
from collections.abc import Iterator

import numpy as np

from backend.cell import Cell

logger = logging.getLogger(__name__)


class Automaton:
    NEIGHBOURS_FOR_BIRTH = 3
    NEIGHBOURS_FOR_SURVIVAL = (2, 3)

    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols

    def run(self, initial_alive_cells: set[Cell]) -> Iterator[np.ndarray]:
        logger.info("starting run: %d initial alive cells", len(initial_alive_cells))
        alive_cells = self._clip_to_bounds(initial_alive_cells)
        yield self._to_matrix(alive_cells)
        step = 0
        while True:
            next_alive_cells = self._clip_to_bounds(self.get_next_alive_cells(alive_cells))
            step += 1
            if next_alive_cells == alive_cells:
                logger.info("stabilised at step %d", step)
                break
            alive_cells = next_alive_cells
            logger.debug("step %d: %d alive cells", step, len(alive_cells))
            yield self._to_matrix(alive_cells)

    @classmethod
    def get_next_alive_cells(cls, alive_cells: set[Cell]) -> set[Cell]:
        candidates = set(alive_cells)
        for alive_cell in alive_cells:
            candidates.update(alive_cell.neighbours())

        next_alive_cells = set()
        for cell in candidates:
            alive_neighbour_count = sum(
                neighbour in alive_cells for neighbour in cell.neighbours()
            )
            is_born = (
                alive_neighbour_count == cls.NEIGHBOURS_FOR_BIRTH
                and cell not in alive_cells
            )
            survives = (
                alive_neighbour_count in cls.NEIGHBOURS_FOR_SURVIVAL
                and cell in alive_cells
            )
            if is_born or survives:
                next_alive_cells.add(cell)
        return next_alive_cells

    def _clip_to_bounds(self, alive_cells: set[Cell]) -> set[Cell]:
        return {
            cell
            for cell in alive_cells
            if 0 <= cell.x < self.cols and 0 <= cell.y < self.rows
        }

    def _to_matrix(self, alive_cells: set[Cell]) -> np.ndarray:
        matrix = np.zeros((self.rows, self.cols), dtype=np.uint8)
        for cell in alive_cells:
            matrix[cell.y, cell.x] = 1
        return matrix
