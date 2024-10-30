import cv2
import mediapipe as mp

# Inicializar o Mediapipe Hands
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Iniciar a captura de vídeo
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Não foi possível ler o frame da câmera.")
            break

        # Espelhar a imagem para efeito de selfie e converter de BGR para RGB
        image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

        # Melhorar o desempenho marcando a imagem como não gravável
        image.flags.writeable = False
        results = hands.process(image)

        # Desenhar as anotações da mão na imagem
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Desenhar os pontos de referência da mão
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Obter as coordenadas das pontas dos dedos e polegar
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

                # Obter as coordenadas das articulações MCP dos dedos
                index_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
                middle_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
                ring_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y
                pinky_mcp_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y

                # Verificar se os dedos (exceto o polegar) estão dobrados
                index_finger_down = index_tip.y > index_mcp_y
                middle_finger_down = middle_tip.y > middle_mcp_y
                ring_finger_down = ring_tip.y > ring_mcp_y
                pinky_finger_down = pinky_tip.y > pinky_mcp_y

                # Verificar a direção do polegar
                thumb_up = thumb_tip.y < thumb_ip.y
                thumb_down = thumb_tip.y > thumb_ip.y

                # Verificar se todos os dedos estão dobrados (exceto o polegar)
                fingers_down = index_finger_down and middle_finger_down and ring_finger_down and pinky_finger_down

                if fingers_down:
                    if thumb_up:
                        cv2.putText(image, 'Like!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                                    1, (0, 255, 0), 2, cv2.LINE_AA)
                        print("Like!")
                    elif thumb_down:
                        cv2.putText(image, 'Deslike!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                                    1, (0, 0, 255), 2, cv2.LINE_AA)
                        print("Deslike!")
                else:
                    cv2.putText(image, 'Mão detectada', (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (255, 255, 0), 2, cv2.LINE_AA)

        # Mostrar a imagem resultante
        cv2.imshow('Detector de Like e Deslike', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()

