# Testing a Python CLI

In this we did 3 types of tests
### 1) Unit testing
Unit tests are tests written exactly one specific thing.
For eg
In unit test we essentially tested our object creation
and tests mostly fall in two brackets..
a) When we create an object lets' say
```
obj=PythonClass(arg1,arg2)

Testing is done to check if Class signature has not changed
assertEqual(obj1.arg1,arg1)

```
b) The other unit tests we write are basically for member functions.
where we say 
```
obj1.func()==expected_output
```


### 2) Integration testing

In these tests we usually test combination of two or more 
features that we tested using unit tests.
The idea here is to understand how the two features interact with each other

For eg an intergration test would be 
```
obj1=Class1(...)
obj2=Class2(...)

obj2.some_function(obj1)==expected_output

```

### System Testing 