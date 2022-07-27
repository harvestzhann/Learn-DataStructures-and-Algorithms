def sequential_search(arr:list, item:int) -> int:
   index: int = 0
   found = False
   
   # Scan arr from first to last index
   while index < len(arr) and not found:
      if arr[index] == item:
         found = True   # exit loop
      else:
         index += 1  # not found, go to next index
   
   if found:
      return index
   return -1   # not found


def main():
   arr = [3, 2, 5, 4, 1]
   item = 4

   print(sequential_search(arr, item))


if __name__ == '__main__':
   main()
