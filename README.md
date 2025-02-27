#  Quantum Circuit Visualizer  
A **web-based quantum circuit visualizer** that allows users to create, simulate, and visualize quantum circuits using **Qiskit** and **Flask**.

## Overview
<img width="1081" alt="Screenshot 2025-02-27 at 2 48 41 pm" src="https://github.com/user-attachments/assets/c5eab0ff-0ef5-4d9e-b60b-4b6d2598d868" />

### Explanation
#### 1. User Interface (HTML, CSS)
- The user selects qubits & quantum gates via a web form.
#### 2. Flask Web Server (`app.py`)
- Handles form submissions and sends data to the circuit generator.
#### 3. Form Input Handler
- Reads number of qubits and selected gates (H, X, Y, Z, CNOT).
#### 4. Quantum Circuit Generator (`quantum_circuit.py`)
- Uses Qiskit to create a quantum circuit with the user’s selections.
#### 5. Circuit Visualization
- Converts the circuit into a Matplotlib-rendered image (PNG).
#### 6. Flask Response
- Returns the image to the HTML page for display.
#### 7. Browser Displays Output
- The user sees a visualized quantum circuit in their browser.


## Features
- **Select Number of Qubits** (1-5)
- **Choose Quantum Gates** (H, X, Y, Z)
- **Apply CNOT Gate** (Qubit 0 → Qubit 1)
- **View Circuit Diagram** (Generated using Qiskit & Matplotlib)
- **Web-Based UI** (Powered by Flask)

## Installation

### 1. Prerequisites
- Ensure you have **Python 3.8+** and **pip** installed.  
- Install **virtualenv**:
```
pip install virtualenv
```

### 2. Clone the Repository
```
git clone https://github.com/MenakaGodakanda/quantum-circuit-visualizer.git
cd quantum-circuit-visualizer
```

### 3. Create and Activate Virtual Environment
```
python -m venv qcircuit
source qcircuit/bin/activate  # For Linux/Mac
qcircuit\Scripts\activate     # For Windows (PowerShell)
```

### 4. Install Dependencies
```
pip install qiskit flask matplotlib pylatexenc
```
- **Qiskit** (Quantum computing library)
- **Flask** (Web framework)
- **Matplotlib** (For circuit visualization)
- **pylatexenc** (Required by Qiskit for rendering)

### 5. Running the Application
```
python app.py
```
![Screenshot 2025-02-27 141458](https://github.com/user-attachments/assets/714202fe-9c62-4902-8d41-834ab53f896b)

- Then open `http://127.0.0.1:5000/` in your browser.
![Screenshot 2025-02-27 142506](https://github.com/user-attachments/assets/ac49acba-70f2-4dfa-82f6-e58294095fec)

## Example Quantum Circuits

### 1. Hadamard on Qubit 0
#### Input:
- Qubit 0: `H`

#### Circuit Output:
![Screenshot 2025-02-27 142000](https://github.com/user-attachments/assets/fce578f8-2bb2-40c4-9e8a-c8325e9ac8ae)

### 2. Hadamard & CNOT (Qubit 0 → Qubit 1)
#### Input:
- Qubit 0: `H`
- Qubit 1: `CNOT`

#### Circuit Output:
![Screenshot 2025-02-27 141150](https://github.com/user-attachments/assets/71695c7b-f419-4fb1-8f8f-ccccb0d43955)

### 3. Pauli Gates
#### Input:
- Qubit 0: `X`
- Qubit 1: `Z`
- Qubit 2: `Y`

#### Circuit Output:
![Screenshot 2025-02-27 141244](https://github.com/user-attachments/assets/dc29aa3a-8e17-4022-8b7c-5debec72ba09)

## File Structure
```
quantum-circuit-visualizer/
│── static/                 # Stores CSS, images, etc.
│── templates/              # HTML files (Flask templates)
│   ├── index.html
│── app.py                  # Flask web server
│── quantum_circuit.py       # Circuit generation logic
│── README.md                # Project documentation
```

## License
This project is licensed under the MIT License.
