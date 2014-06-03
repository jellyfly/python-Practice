my_name = 'Jelly, Ming Tan'
my_age = 23 # not a lie
my_height = 158 # cm
my_weight = 120 # lbs
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "She's %d cm tall." % my_height
print "She's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "Her teeth are usually %s depending on the tea." % my_teeth

# this line is tricky try to get it exactly right
print "If I add %d, %d, and %d I get %d" % (my_age, my_height, my_weight,  my_age + my_height + my_weight)

strange = 'dsa'
print "Let's try to print this strange line %r." % strange

inch_height = my_height * 0.39370
kilo_weight = my_weight / 2.2046
print "Oh, let's convert to these units you are familiar: she is %.2f inches high and %.2f kg heavy." % (inch_height, kilo_weight)
