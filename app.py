from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
        <h1>Welcome to Varshi's Web App</h1>
        <p>This app is protected by Azure WAF!</p>
    """)

@app.route('/echo')
def echo():
    user_input = request.args.get("q", "")
    return f"You entered: {user_input}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
