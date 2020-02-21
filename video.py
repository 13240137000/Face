import face_recognition
import cv2 as cv


def main():

    capture = cv.VideoCapture(0)

    jack_img = face_recognition.load_image_file("images/jack.jpg")
    jack_face_encoding = face_recognition.face_encodings(jack_img)[0]

    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:

        ret, frame = capture.read()

        small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)

        if process_this_frame:

            face_locations = face_recognition.face_locations(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                match = face_recognition.compare_faces([jack_face_encoding], face_encoding)

                if match[0]:
                    name = "Jack."
                else:
                    name = "unknown"

                face_names.append(name)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):

            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), 2)

            font = cv.FONT_HERSHEY_DUPLEX

            cv.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv.imshow('Video', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
