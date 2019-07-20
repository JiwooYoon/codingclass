from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

articles = []

## HTML을 주는 부분
@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/hw', methods=['POST'])
def hw():
   global articles

   name_receive = request.form['name_give']
   quantity_receive = request.form['quantity_give']
   address_receive = request.form['address_give']
   phone_receive = request.form['phone_give']

   article = {'name':name_receive,'quantity':quantity_receive, 'address':address_receive, 'phone':phone_receive}

   articles.append(article)

   return jsonify({'result':'success'})

@app.route('/hw', methods=['GET'])
def check():
   return jsonify({'result':'success', 'articles':articles})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5001,debug=True)