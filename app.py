from flask import Flask,render_template


app=Flask(__name__, template_folder="template")


#first function=foward slash
@app.route("/index")
def first_webpage():
    #create a variable
    name = 'Flask'
    #pass the variable in the template
    return render_template('index.html',index_variable =  name)
app.run(debug=True)
