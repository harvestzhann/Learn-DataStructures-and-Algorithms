import math


def jump_search(arr: list, find: int):
   # check if arr is sorted
   if sorted(arr) == arr:
      length = len(arr)
      step = int(math.sqrt(length))
      last_index = 0
      
      while arr[min(step, length) - 1] < find:
         last_index = step
         step += int(math.sqrt(length))
         if last_index >= length:
            return -1
      
      # sequnecial search
      while arr[last_index] < find:
         last_index += 1
      
      if arr[last_index] == find:
         return last_index
      return -1

   raise ValueError("first argument must be sorted")  # arr unsorted


def main():
   arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 30]
   find = 30
   print(jump_search(arr, find))


if __name__ == '__main__':
   main()
