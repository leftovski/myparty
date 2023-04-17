# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

# Create Flask app instance
app = Flask(__name__)
app.secret_key = 'mysecretkey'

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

# Create cursor object
mycursor = mydb.cursor()

# Define routes
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/shop')
def shop():
	# Get products from database
	mycursor.execute("SELECT * FROM products")
	products = mycursor.fetchall()
	return render_template('shop.html', products=products)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact
