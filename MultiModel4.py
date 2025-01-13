import cv2
import mediapipe as mp
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from google.protobuf.json_format import MessageToDict
import threading

mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.85,
    min_tracking_confidence=0.85,
    max_num_hands=2,
)

cap = cv2.VideoCapture(0)


def process_frame():
    success, img = cap.read()
    if not success:
        return None

    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        if len(results.multi_hand_landmarks) == 2:
            cv2.putText(
                img,
                "Both Hands",
                (250, 50),
                cv2.FONT_HERSHEY_COMPLEX,
                0.9,
                (0, 255, 0),
                2,
            )
        else:
            for hand_landmarks, hand_handedness in zip(
                results.multi_hand_landmarks, results.multi_handedness
            ):
                label = MessageToDict(hand_handedness)["classification"][0]["label"]
                if label == "Left":
                    cv2.putText(
                        img,
                        label + " Hand",
                        (20, 50),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.9,
                        (0, 255, 0),
                        2,
                    )
                elif label == "Right":
                    cv2.putText(
                        img,
                        label + " Hand",
                        (460, 50),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.9,
                        (0, 255, 0),
                        2,
                    )

                for landmark in hand_landmarks.landmark:
                    x = int(landmark.x * img.shape[1])
                    y = int(landmark.y * img.shape[0])
                    cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    return img


def update_frame():
    if video_on:
        img = process_frame()
        if img is not None:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img = ImageTk.PhotoImage(img)
            lbl_video.imgtk = img
            lbl_video.configure(image=img)
        root.after(10, update_frame)


def start_video():
    global video_on, cap
    if not cap.isOpened():
        cap = cv2.VideoCapture(0)
    video_on = True
    update_frame()


def stop_video():
    global video_on
    video_on = False
    lbl_video.configure(image="")
    cap.release()


def on_closing():
    stop_video()
    cv2.destroyAllWindows()
    root.destroy()


root = tk.Tk()
root.title("Enhanced Hand Detection Program Developed By A&J")
root.geometry("1920x1080")
root.configure(bg="#343f71")

video_on = False

title_label = tk.Label(
    root,
    text="Enhanced Hand Detection",
    font=("Arial", 30, "bold"),
    bg="#343f71",
    fg="#ecf0f1",
)
title_label.pack(pady=20)

lbl_video = tk.Label(root, bg="#343f71")
lbl_video.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)

start_button = tk.Button(
    root,
    text="Start Video",
    command=start_video,
    font=("Arial", 14),
    bg="#009500",
    fg="#ffffff",
    activebackground="#3498db",
    activeforeground="#000000",
)
start_button.pack(side=tk.LEFT, padx=20, pady=50)

stop_button = tk.Button(
    root,
    text="Stop Video",
    command=stop_video,
    font=("Arial", 14),
    bg="#e74c3c",
    fg="#ffffff",
    activebackground="#3498db",
    activeforeground="#000000",
)
stop_button.pack(side=tk.RIGHT, padx=20, pady=50)

root.protocol("WM_DELETE_WINDOW", on_closing)

footer_label = tk.Label(
    root, text="Developed By A&J", font=("Arial", 15), bg="#343f71", fg="#ffea00"
)
footer_label.pack(side="bottom", pady=10)

root.mainloop()
