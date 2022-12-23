# MENCARI TINGGI SEGITIGA
import math

a = int(input("Masukkan alas segitiga : "))
b = int(input("Masukkan sisi miring segitiga : "))
c = int(math.sqrt(b**2 - a**2))

print(f"tinggi segitiga = {c}")
