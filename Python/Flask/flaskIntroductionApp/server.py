from flask_app import app

from flask_app.controllers import users, auth

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True,host="0.0.0.0", port=8000)    # R

