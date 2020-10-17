import socket
import tkinter as tk
import keyboard

hosting = False

defport = 80

defhtml = """<html>
<head>
<style>
body {
   font-family: !!FONT!!;
}
</style>
<title>!!TITLE!!</title>
</head>
<body>
!!BODY!!
</body>
</html>"""

def compilecode(title, body, font="Arial"):
    print("Compiling...")
    return bytes(defhtml.replace("!!TITLE!!", title).replace("!!BODY!!", body).replace("!!FONT!!", font), "UTF-8")

html = compilecode("AC88 Web",
                   "<h1>AC88 Web</h1><h2>Error 204</h2><p>This site has been started without any code. If you are the developer please check your website editor.</p>")

def run(port, html, onlylh=False):
    if not type(html)==bytes:
        print("Expected html in b'' not ''")
        return
    sock = socket.socket()
    sock.bind(('', port))
    print("Waiting for client...")
    sock.listen(5)
    client, address = sock.accept()
    print("Incoming:", address)
    if not address[0]=="127.0.0.1" and onlylh:
        print("Aborting run. Non-localhost user requested.")
        return
    print(client.recv(1024))
    print()
    client.send(b'HTTP/1.0 200 OK\r\n')
    client.send(b"Content-Type: text/html\r\n\r\n")
    client.send(html)
    client.close()
    print("Answering ...")
    print("Finished.")
    sock.close()

def aborthost(e=""):
    print("Aborting host...")
    global hosting
    keyboard.unhook_all()
    hosting = False

def host(port, html, ek="h"):
    print("Hosting...")
    global hosting
    hosting = True
    if not ek==None:
        keyboard.on_press_key("h", aborthost)
    while hosting:
        run(port, html)
