from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Category, Base, Item, User

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create first user
User1 = User(name="Avery Berkowitz",
             email="aman1321@yahoo.com"
             )
session.add(User1)
session.commit()

# First category
category1 = Category(name="Soccer")

session.add(category1)
session.commit()

Item1 = Item(user_id=1,
             name="Soccar Ball",
             description="You definitely need this in order to play soccer",
             category_name="Soccer", category=category1)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1,
             name="Shin Guards", description="Protect your legs",
             category_name="Soccer", category=category1)

session.add(Item2)
session.commit()

# Second category
category2 = Category(name="Basketball")

session.add(category2)
session.commit()

Item1 = Item(user_id=1,
             name="basketball",
             description="You definitely need this in order to play soccer",
             category_name="Basketball", category=category2)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1,
             name="Hoop", description="Usally placed at 10ft",
             category_name="Basketball", category=category2)

session.add(Item2)
session.commit()

# Third category
category3 = Category(name="Baseball")

session.add(category3)
session.commit()

Item1 = Item(user_id=1,
             name="baseball",
             description="You definitely need this",
             category_name="Baseball", category=category3)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1,
             name="Glove",
             description="Usally placed on your hand",
             category_name="Baseball", category=category3)

session.add(Item2)
session.commit()

# Forth category
category4 = Category(name="Frisbee")

session.add(category4)
session.commit()

Item1 = Item(user_id=1,
             name="Frisbee",
             description="You definitely need this in order to play.",
             category_name="Frisbee", category=category4)

session.add(Item1)
session.commit()


# Fifth category
category5 = Category(name="Snowboarding")

session.add(category5)
session.commit()

Item1 = Item(user_id=1,
             name="Down Jacket",
             description="This will keep you warm on the mountain",
             category_name="Snowboarding", category=category5)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1,
             name="Gloves",
             description="Hands are often the first to get cold.",
             category_name="Snowboarding", category=category5)

session.add(Item2)
session.commit()

# Sixth category
category6 = Category(name="Rock Climbing")

session.add(category6)
session.commit()

Item1 = Item(user_id=1,
             name="100m rope",
             description="Keep yourself or your partner safe as you climb",
             category_name="Rock Climbing", category=category6)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1,
             name="Rock Climbing Shoes",
             description="These help your feet stick to the rock",
             category_name="Rock Climbing", category=category6)

session.add(Item2)
session.commit()

# 7 category
category7 = Category(name="Foosball")

session.add(category7)
session.commit()

Item1 = Item(user_id=1,
             name="Table",
             description="You probably need this to play",
             category_name="Foosball", category=category7)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1,
             name="Replacement Balls",
             description="Very Important.  These can be easily lost",
             category_name="Foosball", category=category7)

session.add(Item2)
session.commit()

# 8 category
category8 = Category(name="Skating")

session.add(category8)
session.commit()

Item1 = Item(user_id=1,
             name="Skates",
             description="Made for ice or hard surfaces.",
             category_name="Skating", category=category8)

session.add(Item1)
session.commit()

# 9 category
category9 = Category(name="Hockey")

session.add(category9)
session.commit()

Item1 = Item(user_id=1,
             name="Puck",
             description="You probably need this to play",
             category_name="Hockey", category=category9)

session.add(Item1)
session.commit()


Item2 = Item(user_id=1,
             name="Pads",
             description="You need to protect your body",
             category_name="Hockey", category=category9)

session.add(Item2)
session.commit()
