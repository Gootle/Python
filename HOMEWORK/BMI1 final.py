def bmi_app():
	height = input('tall')
	weight = input('weight2')
	bmi_value = int(weight)/(int(height)/100)**2
	print('your BMI is {}'.format(round(bmi_value, 2)))
	if bmi_value < 18.5:
		print('eat more')
	elif bmi_value >= 18.5 and bmi_value <= 24:
		print('you are OK')
	else:
		print('you\'d better do some exercise')

bmi_app()
