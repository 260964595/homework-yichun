#-*-coding:utf-8-*-
name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes='Blue'
teeth='White'
hair='Brown'
print "Let's talk about %s." % name
print "He's %d inches tall."%height
print "He's %d pounds heavy." % weight
print "Actaually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes,hair)
print "His teeth are usually %s depending on the coffee." % teeth
#this line is tricky,try to get it exactyly right
print "If I add %r,%r,and %d I get %d." %(age,height,weight,age+height+weight)