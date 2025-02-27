from flask import Flask, render_template, request  # Fix import

app = Flask(__name__)

@app.route('/')
def index():
    return """
        <html>
        <body>
            <form action="/greet" method="POST">
                Enter your name: <input type="text" name="username">
                <input type="submit" value="Submit">  <!-- Fix `values` to `value` -->
            </form>
        </body>
        </html>
    """

@app.route('/greet', methods=['POST'])  # Fix `method` to `methods`
def greet():
    user_input = request.form.get('username', 'Guest')  # Handle empty input
    return f"Hello {user_input}, Welcome to this app for Docker demonstration. Please consider liking and subscribing to the channel!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
