def ploshad(width, height): #Задание 2
    if width <= 0 or height <= 0:
        return "Ширина и высота прямоугольника должны быть положительными числами."
    else:
        area = width * height
        return area
def isprime(num): #Задание 3
   if num%2==0:
      return "Чётное"
   else:
      return "Нечётное"
def sum_cisel(num): #Задание 4
   if num < 0:
      return 0
   str_num = str(num)
   result = 0
   for i in str_num:
      result += int(i)
   return result

print("2) ",ploshad(65,45))
print("3) ",isprime(45))
print("4) ",sum_cisel(55))




