#ssk 2023 -TechCree
from phew import logging, server, connect_to_wifi
from phew.template import render_template
from secrets import ssid, password
#import led
#import launcher

connect_to_wifi(ssid, password)

@server.route("/")
def index(request):
    return render_template("index.html", name="Galactic Unicorn", title="Webserver")

@server.route("/editor", ["POST",'GET'])
def login_form(request):
    print(request.method)
    if request.method == 'GET':
        return render_template("editor.html")
    
    if request.method == 'POST':    
        
            
        settext = request.form.get("settext", None)
        with open("settext_file.py", "w") as f:
            f.write("settext = '" + settext + "'")
            
        
        pass
        execfile("a_showtext.py") #for testing function
        return render_template('default.html', content = f"<h1>Gespeichert: , {settext}</h1>")


@server.catchall()
def my_catchall(request):
  return "No matching route", 404

server.run()
