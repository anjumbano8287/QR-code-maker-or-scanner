import cv2
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture(0)
    
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Decode qr code in the frame
    for obj in decode(frame):
        print(f"QR code date :{obj.data.decode("utf-8")}")  # print decode data


    # Display the video feed 
    cv2.imshow("QR code scanner",frame)
    # exit on pressin q

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # release the webcam and close windows
cap.release
cv2.destroyAllWindows    


    
  