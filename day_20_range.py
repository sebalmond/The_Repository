start = 200
end = 300
increment = 20

print ("Example:")
print ("Start at:", start)
print ("End before:", end)
print ("Increment between values:", increment)
print ("")


for i in range (start, end, increment):
  print(i)

print ("")
start = int(input("Start at:"))
end = int (input("End at:"))
increment = int(input("Increment between values:"))
print ("")

for i in range (start, end, increment):
  print(i)