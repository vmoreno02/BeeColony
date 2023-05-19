"""DTO for site information"""

from typing import Tuple


class Site:
    def __init__(self, pos: Tuple(int, int), quality: int) -> None:
        self.pos = pos
        self.quality = quality

    def get_pos(self) -> Tuple(int, int):
        return self.pos
    
    def set_pos(self, pos: Tuple(int, int)) -> None:
        self.pos = pos

    def get_quality(self) -> int:
        return self.quality
    
    def set_quality(self, quality: int) -> None:
        self.quality = quality