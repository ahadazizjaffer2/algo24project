from flask import Flask, request, render_template, redirect, url_for, jsonify
import os
from algorithms.closest_pair import visualize_closest_pair
from algorithms.int_multiplication import visualize_integer_multiplication

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/algo/<algo_name>', methods=['GET', 'POST'])
def algo(algo_name):
    # Initialize steps and result
    steps = []
    result = ""
    
    if request.method == 'POST':
        # Save uploaded file
        file = request.files['input_file']
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            
            # Run the chosen algorithm
            if algo_name == 'closest_pair':
                steps, result = visualize_closest_pair(file_path)
                if not steps:  # Ensure steps is not empty or undefined
                    steps = ["No steps generated."]
                if not result:  # Ensure result is not empty or undefined
                    result = "No result generated."
                return render_template('closest_pair.html', steps=steps, result=result)
            elif algo_name == 'int_multiplication':
                steps, result = visualize_integer_multiplication(file_path)
                if not steps:
                    steps = ["No steps generated."]
                if not result:
                    result = "No result generated."
                return render_template('int_multiplication.html', steps=steps, result=result)
    else:
        # Handle GET request to show the file upload page
        if algo_name == 'closest_pair':
            return render_template('closest_pair.html', steps=steps, result=result)
        elif algo_name == 'int_multiplication':
            return render_template('int_multiplication.html', steps=steps, result=result)

    # If algo_name is not recognized, redirect to home
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=False)
