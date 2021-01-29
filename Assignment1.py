from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def firstpage():
    return render_template('view.html')

@app.route('/ResultView',methods=["POST","GET"])
def ResultView():
     n = int(request.form["userinput"])
     primfac = []
     d = 2
     primfac.append(n)
     while d <= n:
         if (n % d) == 0:
             n //= d
             primfac.append(n)
         else:
             d += 1

#    return primfac
#   primefactors = []
     return render_template("resultview.html",primefactors=primfac)

if __name__ == '__main__':
  app.run(debug=True,host='127.0.0.1',port=8000)
