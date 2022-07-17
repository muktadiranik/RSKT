import contextlib
import sqlite3
import string
import random
import datetime

def random_date():
    day = str(random.randint(1, 28))
    if len(day) < 2:
        day = "0" + day
    month = str(random.randint(1, 12))
    if len(month) < 2:
        month = "0" + month
    year = str(random.randint(2000, 2025))
    date = day + "/" + month + "/" + year
    return date

def random_month():
    month = str(random.randint(1, 12))
    if len(month) < 2:
        month = "0" + month
    year = str(random.randint(2000, 2025))
    date = month + "/" + year
    return date

def random_string(length):
    return ''.join((random.choice(string.ascii_uppercase) for x in range(length)))

def create_database():
    conn = sqlite3.connect("RSKT.db")
    cur = conn.cursor()
    sql = """CREATE TABLE if not exists member (
                    id INTEGER PRIMARY KEY, 
                    date TEXT, 
                    name TEXT, 
                    father_name TEXT, 
                    profession TEXT, 
                    workplace TEXT, 
                    address TEXT, 
                    phone TEXT, 
                    remarks TEXT                
                    )"""
    cur.execute(sql)
    conn.commit()

    sql = """CREATE TABLE if not exists receipt (
                    date TEXT, 
                    member_id INTEGER, 
                    member_name TEXT, 
                    amount INTEGER, 
                    payment_type TEXT, 
                    paid_for TEXT, 
                    payment_method TEXT, 
                    reference TEXT, 
                    remarks TEXT
                    )"""
    cur.execute(sql)
    conn.commit()

    sql = """CREATE TABLE if not exists income_expense (
                            year TEXT, 
                            monthly_contribution INTEGER, 
                            admit_fine INTEGER, 
                            form INTEGER, 
                            donation INTEGER, 
                            death_allowance INTEGER, 
                            disaster_allowance INTEGER, 
                            miscellaneous INTEGER, 
                            previous_balance INTEGER, 
                            new_balance INTEGER
                            )"""
    cur.execute(sql)
    conn.commit()

    sql = """CREATE TABLE if not exists bank_statement (
                            account_type TEXT, 
                            date TEXT, 
                            transaction_code TEXT, 
                            debit INTEGER, 
                            credit INTEGER, 
                            balance INTEGER, 
                            remarks TEXT 
                            )"""
    cur.execute(sql)
    conn.commit()

    sql = """CREATE TABLE if not exists self_expense (
                            date TEXT, 
                            purpose TEXT, 
                            amount INTEGER, 
                            remarks TEXT
                            )"""
    cur.execute(sql)
    conn.commit()

    conn.close()

def add_self_expense(n):
    amounts = [50, 100, 200, 400, 500, 600, 800, 1000]
    sql = """INSERT INTO self_expense VALUES (
    :date, 
    :purpose, 
    :amount, 
    :remarks
    )"""
    for i in range(n):
        date = random_date()
        purpose = random_string(20)
        amount = amounts[random.randint(0, 7)]
        remarks = random_string(10)
        conn = sqlite3.connect("RSKT.db")
        cur = conn.cursor()
        cur.execute(sql, {
            "date": date,
            "purpose": purpose,
            "amount": amount,
            "remarks": remarks
        })
        conn.commit()
        print(date, purpose, amount, remarks)
    conn.close()

def add_bank_statement(n):
    types = ["Savings Account", "FDR"]
    debits = [1000, 2000, 10000, 20000, 5000, 50000]
    credits = [1000, 2000, 10000, 20000, 5000, 50000]
    balances = [100000, 200000, 105020, 201050, 1020020, 2050010]
    conn = sqlite3.connect("RSKT.db")
    cur = conn.cursor()
    sql = """INSERT INTO bank_statement VALUES (
    :account_type,  
    :date, 
    :transaction_code, 
    :debit, 
    :credit, 
    :balance, 
    :remarks
    )"""
    for i in range(n):
        type = types[random.randint(0, 1)]
        date = random_date()
        transaction_code = random_string(20)
        debit = debits[random.randint(1, 5)]
        credit = credits[random.randint(1, 5)]
        balance = balances[random.randint(1, 5)]
        remarks = random_string(10)
        cur.execute(sql, {
            "account_type": type,
            "date": date,
            "transaction_code": transaction_code,
            "debit": debit,
            "credit": credit,
            "balance": balance,
            "remarks": remarks
        })
        conn.commit()
        print(type, date, transaction_code, debit, credit, balance, remarks)

    conn.close()

def add_member(n, m):
    sql = "INSERT INTO member VALUES (:id, :date, :name, :father_name, :profession, :workplace, :address, :phone, :remarks)"
    conn = sqlite3.connect("RSKT.db")
    cur = conn.cursor()
    for i in range(n, m):
        date = random_date()
        name = random_string(20)
        father_name = random_string(20)
        profession = random_string(20)
        workplace = random_string(20)
        address = random_string(40)
        phone = str(random.randint(1000000000, 9999999999))
        remarks = random_string(20)
        print(i, date, name, father_name, profession, workplace, address, phone, remarks)

        cur.execute(sql, {
            "id": i,
            "date": date,
            "name": name,
            "father_name": father_name,
            "profession": profession,
            "workplace": workplace,
            "address": address,
            "phone": phone,
            "remarks": remarks
        })
        conn.commit()

    conn.close()

def add_receipt(n):
    amounts = [50, 100, 200, 400, 500, 600, 800, 1000]
    payment_types = ["Due/Current/Advance", "Admit/Fine"]
    methods = ["Cash", "Mobile Banking"]

    conn = sqlite3.connect("RSKT.db")
    cur = conn.cursor()

    for i in range(n):
        member_id = random.randint(1, 199)
        sql = "SELECT name FROM member WHERE id = " + str(member_id)
        cur.execute(sql)
        items = cur.fetchone()
        conn.commit()
        payment_type = payment_types[random.randint(0, 1)]
        sql = """INSERT INTO receipt VALUES (
                    :date, 
                    :member_id, 
                    :member_name, 
                    :amount, 
                    :payment_type, 
                    :paid_for, 
                    :payment_method, 
                    :reference, 
                    :remarks
                    )"""

        member_name = items[0]
        date = random_date()
        amount = amounts[random.randint(0, 7)]

        paid_for = random_month()
        payment_method = methods[random.randint(0, 1)]
        reference = random_string(20)
        remarks = random_string(20)

        cur.execute(sql, {
            "date": date,
            "member_id": member_id,
            "member_name": member_name,
            "amount": amount,
            "payment_type": payment_type,
            "paid_for": paid_for,
            "payment_method": payment_method,
            "reference": reference,
            "remarks": remarks
        })
        conn.commit()
        print(date, member_id, member_name, amount, payment_type, paid_for, payment_method, reference, remarks)
    conn.close()

def add_income_expense(n):
    sql = """INSERT INTO income_expense VALUES (
        :year, 
        :monthly_contribution, 
        :admit_fine, 
        :form, 
        :donation, 
        :death_allowance, 
        :disaster_allowance, 
        :miscellaneous, 
        :previous_balance, 
        :new_balance
    )"""
    conn = sqlite3.connect("RSKT.db")
    cur = conn.cursor()
    for i in range(n):
        year = random.randint(2000, 2025)
        monthly_contribution = random.randint(1, 10) * 100
        admit_fine = random.randint(1, 10) * 100
        form = random.randint(1, 10) * 100
        donation = random.randint(1, 10) * 10000
        death_allowance = random.randint(1, 10) * 10000
        disaster_allowance = random.randint(1, 10) * 10000
        miscellaneous = random.randint(1, 10) * 100
        previous_balance = random.randint(1, 10) * 1000000
        new_balance = random.randint(1, 10) * 1000000
        cur.execute(sql, {
            "year": year,
            "monthly_contribution": monthly_contribution,
            "admit_fine": admit_fine,
            "form": form,
            "donation": donation,
            "death_allowance": death_allowance,
            "disaster_allowance": disaster_allowance,
            "miscellaneous": miscellaneous,
            "previous_balance": previous_balance,
            "new_balance": new_balance
        })
        conn.commit()
        print(year, monthly_contribution, admit_fine, form, donation, death_allowance, disaster_allowance, miscellaneous, previous_balance, new_balance)
    conn.close()

create_database()
add_member(1, 200)
add_receipt(4000)
add_bank_statement(200)
add_income_expense(100)
add_self_expense(200)
