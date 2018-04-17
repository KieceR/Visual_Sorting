# <<< START OF KNOWN ERRORS >>>
'''
1 - A Traceback error will apears if the canvas is closed before the sorting finishes (Solution would be putting entrire main loop on 'try' and make a exception to print on console. I chose to let the program this way.);

'''
# <<< END OF KNOWN ERRORS >>>


# <<< START OF IMPORTING MODULES >>>
import time
import json
from tkinter import *
# <<< END OF IMPORTING MODULES >>>



# <<< START OF FUNCTION DEFINING >>>
def bubble_sort_visual(lista):
	for j in range(len(lista)):
		for i in range(len(lista)-1):
			if lista[i] > lista[i+1]:
				lista[i], lista[i+1] = lista[i+1], lista[i]
				canvas.delete("all")
				# >>> If the sorting is too fast, you can change this to make each step take the time passed <<<
				#time.sleep(0.01)
				for k in lista:
					canvas.create_line(k*5, (len(lista)*5), k*5, (len(lista)*5)-lista[k]*5, fill="white", width=3)
				animation.update()

def bubble_sort2_visual(lista):
	for j in range(len(lista)-1):
		for i in range(len(lista)-j-1):
			if lista[i] > lista[i+1]:
				lista[i], lista[i+1] = lista[i+1], lista[i]
				canvas.delete("all")
				# >>> If the sorting is too fast, you can change this to make each step take the time passed <<<
				#time.sleep(0.01)
				for k in lista:
					canvas.create_line(k*5, (len(lista)*5), k*5, (len(lista)*5)-lista[k]*5, fill="white", width=3)
				animation.update()

def bubble_sort3_visual(lista):
	for j in range(len(lista)-1):
		switch = False
		for i in range(len(lista)-j-1):
			if lista[i] > lista[i+1]:
				lista[i], lista[i+1] = lista[i+1], lista[i]
				switch = True
				canvas.delete("all")
				# >>> If the sorting is too fast, you can change this to make each step take the time passed <<<
				#time.sleep(0.01)
				for k in lista:
					canvas.create_line(k*5, (len(lista)*5), k*5, (len(lista)*5)-lista[k]*5, fill="white", width=3)
				animation.update()
		if not switch:
			break

def selection_sort_visual(lista):
	for j in range(len(lista)):
		low = j
		for i in range(j +1, len(lista)):
			if lista[i] < lista[low]:
				low = i
		if j != low:
			lista[j], lista[low] = lista[low], lista[j]
			canvas.delete("all")
			# >>> If the sorting is too fast, you can change this to make each step take the time passed <<<
			#time.sleep(0.05)
			for k in lista:
				canvas.create_line(k*5, (len(lista)*5), k*5, (len(lista)*5)-lista[k]*5, fill="white", width=3)
			animation.update()

def insertion_sort_visual(lista):
	for i in range(1, len(lista)):
		j = i
		while j > 0 and lista[j-1] > lista [j]:
			lista[j], lista[j-1] = lista[j-1], lista[j]
			j = j - 1
			canvas.delete("all")
			# >>> If the sorting is too fast, you can change this to make each step take the time passed <<<
			#time.sleep(0.05)
			for k in lista:
				canvas.create_line(k*5, (len(lista)*5), k*5, (len(lista)*5)-lista[k]*5, fill="white", width=3)
			animation.update()
# <<< END OF FUNCTION DEFINING >>>



# <<< START OF MAIN CODE >>>
# >>> Opens json file and pass as values to list <<<
lista_data = json.load(open("lista.json"))
# >>> Creates a new list with the same values as the lista_data <<<
lista = lista_data[:]


# <<< STAR OF THE MAIN LOOP >>>
while True:
	# >>> Starts a new tkinter GUI <<<
	animation = Tk()
	# >>> Creates a canvas widget <<<
	canvas = Canvas(animation, bg='black', height=(len(lista)*5), width=(len(lista)*5))
	# >>> Packs canvas to window <<<
	canvas.pack()
	animation.update()

	# >>> Prompts user to make a choice on the console (if choice is not an integer a exception is made and the user has to remake the choice) <<<
	while True:
		try:
			choice = int(input("Qual Algoritmo de Ordenação deseja visualizar?\nDigite 1 para BubbleSort_1;\nDigite 2 para BubbleSort_2;\nDigite 3 para BubbleSort_3;\nDigite 4 para SelectionSort;\nDigite 5 para InsertionSort;\nDigite qualquer outro número para sair.\nSua escolha: "))
		except:
			"Você deve digitar um Número!"
		break

	# >>> Given the choice the program will call for a specified function <<<
	if 		choice == 1:
		bubble_sort3_visual(lista)
	elif 	choice == 2:
		bubble_sort3_visual(lista)
	elif 	choice == 3:
		bubble_sort3_visual(lista)
	elif 	choice == 4:
		selection_sort_visual(lista)
	elif 	choice == 5:
		insertion_sort_visual(lista)
	# >>> If the number is different from the choices given, it will close the program (raising a system exit) <<<
	else:
		print("Quitting...")
		raise SystemExit(0)

	# >>> If the program runs as intended the canvas background will change color for some time and then the window will be destroyed and the list will reset <<<
	# >>> Configure the color change <<<
	canvas.configure(bg='green')
	# >>> Update the canvas to set up the color change <<<
	animation.update()
	# >>> Defines the time which the frame will stay the same <<<
	time.sleep(1)
	# >>> Removes the window from existence <<<
	animation.destroy()
	# >>> resets the list <<<
	lista = lista_data[:]

	# <<< START OF RETRYING LOOP >>>
	while True:
		again = input("Deseja visualizar outro algortimo? (Digite 'S' para sim ou 'N' para não): ").upper()
		if 		again == "SIM" or again == "S" or again == "'S'":
			break
		elif 	again == "NÃO" or again == "N" or again == "'N'" or again == "NAO":
			print("Quitting...")
			animation.destroy()
			raise SystemExit(0)
		else:
			print("Não entendi. Por favor tente novamente:")
	# <<< END OF RETRYING LOOP >>>

# >>> Makes sure the canvas widget stays on (not really useful given the code's structure) <<<
#animation.mainloop()

# >>> This part is a preventive shutdown, but is not really doing anything given the codes structure <<<
print("Program done!")
# >>> Raises a function to close the program <<<
raise SystemExit(0)
# <<< END OF MAIN CODE >>>
