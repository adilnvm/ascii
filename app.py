# app.py
from flask import Flask, render_template, request
from flask import send_file
import pywhatkit as kt

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "imageInput" in request.files:
        image = request.files["imageInput"]
        
        # Save the uploaded image
        image_path = "uploaded_image.jpg"
        image.save(image_path)

        # Convert the image to ASCII art
        ascii_art_path = "ascii_art.txt"
        kt.image_to_ascii_art(image_path, ascii_art_path)
        print(f"ASCII art file created at: {ascii_art_path}")

        

        return render_template("result.html", image_path=image_path, ascii_art_path=ascii_art_path)
    else:
        return "No image received."

@app.route("/download_ascii")
def download_ascii():
    ascii_art_path = "ascii_art.txt"
    return send_file(ascii_art_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, port=8080)

app = Flask(__name__, static_url_path='/static')


print("hi")
