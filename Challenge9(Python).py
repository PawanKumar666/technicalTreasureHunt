etad= ['t','f','k','f','b','l','v','g','a','t','y','r']
raey = ['i','l','y','t','g','b','t','q','j','i','x','i','x','r','i','w','x','l','g','e','y','t','e','g','k','o','d','y','w','y']
htnom = ['n','o','e','i','u','m','h','q','b','t','4','z','b','t']
ans=list(zip(etad[4::-1],htnom[4::-1],raey[4:21:8]))
key=[]
for i in ans:
    key.append(list(i))
print("YourKeyIs : {}{}{}".format(((','.join(key[0])).replace(',','')),((','.join(key[1])).replace(',','')),((','.join(key[2])).replace(',',''))))#Find the pattern

#Wait a minute,What does the variables even mean!




#Created 4/4/21
