def binary_search_recursion(arr:list, find:int) -> float:
   # check if arr is sorted
   if sorted(arr) == arr:
      if len(arr) > 0:
         middle = len(arr) // 2
         if arr[middle] == find:
            return True
         else:
            if find < arr[middle]:
               return binary_search_recursion(arr[:middle], find)
            else:
               return binary_search_recursion(arr[middle+1:], find)
      else:
         return False
   
   raise ValueError("'arr' must be sorted")


def main():
   arr = [0, 2, 4, 6, 8, 10, 12, 14]
   find = 12
   print(binary_search_recursion(arr, find))


if __name__ == '__main__':
   main()
