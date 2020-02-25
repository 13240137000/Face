import face_recognition
import cv2


def main():

    img = face_recognition.load_image_file("images/5z.png")
    face_locations = face_recognition.face_locations(img)

    img = cv2.imread("images/5z.png")

    faces = len(face_locations)

    for i in range(0, faces):
        top = face_locations[i][0]
        right = face_locations[i][1]
        bottom = face_locations[i][2]
        left = face_locations[i][3]

        start = (left, top)
        end = (right, bottom)

        color = (55, 255, 155)
        thickness = 3
        cv2.rectangle(img, start, end, color, thickness)

    cv2.namedWindow("result")
    cv2.imshow("result", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

