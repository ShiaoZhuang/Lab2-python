# Author: Shiao Zhuang sqz5328@psu.edu
# Collaborator: Ruimin Gao rpg5384@psu.edu
# Collaborator: Evan Eissfeldt eme5317@psu.edu
# Collaborator: Alondra Salinas avs6630@psu.edu
# Section: 1
# Breakout: 16
def getLetterGrade(n):
  n = float(n)
  if n >= 93.0:
    n = 'A'
  elif n >= 90.0:
    n = 'A-'
  elif n >= 87.0:
    n = 'B+'
  elif n >= 83.0:
    n = 'B'
  elif n >= 80.0:
    n = 'B-'
  elif n >= 77.0:
    n = 'C+'
  elif n >= 70.0:
    n = 'C'
  elif n >= 60.0:
    n = 'D'
  elif n < 60.0:
    n = 'F'
  return n


def run():
  n = float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(n)}.")

if __name__ == "__main__":
  run()