import random

def main():

	#while(1):
	#time.sleep(5)
    f = open('./text/datos.txt','r+')

    f.write('data1='+'\" ->'+str(random.randrange(0,1000)) +' m \"'+';'+'\n')
    f.write('data2='+'\" ->'+str(random.randrange(0,1000)) +' m \"'+';'+'\n' )
    f.write('data3='+'\" ->'+str(random.randrange(0,360)) +'\"'+';'+'\n')
    f.close()




if __name__ == '__main__':
    main()
