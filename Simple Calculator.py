# Hi devs , this is my first python project

print ( " This is the calculator made by me " . center(50) . upper() )
print ()
print ( " For Addition press 1 ")
print ( " For Subtraction press 2 ")
print ( " For Multiplication press 3 ")
print ( " For Division press 4 ")
print()
a = int (input ( " Enter your choice : "))

if ( a > 0 and a <5):
  b = int ( input ( " Enter the first number : "))
  c = int ( input ( " Enter the second number : "))
  
  if (a == 1):
    print ( "Answer : " , b+c )

  elif (a == 2):
    print ( "Answer : " ,  b-c )

  elif (a == 3):
    print ( "Answer : " ,  b*c )

  elif (a == 4):
    print ( "Answer : " ,  b/c )

  else:
    print (" Wrong Input")

else: 
  print(" Choose a valid Number between 1 to 4")

print (" Thanks for using the calcutor made by KUNSH")
print()
input ( "Press Enter to exit ")