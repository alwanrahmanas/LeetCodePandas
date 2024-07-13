class Solution:
    def __init__(self):
        # Peta simbol Romawi ke nilai integer
        self.roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
    def romanToInt(self, s: str) -> int:
        # Inisialisasi total
        total = 0
        
        # Iterasi melalui string angka Romawi
        for i in range(len(s)):
            # Jika simbol saat ini lebih kecil dari simbol berikutnya, kurangi dari total
            if i < len(s) - 1 and self.roman_to_int[s[i]] < self.roman_to_int[s[i + 1]]:
                total -= self.roman_to_int[s[i]]
            else:
                # Tambahkan nilai simbol ke total
                total += self.roman_to_int[s[i]]
        
        return total