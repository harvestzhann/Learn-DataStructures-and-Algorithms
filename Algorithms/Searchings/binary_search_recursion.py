def binary_search(arr:list, item:int) -> float:
   if len(arr) > 0:
      middle = len(arr) // 2
      if arr[middle] == item:
         return True
      else:
         if item < arr[middle]:
            return binary_search(arr[:middle], item)
         else:
            return binary_search(arr[middle+1:], item)
   else:
      return False


def main():
   arr = [0, 2, 4, 6, 8, 10, 12, 14]
   item = 12
   print(binary_search(arr, item))


if __name__ == '__main__':
   main()
