import face_recognition


def landmarks():

    image = face_recognition.load_image_file("images/jack.jpg")

    face_landmarks_list = face_recognition.face_landmarks(image, face_locations=None, model="small")

    print(face_landmarks_list)


if __name__ == "__main__":
    landmarks()
