import  os

def delect(dir1,dir2):
  list2=os.listdir(dir2)
  list3=[]
  for i in list2:
      list3.append(i)

  list1=os.listdir(dir1)
  for i in list1:
      if i  in list3:
        os.remove(dir1+ '\\'+i)
      else:
          continue

if __name__ == '__main__':
    dir1=r"E:\CV04\train\test\B"     #需要被去重的文件夹
    dir2=r"E:\CV04\train\test\A"     #源文件夹
delect(dir1,dir2)
