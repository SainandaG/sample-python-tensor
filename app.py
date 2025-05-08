from flask import Flask, render_template, request, redirect, url_for
import os
import cv2

app = Flask(__name__)
UPLOAD_FOLDER = "static"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        if file:
            img_path = os.path.join(app.config["UPLOAD_FOLDER"], "uploaded_image.jpg")
            file.save(img_path)

            # Convert the image to grayscale using OpenCV
            img = cv2.imread(img_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray_path = os.path.join(app.config["UPLOAD_FOLDER"], "gray_image.jpg")
            cv2.imwrite(gray_path, gray)

            # Return the path of the processed image to be shown
            return render_template("index.html", output_image="gray_image.jpg")
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
