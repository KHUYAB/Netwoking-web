"""
NetConnect Solutions - Flask Application
A modern static website for a networking solutions company
"""
from flask import Flask, render_template

# Initialize Flask application
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html', title='Home')

# Services route
@app.route('/services')
def services():
    """Render the services page"""
    return render_template('services.html', title='Services')

# About route
@app.route('/about')
def about():
    """Render the about us page"""
    return render_template('about.html', title='About Us')

# Contact route
@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template('contact.html', title='Contact')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html', title='Page Not Found'), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    return render_template('500.html', title='Server Error'), 500

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)