from CharacterDetection.test import BigLetterDetection
from CharacterClassification import test

cd = BigLetterDetection()
cd.detect('../CharacterDetection_Classification/story_image_2.jpg')

test.classify('../CharacterDetection_Classification/temp.jpg')