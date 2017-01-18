import cv2
import numpy
import LDAPUser

# Get user supplied values
def faceDetection(image):
    #imagePath = "foto1.jpg"
    cascPathFace = "haarcascade_frontalface_default.xml"
    cascPathEyes = "haarcascade_eye.xml"
    cascPathGlasses = "haarcascade_eye_tree_eyeglasses.xml"
    
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPathFace)
    eyesCascade = cv2.CascadeClassifier(cascPathEyes)
    
    # Read the image
    #image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    people=numpy.array(["Radin Stefano","Gombani Sara"])
    
    path_faces="D:\\foto_facerec\\"
    im1=cv2.imread(path_faces+"sr\\1.jpg",cv2.IMREAD_GRAYSCALE)
    im2=cv2.imread(path_faces+"sr\\2.jpg",cv2.IMREAD_GRAYSCALE)
    im3=cv2.imread(path_faces+"sr\\3.jpg",cv2.IMREAD_GRAYSCALE)
    im4=cv2.imread(path_faces+"sr\\4.jpg",cv2.IMREAD_GRAYSCALE)
    im5=cv2.imread(path_faces+"sr\\5.jpg",cv2.IMREAD_GRAYSCALE)
    im6=cv2.imread(path_faces+"sg\\1.jpg",cv2.IMREAD_GRAYSCALE)
    im7=cv2.imread(path_faces+"sg\\2.jpg",cv2.IMREAD_GRAYSCALE)
    im8=cv2.imread(path_faces+"sg\\3.jpg",cv2.IMREAD_GRAYSCALE)
    im9=cv2.imread(path_faces+"sg\\4.jpg",cv2.IMREAD_GRAYSCALE)
    im10=cv2.imread(path_faces+"sg\\5.jpg",cv2.IMREAD_GRAYSCALE)
    images=numpy.array([im1,im2,im3,im4,im5,im6,im7,im8,im9,im10])
    labels=numpy.array([0,0,0,0,0,1,1,1,1,1])
    
    model = cv2.createEigenFaceRecognizer()
    model.train(images,labels)   
    
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(60, 60),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    
    print("Found {0} faces!".format(len(faces)))
    
    # Draw a rectangle around the faces
    i=1
    for (x, y, w, h) in faces:
        p_label=-1
        [p_label, p_confidence] = model.predict(cv2.resize(gray[y: y + h, x: x + w],(100,100)))
        cv2.rectangle(image, (x, y), (x+w, y+h), (23, 32, 193), 2)
        cv2.putText(image,str(i) + " - " + people[p_label],(x, y-5), cv2.FONT_HERSHEY_PLAIN, 1, (23, 32, 193))
        [ruolo,dept]=LDAPUser.cercaLDAP(people[p_label])
        cv2.putText(image,ruolo,(x+5, y+15), cv2.FONT_HERSHEY_PLAIN, 1, (23, 32, 193))
        cv2.putText(image,dept,(x+5, y+30), cv2.FONT_HERSHEY_PLAIN, 1, (23, 32, 193))
        #cv2.putText(image,str(i)+" - "+str(p_confidence),(x, y-5), cv2.FONT_HERSHEY_PLAIN, 1, (23, 32, 193))
        eyes = eyesCascade.detectMultiScale(
            gray[y:y+h,x:x+w],
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(10,10),
            flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        for (ex,ey,ew,eh) in eyes:
            #cv2.rectangle(image, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (23, 32, 193), 2)
            cv2.line(image,(x+ex+ew/2-5,y+ey+eh/2),(x+ex+ew/2+5,y+ey+eh/2),(23, 32, 193))
            cv2.line(image,(x+ex+ew/2,y+ey+eh/2-5),(x+ex+ew/2,y+ey+eh/2+5),(23, 32, 193))
        i+=1
        
    cv2.imshow("Found faces", image)
    cv2.waitKey(0)
