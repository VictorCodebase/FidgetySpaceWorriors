print("I missed you python \n lets go!!!!!");

#loops
x = 0;
while x < 10:
     print (x);
     x = x + 1;
    
for i in range (0, 10, 2):
    print (i);
    
# using loops for various data structures

#? lists
list = ["Goi'n", "to", "Nodify", "this"];

for i in list:
     print(i);

#?tuples
tuple = ("tuppling", "over", "you", "😎👍", "Ps; you cannot change the order in a tuple without re-hard coding")
for i in tuple:
     print (i);

#?dictionary
dictionary = {
     'Alice' : "wonderland",
     'Nikola' : "AC",
     }
print (dictionary['Alice'])




#! classes
class testClass:
     def __init__(self, x: int, y: int) -> None:
          self.x = x
          self.y = y
          self.prod = 0
     def getSum(self) -> int:
          self.prod = self.x * self.y
          return self.prod
          

newObj = testClass(3, 5)

print(newObj.getSum(), "printed product")
          

