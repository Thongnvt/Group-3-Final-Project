# Group-3-Final-Project
Final project of DAT301m
In this project, I use VietOCR, a famous model in Vietnamese language detection. I have provided all the weight than i trained for this project

About the project, I used 2 seperate model, one for detection and one is for recognition.

About detection, I used EAST ( Efficient and Accuracy Scene Text), a model use for detect character, mostly used in document or character with no curve or abnormal shape, with the time of proscessing very fast.

For recognition, I used VietOCR, as I said above, I have trained for 10 hour, using pretrained weight to support, with the accuracy in seq exceed 0.86%, and accuracy in each character exceed 0.92 to 0.95  percent.

And to make the result better, I have written a spell checker module, using pyvi and custom_spellchecker, for a better performance.

I hope it will help.
