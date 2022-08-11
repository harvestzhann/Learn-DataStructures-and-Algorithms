def binary_search_recursion(arr: list, start: int, end: int, find: int) -> int:
   # check if arr is sorted
   if sorted(arr) == arr:
      if start != end:
         middle = (start + end) // 2
         if arr[middle] == find:
            return middle
         else:
            if find < arr[middle]:
               return binary_search_recursion(arr, start, middle-1, find)
            else:
               return binary_search_recursion(arr, middle+1, end, find)
      else:
         return -1
   
   raise ValueError("'arr' must be sorted")


def main():
   arr = [0, 2, 4, 6, 8, 10, 12, 14]
   find = 12
   print(binary_search_recursion(arr, 0, len(arr)-1, find))


if __name__ == '__main__':
   main()
