from dataclasses import dataclass

@dataclass
class Actor:
    id: int = 0
    first_name: str = ""
    last_name: str = ""
    birth_year: int = 0

    def detail(self):
        det_str = f"{self.id} - {self.last_name}, {self.first_name}: born in {self.birth_year}"
        return det_str