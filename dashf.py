from flask import Flask  
import re
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "hello, this is our first flask website 2";  



if __name__ =='__main__':  
    app.run(debug = True)  

# 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