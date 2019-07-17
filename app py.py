from flask import Flask, render_template
app = Flask(__name__)

articles = []
article_no = 1

@app.route('/')
def home():
   return render_template('Order.html')


@app.route('/mypage')
def mypage():
   return render_template('index.html')

#API를 주는 부분
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
   return render_template('index.html')

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
   global articles
   global article_no

   url_receive = request.form['url_give']
   comment_receive = request.form['comment_give']
   category_receive = request.form['category_give']

   article = {}
   article['url'] = url_receive
   article['comment'] = comment_receive
   article['category'] = category_receive
   article['number'] = article_no

   articles.append(article)

   article_no = article_no + 1

   print(articles)

   return jsonify({'result':'success'})

@app.route('/test', methods=['GET'])
def test_get():
   global articles
   return jsonify({'result':'success', 'values' :articles})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)



@app.route('/delete', methods=['POST'])
def delete():
   global articles
   global article_no
   number_receive = request.form['number_give']

   for article in articles:
      if article['number'] == number_receive:
         articles.remove(article)

   return jsonify({'result':'success'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)