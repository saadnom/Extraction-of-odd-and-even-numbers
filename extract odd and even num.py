array = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = []
even_numbers = []
for i in array:
          if i%2==1:
               odd_numbers.append(i)
for j in array:
          if j%2==0:
               even_numbers.append(j)
          else:
               pass

print("These number are odd ",odd_numbers)
print("These number are even {}".format(even_numbers))