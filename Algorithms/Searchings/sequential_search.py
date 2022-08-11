def sequential_search(arr: list, find: int) -> int:
   index: int = 0
   
   # Iterate arr from first to last index
   while index < len(arr):
      if arr[index] == find:
         return index
      else:
         index += 1  # not found, go to next index
   
   return -1   # not found


def main():
   arr = [3, 2, 5, 4, 1]
   find = 4
   print(sequential_search(arr, find))


if __name__ == '__main__':
   main()
