# Jump Search Algorithm


import math


def jump_search(arr: list, find: int) -> int:
   length = len(arr)
   jump = int(math.sqrt(length))
   index = 0

   while arr[min(jump, length-1)] < find:
      index = jump
      jump += int(math.sqrt(length))
      if index >= length:
         return -1
   
   while arr[index] < find:
      index += 1
   
   if arr[index] == find:
      return index
   return -1


def main():
   arr: list = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 , 22, 24, 25, 30]
   find: int = 30
   print(jump_search(arr, find))


if __name__ == '__main__':
   main()