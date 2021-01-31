from __future__ import print_function
from google.cloud import vision

url_input = input("Please enter a URL of the picture you want to check: ")
image_uri = url_input

client = vision.ImageAnnotatorClient()
image = vision.Image()
image.source.image_uri = image_uri

response = client.label_detection(image=image, max_results=50)

print ("Response: ")
#print('Labels (and confidence score):')
#print('=' * 30)
have_mask = None
for label in response.label_annotations:
#    print(label.description, '(%.2f%%)' % (label.score*100.))
    if label.description == 'Personal protective equipment':
        have_mask = True
    elif label.description == "Mask":
        have_mask = True
print (have_mask)
if have_mask == False:
    print ("Please put a mask on you dumb dumb")
elif have_mask == True:
    print ("Thank you for having a mask")
else:
    print ("Unsure, please make sure yout uri is correct")