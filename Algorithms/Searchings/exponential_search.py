def binary_search(arr: list, start: int, end: int, find: int) -> int:
   if start != end:
      middle = (start + end) // 2
      if arr[middle] == find:
         return middle
      else:
         if arr[middle] < find:
            return binary_search(arr, middle+1, end, find)
         else:
            return binary_search(arr, start, middle-1, find)
   else:
      return -1


def exponential_search(arr: list, find: int) -> int:
   # check if arr is sorted
   if sorted(arr) == arr:
      if arr[0] == find:
         return 0

      index = 1
      while index < len(arr) and arr[index] <= find:
         index *= 2

      return binary_search(arr, index//2, min(index, len(arr)-1), find)
   
   raise ValueError("'arr' argument must be sorted")  # arr unsorted


def main():
   arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
   find = 11
   print(exponential_search(arr, find))


if __name__ == '__main__':
   main()
