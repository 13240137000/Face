import face_recognition


def main():

    staffs = ['Jack', 'Wubo', 'Ding']

    for staff in staffs:
        print(staff)

    # jack_image = face_recognition.load_image_file("images/jack.jpg")
    # unknown_image = face_recognition.load_image_file("images/jack1.jpg")
    #
    # jack_encoding = face_recognition.face_encodings(jack_image)[0]
    # unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    #
    # results = face_recognition.compare_faces([jack_encoding], unknown_encoding)
    #
    # labels = ['Jack']
    #
    # print('results:' + str(results))
    #
    # for i in range(0, len(results)):
    #     if results[i]:
    #         print('The person is:' + labels[i])


if __name__ == "__main__":
    main()
