import contact_tracing_form
class database:

    def __init__(self):
        import sqlite3
        con = sqlite3.connect('contract_tracerDB.db')

        try:
            con.cursor()
            print("successful")
        except Exception as ex:
            print("fail")

