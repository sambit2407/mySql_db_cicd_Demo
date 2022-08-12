
from flask import Flask,render_template,request
from db_connection import store_data,fetch_employee


app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        data=request.form
        name=data['name']
        email=data['email']
        role=data['role']
        store_data(name,email,role)
        return 'Data Entry successful !! '

    return render_template('index.html')

@app.route('/users')
def users():
    userDetails=fetch_employee()
    return render_template('users.html',userDetails=userDetails)









if __name__=='__main__':
    app.run(debug=True)