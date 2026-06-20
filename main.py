from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

app = Flask(__name__)

# SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# -------------------------
# DATABASE MODELS
# -------------------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    balance = db.Column(db.Float, default=1000.0)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100))
    receiver = db.Column(db.String(100))
    amount = db.Column(db.Float)
    reference = db.Column(db.String(100))

# -------------------------
# CREATE DATABASE
# -------------------------

with app.app_context():
    db.create_all()

# -------------------------
# REGISTER USER
# -------------------------

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data['username']
    password = data['password']

    existing_user = User.query.filter_by(username=username).first()

    if existing_user:
        return jsonify({"message": "User already exists"}), 400

    hashed_password = generate_password_hash(password)

    new_user = User(
        username=username,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# -------------------------
# LOGIN
# -------------------------

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        return jsonify({
            "message": "Login successful",
            "balance": user.balance
        })

    return jsonify({"message": "Invalid username or password"}), 401

# -------------------------
# CHECK BALANCE
# -------------------------

@app.route('/balance/<username>', methods=['GET'])
def balance(username):

    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"message": "User not found"}), 404

    return jsonify({
        "username": user.username,
        "balance": user.balance
    })

# -------------------------
# TRANSFER MONEY
# -------------------------

@app.route('/transfer', methods=['POST'])
def transfer():

    data = request.get_json()

    sender_name = data['sender']
    receiver_name = data['receiver']
    amount = float(data['amount'])

    sender = User.query.filter_by(username=sender_name).first()
    receiver = User.query.filter_by(username=receiver_name).first()

    if not sender or not receiver:
        return jsonify({"message": "Invalid users"}), 404

    if sender.balance < amount:
        return jsonify({"message": "Insufficient balance"}), 400

    sender.balance -= amount
    receiver.balance += amount

    transaction_ref = str(uuid.uuid4())

    transaction = Transaction(
        sender=sender_name,
        receiver=receiver_name,
        amount=amount,
        reference=transaction_ref
    )

    db.session.add(transaction)
    db.session.commit()

    return jsonify({
        "message": "Transfer successful",
        "reference": transaction_ref
    })

# -------------------------
# TRANSACTION HISTORY
# -------------------------

@app.route('/transactions', methods=['GET'])
def transactions():

    all_transactions = Transaction.query.all()

    result = []

    for tx in all_transactions:
        result.append({
            "sender": tx.sender,
            "receiver": tx.receiver,
            "amount": tx.amount,
            "reference": tx.reference
        })

    return jsonify(result)

# -------------------------
# RUN SERVER
# -------------------------

if __name__ == '__main__':
    app.run(debug=True)# Main program entry point
