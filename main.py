from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def appPage():
    return render_template('app.html', 
        tabTitle = 'What\'s playing?',
        trackTitle = 'Track Title', 
        albumTitle = 'Album Title')

@app.route('/settings')
def settingsPage():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run()