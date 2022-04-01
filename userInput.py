

'''
#name =input("Quel est votre nom?")
ville = input("dans quelle ville vis-tu?")

print(ville.find('e'))
print(ville.count('a'))
print(ville.upper() )
print(ville.capitalize())
print (ville.replace('ed', 'ARMEL') )
'''
print('\n')
##################################################
'''''
print('I have %d cats' %6)
print('I have %3d cats' %6)
print('I have %03d cats' %6)
print('I have %f cats' %6)
print('I have %.2f cats' %6)

print('\n')
################################################################

print('I have {0:d} cats'.format(6))
print('I have {0:3d} cats'.format(6))
print('I have {0:03d} cats'.format(6))
print('I have {0:f} cats'.format(6))
print('I have {0:.4f} cats'.format(6))
'''''
##############################################
import datetime

nextBirthday = datetime.datetime.strptime('8/19/1989', '%m/%d/%Y').date()
print(nextBirthday)

currentDate = datetime.date.today()
print(currentDate)

days = currentDate  -  nextBirthday

print('days untill nextBirthday :')
print(days.days)
print('\n')