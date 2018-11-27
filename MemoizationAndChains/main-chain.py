from chain import *

if __name__ == '__main__':
  print("### witness → fatness")
  print(chain("witness", "fatness"))
  print("### warning → earring")
  print(chain("warning", "earring"))
  print("### sailing → writing")
  print(chain("sailing", "writing"))

# ### warning → earring
# ['warning', 'warring', 'barring', 'earring']
# ['warning', 'warring', 'barring', 'jarring', 'earring']
# ['warning', 'warring', 'earring']
# ['warning', 'warring', 'jarring', 'barring', 'earring']
# ['warning', 'warring', 'jarring', 'earring']
