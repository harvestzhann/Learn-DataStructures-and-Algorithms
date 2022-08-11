def interpolation_search(arr: list, find: int) -> int:
   # check if arr is sorted
   if sorted(arr) == arr:
      start, end = 0, len(arr) - 1

      while start <= end:
         if arr[start] == find:
            return start
         if arr[end] == find:
            return end

         pointer = start + ((find - arr[start]) * (end - start) // (arr[end] - arr[start]))

         if arr[pointer] == find:
            return pointer
         else:
            if arr[pointer] < find:
               start = pointer + 1
            else:
               end = pointer - 1
      return -1
   
   raise ValueError("'arr' argument must be sorted")  # arr unsorted


def main():
   arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 30]
   find = 10
   print(interpolation_search(arr, find))


if __name__ == '__main__':
   main()