import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend

from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
import io
import base64

def generate_quantum_circuit(qbits, gate_choices, apply_cnot):
    """Creates a quantum circuit based on user-selected gates and applies CNOT if requested."""
    circuit = QuantumCircuit(qbits)

    for i, gate in enumerate(gate_choices):
        if gate == "H":
            circuit.h(i)
        elif gate == "X":
            circuit.x(i)
        elif gate == "Y":
            circuit.y(i)
        elif gate == "Z":
            circuit.z(i)

    # Apply CNOT if requested
    if apply_cnot and qbits > 1:
        circuit.cx(0, 1)  # Apply CNOT from qubit 0 to qubit 1

    # Create Matplotlib figure
    fig, ax = plt.subplots()
    circuit.draw('mpl', ax=ax)  # Explicitly draw on the created figure

    # Save the figure as an image
    img_stream = io.BytesIO()
    fig.savefig(img_stream, format='png', bbox_inches='tight')  # Ensure proper cropping
    plt.close(fig)  # Close figure to prevent memory leaks
    img_stream.seek(0)

    # Encode to base64 for HTML display
    encoded_img = base64.b64encode(img_stream.read()).decode("utf-8")
    return encoded_img

