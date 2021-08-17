import hashlib

from flask.json import jsonify
import jwt
import mysql.connector
from flask import request, make_response

# These functions need to be implemented
class Token:
    secret = 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW'
    def generate_token(self, username, password):
        try:
            p, s, r = getEncriptPass(username)
        except:
            return "HTTP error message"
            #return make_response('HTTP error message', 403, {'WWW-Authenticate': 'Invalid user'})

        key = password+s
        passcript = hashlib.sha512(str(key).encode("utf-8")).hexdigest()

        if passcript==p:
            token = jwt.encode(
                headers={"alg": "HS256", "typ": "JWT"},
                payload = {"role":r},
                key=self.secret,
                algorithm='HS256'
            )
        
            return token
        else:
        #it should return a 403 HTTP error message.
            return 'HTTP error message'
            #return make_response('HTTP error message', 403, {'WWW-Authenticate': 'Invalid credentials'})

class Restricted:
    secret = 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW'
    def access_data(self, authorization):
        #print("aut : ", authorization)
        aut=authorization.split(' ')[1]
        try :
            val = jwt.decode(aut, self.secret, algorithms=['HS256'])
        except:
            val = {} 
            val["role"] = False
        
        if val["role"]:
            return 'You are under protected data'
        else :
            return '401'

def db():
    user = "secret"
    passw = "noPow3r"
    host = "bootcamp-tht.sre.wize.mx"
    db = "bootcamp_tht"

    mydb = mysql.connector.connect(
        host=host,
        user=user,
        password=passw, 
        db=db
    )
    return mydb

def getEncriptPass(username):
    conn = db()
    cur = conn.cursor()
    cur.execute("SELECT password, salt, role FROM users WHERE username='"+username+"'")
    res = cur.fetchone()
    conn.close()
    return res