# Easy Categories
# Copyright (c) 2022 Alvsch

## Importing Library
```python
from Category import *
```
## Creating Categories
```python
# Id is used to for you to identify a category (Set to any integer if you dont use it)
# Titel is the text displayed when the user is inputing

category0 = Category(id, title, req) #req is optional
```
	
## Attributes
```python
category0.addChild(ChildCategory) # Add child categories
category0.removeChild(ChildCategory) # Remove child categories

category0.hasChild() # Checks if the categories has any children
category0.isChild() # Checks if the category is a child (Will always return False in a Category)

category0.setFunc(function) # Set a function to be executed when the callFunc() method is called
category0.callFunc(*args) # Calls the function defined by the setFunc() function
```


## Creating Child Categories
```python
# Id is used to for you to identify a category (Set to any integer if you dont use it)
# Titel is the text displayed when the user is inputing

ChildCategory0 = ChildCategory(id, title)
```
	
## Attributes
```python
childcategory0.addChild(ChildCategory) # Add child categories
childcategory0.removeChild(ChildCategory) # Remove child categories

ChildCategory0.hasChild() # Checks if the categories has any children
ChildCategory0.isChild() # Checks if the category is a child (Will always return True in a ChildCategory)

ChildCategory0.setFunc() # Set a function to be executed when the callFunc() method is called
ChildCategory0.callFunc() # Calls the function defined by the setFunc() function
```
	
## Selection
```python
# Enter an unlimited amount of categories, The user can select from them and you can handle the action

selection(c0, c1, c2) 
```


## Basic Example
```python
from categories import *

# Copyright (c) 2022 Alvsch

#Defining Categories
c0 = Category(0, "Help")
c1 = Category(0, "Exit")


while True:
	selected_category = selection(c0, c1)
	print(selected_category.name)
```
		
### Output

	[0] Help
	[1] Exit

	Select Action: 0
	Help


	[0] Help
	[1] Exit

	Select Action: 1
	Exit


	[0] Help
	[1] Exit

	Select Action: 
			
## Example With Functions
```python
from categories import *

# Copyright (c) 2022 Alvsch

# Defining Functions
def help_func():
    print("This is a really bad help menu, don't make menus like these")


# Defining Categories
c0 = Category(0, "Help")
c1 = Category(0, "Exit")

#Setting Functions
c0.setFunc(help_func)  # DO NOT HAVE () IN THE END OF THE FUNCTION, JUST THE NAME
c1.setFunc(lambda: exit()) # Simple lambda expression


while True:
    selected_category = selection(c0, c1)
    selected_category.callFunc() # Call the function instead of printing name
```	
### Output

	[0] Help
	[1] Exit

	Select Action: 0
	This is a really bad help menu, don't make menus like these


	[0] Help
	[1] Exit

	Select Action: 1

	Process finished with exit code 0

## Example With Requirements
```python
from categories import *

# Copyright (c) 2022 Alvsch

var0 = 1
var1 = 2

# To add a variable use an f"" string and add {variable} and to add ", do \"
c0 = Category(0, "I can't be seen", f"{var0} == {var1}")  # Sorry for the bad input formatting :(

c1 = Category(0, "I can be seen")

while True:
    selected_category = selection(c0, c1)
    print(selected_category.name)
```

### Output
	[0] I can be seen

	Select Action: 0
	I can be seen
	
	#If we then would change var1 to 1 so the value would be True
	
	[0] I can't be seen
	[1] I can be seen

	Select Action: 0
	I can't be seen
	


## Example With Children
```python
from categories import *

# Copyright (c) 2022 Alvsch

# Defining Functions
def not_coders():
	print("Also Alvsch")

def help():
	print("This is a really bad help menu, don't make menus like these")	


#Defining Categories
c0 = Category(0, "Help")
c1 = Category(0, "Credits")
c2 = Category(0, "Exit")


# Defining Children
cc0 = ChildCategory(0, "Coders")
cc1 = ChildCategory(0, "Not Coders")
# Setting Functions to Child Categories
cc0.setFunc(lambda: print("Alvsch"))
cc1.setFunc(not_coders) # DO NOT HAVE () IN THE END OF THE FUNCTION, JUST THE NAME


# Adding Children to the "c1" Category
c1.addChild(cc0)
c1.addChild(cc1)


# Setting Functions to Categories
c0.setFunc(help) # DO NOT HAVE () IN THE END OF THE FUNCTION, JUST THE NAME

# c1 Does not need a function because it has children and the function won't be called

c2.setFunc(lambda: exit())


while True:
	selected_category = selection(c0, c1, c2)
	selected_category.callFunc()
```	
### Output
	[0] Help
	[1] Credits
	[2] Exit

	Select Action: 1
	
	
	[0] Coders
	[1] Not Coders

	Select Action: 0
	Alvsch


	[0] Help
	[1] Credits
	[2] Exit

	Select Action: 1
	
	
	[0] Coders
	[1] Not Coders

	Select Action: 1
	Also Alvsch


	[0] Help
	[1] Credits
	[2] Exit

	Select Action: 2
	
	Process finished with exit code 0
	
	
	
	
	
	
	
	
	
