# Binary Search with Recursion Algorithm


def binary_search_recursion(arr: list, find: int) -> float:
   if len(arr) > 0:
      middle = len(arr) // 2
      if arr[middle] == find:
         return True
      else:
         if find < arr[middle]:
            return binary_search_recursion(arr[:middle], find)
         else:
            return binary_search_recursion(arr[middle + 1:], find)
   return False


def main():
   arr: list = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 , 22, 24, 25, 30]
   find: int = 1
   print(binary_search_recursion(arr, find))


if __name__ == '__main__':
   main()