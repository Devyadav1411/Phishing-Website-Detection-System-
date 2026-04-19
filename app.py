from flask import   Flask, render_template, request
import pickle
import re
app = Flask(__name__)

vector =pickle.load(open("vectorizer.pkl" , 'rb'))
model =pickle.load(open("phising.pkl", 'rb'))

@app.route("/" , methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        url = request.form['url']
        cleaned_url = re.sub(r'^https?://(www\.)?' , '', url)
        print(cleaned_url)
       # print(url)

        predict =model.predict(vector.transform([cleaned_url]))
        #print(predict)

        if predict =='bad':
            predict = "This is Phising Website !!"
        elif predict =='good':
            predict = "Hoorah, You are safe!! "
        else:
            predict ="Something went wrong!!"        

        return render_template("index.html", predict=predict)
    else:
        return render_template("index.html")



if __name__=="__main__":
    app.run(debug=True)
    