from flask import Flask, render_template, request
from quantum_circuit import generate_quantum_circuit

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    qbits = 2  # Default qubits
    img_data = None
    gate_choices = ["H"] * qbits  # Default gates
    apply_cnot = False  # Default CNOT state

    if request.method == "POST":
        qbits = int(request.form["qbits"])
        gate_choices = [request.form.get(f"gate_{i}", "H") for i in range(qbits)]
        apply_cnot = "apply_cnot" in request.form  # Check if checkbox was submitted

        img_data = generate_quantum_circuit(qbits, gate_choices, apply_cnot)

    return render_template("index.html", img_data=img_data, qbits=qbits, gate_choices=gate_choices, apply_cnot=apply_cnot)

if __name__ == "__main__":
    app.run(debug=True)

