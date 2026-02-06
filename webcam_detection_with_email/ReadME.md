# Motion Detection Security Camera with Email Alerts

This project uses **OpenCV** to detect motion through a webcam, automatically captures images when movement is detected, and sends an **email alert with an image attachment**. After sending the email, the saved images are cleaned up to save storage.

---

## Features

* Real-time motion detection using webcam
* Draws bounding boxes around detected movement
* Saves images when motion is detected
* Sends email alert with captured image
* Cleans up stored images automatically
* Uses threading to avoid blocking the video feed

---

## How It Works

1. Captures video from the webcam
2. Converts frames to grayscale and applies Gaussian blur
3. Compares current frame with the first frame to detect changes
4. Uses thresholding to isolate motion areas
5. Detects contours and filters out small movements
6. Saves images when motion is detected
7. Sends an email when motion stops
8. Deletes stored images after sending the email

---

## Requirements

Install the required dependencies:

```bash
pip install opencv-python
```

(Standard Python libraries used: `os`, `time`, `glob`, `threading`, `smtplib`, `email`)

---

## Folder Structure

```
project/
│
├── main.py
├── mail.py
├── images/
│   └── (captured images saved here)
└── README.md
```

⚠️ Make sure the `images` folder exists before running the program.

---

## Email Setup

In `mail.py`, configure your email credentials:

```python
SENDER = "your_email@gmail.com"
PASSWORD = "your_app_password"
RECEIVER = "receiver_email@gmail.com"
```

> Use a **Gmail App Password**, not your normal Gmail password.

---

## Running the Program

```bash
python main.py
```

* Press **`q`** to quit the application.
* When motion is detected, a green rectangle appears around the moving object.
* An email is sent once motion stops.

---

## Threshold Window (Debug)

The **Threshold window** shows a black-and-white view of detected motion:

* White = motion detected
* Black = no motion

This window helps tune sensitivity and can be removed once debugging is complete.

---

## Notes

* Adjust contour area (`10000`) to control motion sensitivity
* Adjust threshold value (`65`) to handle lighting conditions
* Designed for single-camera use

---

## Future Improvements

* Reduce false positives
* Add video recording
* Support multiple cameras
* Add cooldown timer for email alerts

---

## License

This project is for learning and personal use.

---


