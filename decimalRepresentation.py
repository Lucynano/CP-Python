from typing import List

class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        return list(int(digit) * (10 ** (i - 1)) for digit, i in zip(str(n), range(len(str(n)), 0, -1)) if digit != '0')

