Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = (int(input('Price of the meal:')))
b = (int(input('Percentage on tip:')))
print('Tips:', (b*(a/100)))
print('Total:', a+(b*(a/100)))
