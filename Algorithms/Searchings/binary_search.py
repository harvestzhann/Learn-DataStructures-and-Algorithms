def binary_search(arr:list, item:int):
   start, end = 0, len(arr)-1 # Searching range

   while start <= end:
      middle = (start + end) // 2 # Middle index
      if arr[middle] == item:
         return middle
      else:
         if item < arr[middle]:
            end = middle - 1 # Move range to the left
         else:
            start = middle + 1 # Move range to the right
         
   return -1 # Not found


def main():
   arr = [0, 2, 4, 6, 8, 10, 12, 14]
   item = 12
   print(binary_search(arr, item))


if __name__ == '__main__':
   main()
