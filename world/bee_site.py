"""DTO for site information"""

from typing import Tuple


class Site:
    def __init__(self, pos, quality: int) -> None:
        self.pos = pos
        self.quality = quality

    def get_pos(self):
        return self.pos
    
    def set_pos(self, pos) -> None:
        self.pos = pos

    def get_quality(self) -> int:
        return self.quality
    
    def set_quality(self, quality: int) -> None:
        self.quality = quality