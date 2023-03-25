
from PIL import Image
from numpy import asarray
from mtcnn.mtcnn import MTCNN
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
import os
import cv2

def extract_face(image, required_size=(224, 224)):
	pixels = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
	detector = MTCNN()
	results = detector.detect_faces(pixels)
	if results:
		x1, y1, width, height = results[0]['box']
		x2, y2 = x1 + width, y1 + height
		face = pixels[y1:y2, x1:x2]
		image = Image.fromarray(face)
		image = image.resize(required_size)
		face_array = asarray(image)
		return face_array
	return []


def get_embeddings(filenames):
	faces = [extract_face(f) for f in filenames]
	if faces != [[]]:
		samples = asarray(faces, 'float32')
		samples = preprocess_input(samples, version=2)
		model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')
		yhat = model.predict(samples)
		return yhat
	return [[]]
    	





