Here are some SQLAlchemy methods you can use to query a single class:

query: This method allows you to query a class and return a Query object, which you can use to filter, order, and limit the results.

python
Copy code
from app import db, User

# Get all users
users = db.session.query(User).all()

# Get a specific user by ID
user = db.session.query(User).get(1)
filter: This method allows you to filter the results based on certain conditions. You can chain multiple filter calls to create more complex filters.

python
Copy code
from app import db, User

# Get all users with a specific username
users = db.session.query(User).filter_by(username='jdoe').all()

# Get all users with a specific email domain
users = db.session.query(User).filter(User.email.like('%@example.com')).all()
order_by: This method allows you to sort the results based on a specific column. You can use the desc method to sort in descending order.

python
Copy code
from app import db, User

# Get all users sorted by username in ascending order
users = db.session.query(User).order_by(User.username.asc()).all()

# Get all users sorted by email in descending order
users = db.session.query(User).order_by(User.email.desc()).all()
limit: This method allows you to limit the number of results returned.

python
Copy code
from app import db, User

# Get the first 10 users
users = db.session.query(User).limit(10).all()
first: This method allows you to retrieve the first result returned by the query.

python
Copy code
from app import db, User

# Get the first user with a specific username
user = db.session.query(User).filter_by(username='jdoe').first()
These are just a few examples of the many methods available in SQLAlchemy for querying a single class. By using these methods, you can easily retrieve and manipulate data from your database.





