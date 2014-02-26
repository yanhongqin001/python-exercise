people=20
cats=30
dogs=15
if people<cats:
    print "too many cats! the world is doomed"
elif people>cats:
    print "not many cats! the world is saved!"
else:
    print "we can't decide"
if people<dogs:
    print "the world is drooled on"
elif people>dogs:
    print "the world is dry"
else:
    print "the world is cool"
        
dogs+=5
if people>=dogs:
    print "people are greater than or equal to dogs"
elif people<=dogs:
    print "people are less than or equal to dogs"
else:
    print "people are dogs"
