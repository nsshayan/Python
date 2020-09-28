from flask import Flask, request

app = Flask('login_flask')

@app.route("/")
def show_login():
    output = """
    <html>
       <form name="login_form" method="POST" action="/login">
          Enter username: <input type="text" name="uname" /><br />
          Enter password: <input type="password" name="passwd" /><br />
          <input type="submit" name="login" value="Login" /><br />
       </form>
    </html>
    """
    return output

@app.route("/login", methods=["POST"])
def login():
    return """
      <h1>Logging in!</h1>
      <table border="1">
        <tr><td>Username</td><td>{}</td></tr>
        <tr><td>Password</td><td>{}</td></tr>
      </table>
      """.format(request.form["uname"], request.form["passwd"])


app.run(debug=True)



