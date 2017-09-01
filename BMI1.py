Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def bmi_app()
SyntaxError: invalid syntax
>>> def bmi_app():
	height = input('tall')
	weight = input('weight2')
	bmi_value = int(weight)/(int(height)/100)**2
	print(bmi_value)

	
>>> bmi_app
<function bmi_app at 0x02A96270>
>>> bmi_app()
tall177
weight262
19.789970953429727
>>> def bmi_app():
	height = input('tall')
	weight = input('weight2')
	bmi_value = int(weight)/(int(height)/100)**2
	print('your BMI is {}'.format(round(bmi_value, 2)))
	if bmi_valume < 18.5
	
SyntaxError: invalid syntax
>>> def bmi_app():
	height = input('tall')
	weight = input('weight2')
	bmi_value = int(weight)/(int(height)/100)**2
	print('your BMI is {}'.format(round(bmi_value, 2)))
	if  < 18.5:
		print('eat more')
	elif bmi_valume >=18.5 and bmi_valume<=24:
		
SyntaxError: invalid syntax
>>> def bmi_app():
	height = input('tall')
	weight = input('weight2')
	bmi_value = int(weight)/(int(height)/100)**2
	print('your BMI is {}'.format(round(bmi_value, 2)))
	if  bmi_valume < 18.5:
		print('eat more')
	elif bmi_valume >=18.5 and bmi_valume<=24:
		print('you are OK')
	else:
		print('you\d better do some exercise')

		
>>> bmi_app()
tall180
weight299
your BMI is 30.56
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    bmi_app()
  File "<pyshell#18>", line 6, in bmi_app
    if  bmi_valume < 18.5:
NameError: name 'bmi_valume' is not defined
>>> def bmi_app():
	height = input('tall')
	weight = input('weight2')
	bmi_value = int(weight)/(int(height)/100)**2
	print('your BMI is {}'.format(round(bmi_value, 2)))
	if bmi_valume < 18.5:
		print('eat more')
	elif bmi_valume >= 18.5 and bmi_valume <= 24:
		print('you are OK')
	else:
		print('you\d better do some exercise')

		
>>> bmi_app()
tall180
weight299
your BMI is 30.56
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    bmi_app()
  File "<pyshell#21>", line 6, in bmi_app
    if bmi_valume < 18.5:
NameError: name 'bmi_valume' is not defined
>>> def bmi_app():
	height = input('tall')
	weight = input('weight2')
	bmi_value = int(weight)/(int(height)/100)**2
	print('your BMI is {}'.format(round(bmi_value, 2)))
	if bmi_valume < 18.5:
		print('eat more')
	elif bmi_valume >= 18.5 and bmi_valume <= 24:
		print('you are OK')
	else:
		print('you\d better do some exercise')
