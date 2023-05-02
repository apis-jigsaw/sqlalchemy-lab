If you only want to view the SQL statement for a specific SQLAlchemy query, you can use the statement method of the SQLAlchemy Query object. Here's an example:

python
Copy code
from app import db, User

# Create a new user
user = User(username='jdoe', email='jdoe@example.com')
db.session.add(user)
db.session.commit()

# Get the SQL statement for the last query
stmt = db.session.query(User).statement
print(stmt)
In this example, we're creating a new user and committing the changes to the database using the db.session.add() and db.session.commit() methods. After that, we're using the statement method to get the SQL statement for the last query that was executed, which is the query that inserted the new user into the database.

The statement method returns an instance of the SQLAlchemy Compiled class, which represents a compiled SQL statement. You can convert this to a string using the str method, as shown in the example above. This will print the SQL statement to the console output.