# Exponential Search Algorithm


def binary_search_recursion(arr: list, start: int, end: int, find: int) -> int:
   if len(arr) > 0:
      middle = (start + end) // 2
      if arr[middle] == find:
         return middle
      else:
         if find < arr[middle]:
            return binary_search_recursion(arr, start, arr[:middle], find)
         else:
            return binary_search_recursion(arr, arr[:middle], end, find)
   return -1


def exponential_search(arr: list, find: int) -> int:
   if arr[0] == find:
      return 0
   
   index = 1
   while arr[min(index, len(arr)-1)] < find:
      index *= 2
   
   return binary_search_recursion(arr, index//2, min(index, len(arr)-1), find)


def main():
   arr: list = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 , 22, 24, 25, 30]
   find: int = 1
   print(exponential_search(arr, find))


if __name__ == '__main__':
   main()