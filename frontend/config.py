from pydantic import BaseModel


class GridConfig(BaseModel):
    rows: int
    cols: int


class InitialCellsConfig(BaseModel):
    alive_cells: list[tuple[int, int]]


class AppConfig(BaseModel):
    log_level: str
    grid: GridConfig
    initial_cells: InitialCellsConfig
