def merge_sort(arr,left, right):
  print "ID: %s, %s" % (id(arr[left:right]),arr[left:right])
  n = len(arr[left:right])
  if n < 3:
      sort(arr[left:right])
      return
  p = n/2
  merge_sort(arr,left,left+p)
  print "foo: %s" % arr
  merge_sort(arr,left+p,right)
  merge(arr,left+p-1)


def merge(arr,div):
  print "Merging: %s, div: %s, id: %s" % (arr,div,id(arr))
  if not arr: return
  n = len(arr)
  if n == 1: return
  while div < n-1:
      right = div + 1
      left = right - 1
      print "... %s, div: %s, right: %s, left: %s" % (arr,div,right,left)
      while right > 0:
          try: arr_right = arr[right]
          except:
               print "oh no: %s, %s" % (arr, right)
               raise
          arr_left = arr[left]
          print "arr_left: %s, arr_right: %s" % (arr_left, arr_right)
          if arr_right < arr_left:
              swap(arr, right, left)
              print "After swap: %s" % arr
              right = left
              left = right - 1
          else: break
      div = div + 1


def swap(arr, right, left):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

def sort(arr):
  print "Sorting: %s" % arr
  if len(arr)==1: return
  if len(arr)>2: raise Exception("Array must have length less than 3.")
  left = arr[0]
  right = arr[1]
  if left > right:
    temp = left
    arr[0] = right
    arr[1] = temp
  print "should be sorted: %s" % arr
  return

if __name__ == '__main__':
    import sys
    from random import shuffle
    l = range(0,int(sys.argv[1]))
    shuffle(l)
    print "Sorting: %s, %s" % (id(l),l)
    import pdb ; pdb.set_trace()
    merge_sort(l,0, len(l))
    print "Sorted: %s" % l

"""
Take aways:
  * when dealing with arrays in Python, you have to stick with the same array and just 
    muck with indices
  * check your "stop" conditions very carefully
  * check your array bounds, off-by-1 conditions very carefully
"""
