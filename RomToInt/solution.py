class Solution:
    def romanToInt(self, s: str) -> int:

        rom_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        _sum = 0

        for idx, val in enumerate(s):
            if idx+1 < len(s) and rom_int[val] < rom_int[s[idx+1]]:
                _sum-=rom_int[val]
            else:
                _sum+=rom_int[val]

        return _sum