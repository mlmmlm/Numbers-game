import random
const = 8
anstue = random.randint(1,100)
while const > 0:
 temp = input("你猜猜是数字几：")
 guess = int(temp)
 if guess < 0:
     print("请输入1到100的整数")
     break
 else:
  if guess > 100:
      print("请输入1到100的整数")
      break
  else:
   
    if guess == anstue:
     print("你猜对了!")
     break
    else:
      if guess < anstue:
        print("小啦，你还有",const - 1,"次机会")
      else:
       print("大啦，你还有",const - 1,"次机会")
    const = const - 1
  if const == 0:
      print("失败了\n次数已用尽")
    
print("游戏结束")
  
