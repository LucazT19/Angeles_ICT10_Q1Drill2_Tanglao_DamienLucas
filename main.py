from pyscript import document

def compute(event):

    num1 = float(document.querySelector("#num1").value)
    num2 = float(document.querySelector("#num2").value)

    addition = num1 + num2

    subtraction = num1 - num2

    multiplication = num1 * num2

    if num2 == 0:
        division = "Cannot divide by zero"
    else:
        division = num1 / num2

    result = f"""
    Addition: {addition}<br>
    Subtraction: {subtraction}<br>
    Multiplication: {multiplication}<br>
    Division: {division}
    """

    document.querySelector("#result").innerHTML = result