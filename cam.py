import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh()

two_img = cv2.imread("pics/two.jpg")
tongue_img = cv2.imread("pics/tongue.jpg")
ok_img = cv2.imread("pics/ok.jpg")
index_img = cv2.imread("pics/index.jpg")
bad_img = cv2.imread("pics/bad.jpg")

panel_w, panel_h = 200, 200

current_gesture = None
gesture_counter = 0
THRESHOLD = 2

def index_middle(results):
    if not results.multi_hand_landmarks:
        return False
    for hand_landmarks in results.multi_hand_landmarks:
        lm = hand_landmarks.landmark
        index_up   = lm[8].y  < lm[6].y
        middle_up  = lm[12].y < lm[10].y
        ring_down  = lm[16].y > lm[14].y
        pinky_down = lm[20].y > lm[18].y
        if index_up and middle_up and ring_down and pinky_down:
            return True
    return False

def tongue_out(face_results):
    if not face_results.multi_face_landmarks:
        return False
    for face_landmarks in face_results.multi_face_landmarks:
            top_lip = face_landmarks.landmark[13]
            bottom_lip = face_landmarks.landmark[14]
            if bottom_lip.y - top_lip.y > 0.04 and bottom_lip.y - top_lip.y < 0.1:
                return True
    return False

def thumbs_up(results):
    if not results.multi_hand_landmarks:
        return False
    for hand_landmarks in results.multi_hand_landmarks:
        lm = hand_landmarks.landmark
        thumb_up    = lm[4].y < lm[3].y
        above_wrist = lm[4].y < lm[0].y
        index_down  = lm[8].y  > lm[5].y
        middle_down = lm[12].y > lm[9].y
        ring_down   = lm[16].y > lm[13].y
        pinky_down  = lm[20].y > lm[17].y
        if thumb_up and above_wrist and index_down and middle_down and ring_down and pinky_down:
            return True
    return False

def thumbs_down(results):
    if not results.multi_hand_landmarks:
        return False
    for hand_landmarks in results.multi_hand_landmarks:
        lm = hand_landmarks.landmark
        thumb_down  = lm[4].y > lm[2].y
        below_wrist = lm[4].y > lm[0].y
        index_down  = lm[8].y  > lm[5].y
        middle_down = lm[12].y > lm[9].y
        ring_down   = lm[16].y > lm[13].y
        pinky_down  = lm[20].y > lm[17].y
        if thumb_down and below_wrist and index_down and middle_down and ring_down and pinky_down:
            return True
    return False

def index_up(results):
    if not results.multi_hand_landmarks:
        return False
    for hand_landmarks in results.multi_hand_landmarks:
        lm = hand_landmarks.landmark
        index_up   = lm[8].y  < lm[6].y
        middle_down  = lm[12].y > lm[10].y
        ring_down  = lm[16].y > lm[14].y
        pinky_down = lm[20].y > lm[18].y
        if index_up and middle_down and ring_down and pinky_down:
            return True
    return False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    hand_results = hands.process(rgb)
    face_results = face_mesh.process(rgb)

    if thumbs_down(hand_results):
            raw_gesture = "bad"
    elif thumbs_up(hand_results):
        raw_gesture = "thumb"
    elif index_middle(hand_results):
        raw_gesture = "two"
    elif index_up(hand_results):
        raw_gesture = "index"
    elif tongue_out(face_results):
        raw_gesture = "tongue"
    else:
        raw_gesture = None

    if raw_gesture == current_gesture:
        gesture_counter += 1
    else:
        gesture_counter = 0
        current_gesture = raw_gesture

    confirmed_gesture = current_gesture if gesture_counter >= THRESHOLD else None

    x = frame.shape[1] - panel_w - 10
    y = 10

    if confirmed_gesture == "two" and two_img is not None:
        panel = cv2.resize(two_img, (panel_w, panel_h))
    elif confirmed_gesture == "tongue" and tongue_img is not None:
        panel = cv2.resize(tongue_img, (panel_w, panel_h))
    elif confirmed_gesture == "thumb" and ok_img is not None:
        panel = cv2.resize(ok_img, (panel_w, panel_h))
    elif confirmed_gesture == "index" and index_img is not None:
        panel = cv2.resize(index_img, (panel_w, panel_h))
    elif confirmed_gesture == "bad" and bad_img is not None:
        panel = cv2.resize(bad_img, (panel_w, panel_h))
    else:
        panel = np.ones((panel_h, panel_w, 3), dtype='uint8') * 50
        cv2.putText(panel, "no reaction", (20, panel_h // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    frame[y:y+panel_h, x:x+panel_w] = panel
    cv2.imshow("gesture cam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
