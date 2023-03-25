
from PIL import Image
from numpy import asarray
from mtcnn.mtcnn import MTCNN
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
import os
import cv2

def extract_face(filename, required_size=(224, 224)):
	image = cv2.imread(filename)
	pixels = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
	detector = MTCNN()
	results = detector.detect_faces(pixels)
	if results == []:
		print("Not able to detect any face")
		exit()
	x1, y1, width, height = results[0]['box']
	x2, y2 = x1 + width, y1 + height
	face = pixels[y1:y2, x1:x2]
	image = Image.fromarray(face)
	image = image.resize(required_size)
	face_array = asarray(image)
	return face_array	


def get_embeddings(filenames):
	faces = [extract_face(f) for f in filenames]
	samples = asarray(faces, 'float32')
	samples = preprocess_input(samples, version=2)
	model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')
	yhat = model.predict(samples)
		
	return yhat
    	

if __name__ == '__main__':
        filenames = []
        for x in os.listdir():
            if x.endswith(".jpg"):
                filenames.append(x)
        embeddings = get_embeddings(filenames)
        for image_url, embedds in zip(filenames, embeddings):
            print(embedds)





