from backend.cell import Cell


def test_neighbours_returns_eight_cells():
    assert len(Cell(0, 0).neighbours()) == 8


def test_cell_not_own_neighbour():
    assert Cell(1, 1) not in Cell(1, 1).neighbours()


def test_neighbours_positions():
    neighbours = set(Cell(1, 1).neighbours())
    expected = {
        Cell(0, 0),
        Cell(1, 0),
        Cell(2, 0),
        Cell(0, 1),
        Cell(2, 1),
        Cell(0, 2),
        Cell(1, 2),
        Cell(2, 2),
    }
    assert neighbours == expected
