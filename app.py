from flask import Flask, render_template
app =  Flask(__name__)
# @app.route('the address for your page on your website")
# def {address}();
#    return render_template('{xyz.html}')
@app.route('/')
def home():
  return render_template("home.html")


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
