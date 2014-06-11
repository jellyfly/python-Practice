people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

# can't believe that python doesn't have an official multiline comment operator!
# The following is the solution for extra credit section
# 1. you only can execute the code under if when you satisfy the condition after if
# 2. so that we can know where the chunk of code begins and where does it end.
# 3. tried once, it said : IndentationError: expected an indented block
# 4. as follows

if people != cats:
    print "neither can everyone have a cat nor can every cat have an owner"

# 5. it depends on the relationship between them.    
