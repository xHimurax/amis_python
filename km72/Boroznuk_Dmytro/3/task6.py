import time
import math
first_group=int(input("Введите количество учеников в первой группе:"))
second_group=int(input("Введите количество учеников во второй группе:"))
third_group=int(input("Введите количество учеников в третей группе:"))
tables_in_the_first_class=math.ceil((first_group)/2)
tables_in_the_second_class=math.ceil((second_group)/2)
tables_in_the_third_class=math.ceil((third_group)/2)
print("Minimal number of tables: "+str(tables_in_the_first_class+tables_in_the_second_class+tables_in_the_third_class)+"")
time.sleep(3)
