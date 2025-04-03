from flask import Flask, render_template, request

def celsius_to_fahren(celsius):
    """Converts Celsius to Fahrenheit."""
    try:
        celsius = float(celsius)
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit, None  # Return Fahrenheit and no error
    except ValueError:
        return None, "Invalid input. Please enter a valid number."

app = Flask(__name__, template_folder="C:/Users/prave/win_drive_2/career\learning/repos/celsius_to_fahrenheit/celsius_to_fahrenheit/templates")

@app.route('/', methods=['GET', 'POST'])
def index():
    celsius = None
    fahrenheit = None
    error = None
    if request.method == 'POST':
        celsius_input = request.form['celsius']
        fahrenheit, error = celsius_to_fahren(celsius_input)
        if fahrenheit is not None:
            celsius = float(celsius_input)
    return render_template('index.html', celsius=celsius, fahrenheit=fahrenheit, error=error)

if __name__ == '__main__':
    #print(f"celsius_to_fahrenheit(0) = {celsius_to_fahren(0)}")
    app.run(debug=True)