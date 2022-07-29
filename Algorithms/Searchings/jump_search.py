import math


def jump_search(arr:list, item:int):
   length = len(arr)
   step = int(math.sqrt(length))
   last_index = 0
   
   while arr[min(step, length)-1] < item:
      last_index = step
      step += int(math.sqrt(length))
      if last_index >= length:
         return -1
   
   while arr[last_index] < item:
      last_index += 1
      if last_index == min(step, length):
         return -1
   
   if arr[last_index] == item:
      return last_index
   return -1


def main():
   arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 30]
   item = 30
   print(jump_search(arr, item))


if __name__ == '__main__':
   main()
