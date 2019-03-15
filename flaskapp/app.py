from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# result = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/points', methods=['GET', 'POST'])
def points():
    if request.method == 'POST':
        result = request.form
        # return redirect(url_for('points'))
        return render_template('p5.html', result=result)
    # else:
    #     return render_template('p5.html', result=result)

if __name__ == '__main__':
    app.run()