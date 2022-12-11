from threading import Thread
def karthik():
    import time

    import cv2
    import mediapipe as mp
    import numpy as np
    from pathlib import Path
    from shutil import rmtree

    for path in Path(r"C:\Users\saika\PycharmProjects\jaiganesh\images").glob("**/*"):
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            rmtree(path)

    count = 0
    i = 0
    while (i < 20):
        mp_face_mesh = mp.solutions.face_mesh
        face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
        cap = cv2.VideoCapture(0)
        x, y, w, h = 0, 0, 175, 75
        while cap.isOpened():
            success, image = cap.read()
            time.sleep(10)
            # Flip the image horizontally for a later selfie-view display
            # Also convert the color space from BGR to RGB
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

            # To improve performance
            image.flags.writeable = False

            # Get the result
            results = face_mesh.process(image)

            # To improve performance
            image.flags.writeable = True

            # Convert the color space from RGB to BGR
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            img_h, img_w, img_c = image.shape
            face_3d = []
            face_2d = []

            if results.multi_face_landmarks:
                for face_landmarks in results.multi_face_landmarks:
                    for idx, lm in enumerate(face_landmarks.landmark):
                        if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
                            if idx == 1:
                                nose_2d = (lm.x * img_w, lm.y * img_h)
                                nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 8000)

                            x, y = int(lm.x * img_w), int(lm.y * img_h)

                            # Get the 2D Coordinates
                            face_2d.append([x, y])

                            # Get the 3D Coordinates
                            face_3d.append([x, y, lm.z])

                            # Convert it to the NumPy array
                    face_2d = np.array(face_2d, dtype=np.float64)

                    # Convert it to the NumPy array
                    face_3d = np.array(face_3d, dtype=np.float64)

                    # The camera matrix
                    focal_length = 1 * img_w

                    cam_matrix = np.array([[focal_length, 0, img_h / 2],
                                           [0, focal_length, img_w / 2],
                                           [0, 0, 1]])

                    # The Distance Matrix
                    dist_matrix = np.zeros((4, 1), dtype=np.float64)

                    # Solve PnP
                    success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

                    # Get rotational matrix
                    rmat, jac = cv2.Rodrigues(rot_vec)

                    # Get angles
                    angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)

                    # Get the y rotation degree
                    x = angles[0] * 360
                    y = angles[1] * 360

                    # print(y)

                    # See where the user's head tilting
                    if y < -10:
                        text = "FORWARD,"
                    elif y > 10:
                        text = "FORWARD."
                    elif x < -10:
                        text = "FORWARD,."
                    else:
                        text = "FORWARD"

                    # Display the nose direction
                    nose_3d_projection, jacobian = cv2.projectPoints(nose_3d, rot_vec, trans_vec, cam_matrix,
                                                                     dist_matrix)

                    p1 = (int(nose_2d[0]), int(nose_2d[1]))
                    p2 = (int(nose_3d_projection[0][0][0]), int(nose_3d_projection[0][0][1]))

                    cv2.line(image, p1, p2, (255, 0, 0), 2)
                    x, y, w, h = 0, 0, 1400, 1400
                    cv2.rectangle(image, (x, x), (x + w, y + h), (0, 0, 0), -1)
                    position = ((int)(image.shape[1] / 2 - 268 / 2), (int)(image.shape[0] / 2 - 36 / 2))
                    # Add the text on the image
                    cv2.putText(
                        image,  # numpy array on which text is written
                        text,  # text
                        (40, 60),  # position at which writing has to start
                        cv2.FONT_HERSHEY_SIMPLEX,  # font family
                        3,  # font size
                        (255, 255, 255, 255),  # font color
                        6)  # font stroke

            cv2.namedWindow("detect", cv2.WINDOW_NORMAL)
            cv2.moveWindow('detect', 300, 300)
            cv2.resizeWindow("detect", 300, 700)
            cv2.imshow('detect', image)
            if cv2.waitKey(1):
                cv2.imwrite('C:/Users/saika/PycharmProjects/jaiganesh/images/result%d.jpg' % count, image)
                break
        count += 1
        i += 1

    cap.release()

y6 = Thread(target=karthik)
y6.start()