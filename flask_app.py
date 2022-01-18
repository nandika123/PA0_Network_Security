from flask import *

app = Flask(__name__)

'''Below function changes a cipher text string to plain text without the help 
of lookup table. 
It reverse the letters in the alphabet:
So, 'z' changes to 'a', 'y' changes to 'b' and so on. 
'''
def decipher_text(str):
    plain = ""
    for ch in str:
        if(ch==' '):
            plain = plain + " "
        else:
            plain = plain + chr(25-(ord(ch)-ord('a'))+ord('a'))
    return plain

'''Below function changes a plain text string to cipher text without the help 
of lookup table. 
It reverses the letters in the english alphabet.
So, 'a' changes to 'z', 'b' changes to 'y' and so on. 
'''
def encipher_text(str):
    cipher = ""
    for ch in str:
            if(ch==' '):
                cipher = cipher + " "
            else:
                cipher = cipher + chr(25-(ord(ch)-ord('a'))+ord('a'))
    return cipher

'''
Below two functions route the encipher and decipher buttons to the specific 
actions.
'''
@app.route('/', methods = ['POST', 'GET'])
def encipher():
        if request.method == 'POST':
            str = request.form["plaintext"]
            dec = encipher_text(str)
            return render_template('form.html', enc = str, dec = dec)
        else:
            return render_template('form.html')

@app.route('/decipher', methods = ['POST', 'GET'])
def decipher():
    if request.method == 'POST':
        str = request.form["ciphertext"]
        enc = decipher_text(str)
        return render_template('form.html', enc = enc, dec = str)
    else:
        return render_template('form.html')

if __name__ == "__main__":
    app.run()