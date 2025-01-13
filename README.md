# **Enhanced Hand Detection Program**  
### **YouTube Demonstration**  
   - Check out the live demonstration of this program on YouTube:  
👉 [Hand Tracking & Brightness Control System Demo](https://youtu.be/hZsAZHBGu8s?si=pbSjDZnhu7XyD5XA)

### **Overview**  
The **Enhanced Hand Detection Program** is an advanced real-time hand detection application built using Python, OpenCV, and Mediapipe. It detects left and right hands, identifies whether one or both hands are visible in the frame, and highlights hand landmarks using colored circles.  

The graphical interface is developed using Tkinter, making it user-friendly and interactive.

### **Features**  
1. **Real-Time Hand Detection:**  
   - Detects hands in real-time via the webcam.  
   - Distinguishes between left and right hands.  
   - Displays a "Both Hands" message if both hands are detected.  

2. **Hand Landmark Visualization:**  
   - Hand landmarks are marked with red circles on the video feed for better visualization.  

3. **Interactive GUI:**  
   - Start and stop the video stream with buttons.  
   - Displays the live video feed with detections directly in the GUI window.  

4. **Error Handling:**  
   - Ensures smooth program execution with built-in exception handling.  

### **How It Works**  
### **Hand Detection Logic**  
- Uses Mediapipe's `Hands` solution to detect and process hand landmarks.  
- For each detected hand:  
  - Identifies if the hand is "Left" or "Right" using the classification label.  
  - Displays the hand label on the appropriate side of the screen (left or right).  
- If both hands are visible:  
  - Displays "Both Hands" at the top of the video frame.  

### **GUI Design**  
- The interface is designed with Tkinter and includes:  
  - A **video feed area** for displaying processed frames.  
  - **Start Video** and **Stop Video** buttons for video control.  
  - A **footer label** acknowledging the developers.  

### **Video Feed Integration**  
- The program captures video from the default webcam (`cv2.VideoCapture(0)`), processes each frame to detect hands, and updates the video feed dynamically in the Tkinter window.

### **Usage Guide**  
1. **Starting the Program:**  
   - Run the Python script to launch the GUI.  

2. **Starting Video Detection:**  
   - Click the **Start Video** button to activate the webcam and begin real-time hand detection.  

3. **Stopping Video Detection:**  
   - Click the **Stop Video** button to stop the video feed.  

4. **Exiting the Program:**  
   - Close the program window or click the "X" button to exit the application.  
   - The program releases the webcam and closes all OpenCV windows upon exit.  

### **System Requirements**  
- A working webcam.  
- Python 3.x installed.  
- Compatible with Windows, macOS, or Linux.  

### **Code Summary**  
### **Key Functions:**  
1. **`process_frame()`**  
   - Captures a frame from the webcam.  
   - Processes the frame to detect hand landmarks using Mediapipe.  
   - Adds annotations like labels and landmark circles to the frame.  

2. **`update_frame()`**  
   - Continuously updates the video feed in the Tkinter window.  

3. **`start_video()` and `stop_video()`**  
   - Start and stop the video capture process, respectively.  

4. **`on_closing()`**  
   - Handles the program's exit by stopping video capture and releasing resources.  

### **Contribution**
Feel free to fork the repository, submit issues, or suggest improvements. Contributions are always welcome!

### **License**
This project is licensed under the MIT License. See the LICENSE file for details.

Developed by **A&J** as part of the Multimodal System.
