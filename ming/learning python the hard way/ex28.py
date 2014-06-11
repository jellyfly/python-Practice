Q =[]

Q.append(True and True) 
Q.append(False and True)
Q.append(1==1 and 2==1)
Q.append("test" == "test")
Q.append(1 == 1 or 2 != 1)
Q.append(True and 1 == 1)
Q.append(False and 0 != 0)
Q.append(True or 1 == 1)
Q.append("test" =="testing")
Q.append(1 != 0  and 2 == 1)
Q.append("test" != "testing")
Q.append("test" == 1)
Q.append(not (True and False))
Q.append(not(1 == 1 and 0 != 1))
Q.append(not(10 == 1 or 1000 == 1000))
Q.append(not (1 != 10 or 3 == 4))
Q.append(not("testing" == "testing" and "Zed" == "Cool Guy"))
Q.append(1 == 1 and not ("testing" == 1 or 1 == 0))
Q.append("chunky" == "bacon" and not (3 == 4 or 3 == 3))
Q.append( 3 == 3 and not ("testing" == "testing" or "Python" == "Fun"))

index = 1
for x in Q:
    print index, ".", x
    index += 1
