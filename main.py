a =2
b=2
c  = "nomad code"
d= True
e = False
a_float = 3.12
print(a+b)
print(c)
print(d +e )
superLongVariable = True
print(superLongVariable)

days = "Mon, Tuem, Wed, Thur, Fri"
print(days)

week=["Mon","Tue","Wed","Thur","Fri"]
print(week)

# https://docs.python.org/3/library/

print("Mon" in week)

print(days[3])
# index starts at 0.

print(len(days))

#mutable is meant to be changable


week.append("Sat")
print(week)

#immutable sequence
#tuple

days= ("Mon","Tue","Wed","Thur","Fri")
print(type(days))

#dict

name = "Nico"
age = 29
korean =True
fav_food  = ["Kimchi","Sashimi"]

nico= {'name' : "Nico",
  'age' : 29,
  'korean' :True,
  'fav_food'  : ["Kimchi","Sashimi"]
}
print(nico)
nico["handsome"] = True
print(nico)

something = []


print(len("asdasdasdasd"))

age ="18"

print(type(age))
print(type(int(age)))



#create a function


def say_hello(who):
  print("hello",who)
  

say_hello("nico")

#given input

def plus(a,b):
  print(a + b)

plus(2,5)

#set a default
def minus(a,b=0):
  print(a-b)

minus(a)


def say_hello(name="anonymous"):
  print("hello",name)
say_hello()
say_hello("nico")

def p_plus(a,b):
  print(a+b)


def r_plus(a,b):
  return a + b



p_present = p_plus(2,3)
r_present = r_plus(2,3)

print(p_present,r_present)

#p_plus can save nothing

#retunr kill the function / execution


#positional argument
#if there is no indicator, deterministic

def plus(a,b):
  return a + b
result=plus(2,4)
print(result)


def sayhello(name,age):
  return f"Hello {name} you are {age} years old"
#format

hello = sayhello("nico","12")
print(hello)


hello = sayhello(age = "12",name = "nico")
print(hello)

# it is better to use key argument


def plus(a,b):
  if type(b) is int or type(b) is float:
    return a + b
  else :
    return None

print(plus(12,"10"))



def age_check(age):
  print(f"you are {age}")
  if age < 18:
    print("you cant drink")
  elif age ==18 or age == 19: 
    print("you are new to this!")
  elif age >20 and age <25:
    print("you are still kind of young")
  else :
    print("enjoy")
age_check(23)


days = ("Mon","Tue","Wed","Thu","Fri")


for day in days:
  if day == "Wed":
    break
  else:
    print(day)

