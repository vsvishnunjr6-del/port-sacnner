from flask import Flask, render_template, request
import socket

app = Flask(__name__)

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except:
        return False

@app.route("/", methods=["GET", "POST"])
def index():
    open_ports = []
    target = ""

    if request.method == "POST":
        target = request.form["target"]
        start_port = int(request.form.get("start_port", 20))
        end_port = int(request.form.get("end_port", 1024))

        for port in range(start_port, end_port + 1):
            if scan_port(target, port):
                open_ports.append(port)

    return render_template("index.html", open_ports=open_ports, target=target)

if __name__ == "__main__":
    app.run(debug=True)