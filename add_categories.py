from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Category, Base, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# First category
category1 = Category(name="Soccer")

session.add(category1)
session.commit()

Item1 = Item(name="Soccar Ball", description="You definitely need this in order to play soccer",
             category_name="Soccer", category=category1)

session.add(Item1)
session.commit()


Item2 = Item(name="Shin Guards", description="Protect your legs",
             category_name="Soccer", category=category1)

session.add(Item2)
session.commit()

# Second category
category2 = Category(name="Basketball")

session.add(category2)
session.commit()

Item1 = Item(name="basketball", description="You definitely need this in order to play soccer",
             category_name="Basketball", category=category2)

session.add(Item1)
session.commit()


Item2 = Item(name="Hoop", description="Usally placed at 10ft",
             category_name="Basketball", category=category2)

session.add(Item2)
session.commit()

# Third category
category3 = Category(name="Baseball")

session.add(category3)
session.commit()

Item1 = Item(name="baseball", description="You definitely need this in order to play this sport",
             category_name="Baseball", category=category3)

session.add(Item1)
session.commit()


Item2 = Item(name="Glove", description="Usally placed on your hand, the only necessary equiptment for playing defense",
             category_name="Baseball", category=category3)

session.add(Item2)
session.commit()

# Forth category
category4 = Category(name="Frisbee")

session.add(category4)
session.commit()

Item1 = Item(name="Frisbee", description="You definitely need this in order to play Frisbee.  Infact, it is all you need",
             category_name="Frisbee", category=category4)

session.add(Item1)
session.commit()


# Fifth category
category5 = Category(name="Snowboarding")

session.add(category5)
session.commit()

Item1 = Item(name="Down Jacket", description="This will keep you warm on the mountain",
             category_name="Snowboarding", category=category5)

session.add(Item1)
session.commit()


Item2 = Item(name="Gloves", description="Very Important.  Hands are often the first to get cold in extreme conditions",
             category_name="Snowboarding", category=category5)

session.add(Item2)
session.commit()

# Sixth category
category6 = Category(name="Rock Climbing")

session.add(category6)
session.commit()

Item1 = Item(name="100m rope", description="Keep yourself or your partner safe as you climb",
             category_name="Rock Climbing", category=category6)

session.add(Item1)
session.commit()


Item2 = Item(name="Rock Climbing Shoes", description="These help your feet stick to the rock",
             category_name="Rock Climbing", category=category6)

session.add(Item2)
session.commit()

# 7 category
category7 = Category(name="Foosball")

session.add(category7)
session.commit()

Item1 = Item(name="Table", description="You probably need this to play",
             category_name="Foosball", category=category7)

session.add(Item1)
session.commit()


Item2 = Item(name="Replacement Balls", description="Very Important.  These can be easily lost",
             category_name="Foosball", category=category7)

session.add(Item2)
session.commit()

# 8 category
category8 = Category(name="Skating")

session.add(category8)
session.commit()

Item1 = Item(name="Skates", description="Made for ice or hard surfaces.  Find out where you will be skating first",
             category_name="Skating", category=category8)

session.add(Item1)
session.commit()

# 9 category
category9 = Category(name="Hockey")

session.add(category9)
session.commit()

Item1 = Item(name="Puck", description="You probably need this to play",
             category_name="Hockey", category=category9)

session.add(Item1)
session.commit()


Item2 = Item(name="Pads", description="Very Important.  Hockey is a brutal sport and you need to protect your body",
             category_name="Hockey", category=category9)

session.add(Item2)
session.commit()