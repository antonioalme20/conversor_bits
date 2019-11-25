import menu
import conversiones
print (""" 
  ____ 
 / ___|    ___    _ __   __   __   ___   _ __   ___    ___    _ __ 
 | |      / _ \  | '_ \  \ \ / /  / _ \ | '__| / __|  / _ \  | '__|
 | |___  | (_) | | | | |  \ V /  |  __/ | |    \__ \ | (_) | | |   
  \____|  \___/  |_| |_|   \_/    \___| |_|    |___/  \___/  |_| 

 @antonioalme20
""")
def main():
	#menu principal
	menu.menu1()
	eleccion1=str(input())
	if eleccion1=='1':
		#menu de bits
		menu.menu_bits()
		eleccion2=str(input())
		#Respectivas conversiones de bit->...
		if eleccion2=='1':
			conversiones.bit_to_byte()
		if eleccion2=='2':
			conversiones.bit_to_kilobyte()
		if eleccion2=='3':
			conversiones.bit_to_megabyte()
		if eleccion2=='4':
			conversiones.bit_to_gigabyte()
		if eleccion2=='5':
			conversiones.bit_to_terabyte()
		if eleccion2=='6':
			conversiones.bit_to_petabyte()
		
	if eleccion1 == '2':
		#menu de bytes
		menu.menu_bytes()
		eleccion2=str(input())
		#Respectivas conversiones de byte->...
		if eleccion2=='1':
			conversiones.byte_to_bit()
		if eleccion2=='2':
			conversiones.byte_to_kilobyte()
		if eleccion2=='3':
			conversiones.byte_to_megabyte()
		if eleccion2=='4':
			conversiones.byte_to_gigabyte()
		if eleccion2=='5':
			conversiones.byte_to_terabyte()
		if eleccion2=='6':
			conversiones.byte_to_petabyte()
		
	if eleccion1=='3':
		#menu de kilobytes
		menu.menu_kilobytes()
		eleccion2=str(input())
		#Respectivas conversiones de kilobyte->...
		if eleccion2=='1':
			conversiones.kilobyte_to_bit()
		if eleccion2=='2':
			conversiones.kilobyte_to_byte()
		if eleccion2=='3':
			conversiones.kilobyte_to_megabyte()
		if eleccion2=='4':
			conversiones.kilobyte_to_gigabyte()
		if eleccion2=='5':
			conversiones.kilobyte_to_terabyte()
		if eleccion2=='6':
			conversiones.kilobyte_to_petabyte()
	if eleccion1=='4':
		#menu de megabytes
		menu.menu_megabytes()
		eleccion2=str(input())
		#Respectivas conversiones de megabyte->...
		if eleccion2=='1':
			conversiones.megabyte_to_bit()
		if eleccion2=='2':
			conversiones.megabyte_to_byte()
		if eleccion2=='3':
			conversiones.megabyte_to_kilobyte()
		if eleccion2=='4':
			conversiones.megabyte_to_gigabyte()
		if eleccion2=='5':
			conversiones.megabyte_to_terabyte()
		if eleccion2=='6':
			conversiones.megabyte_to_petabyte()
	if eleccion1=='5':
		#menu de gigabytes
		menu.menu_gigabytes()
		eleccion2=str(input())
		#Respectivas conversiones de gigabyte->...
		if eleccion2=='1':
			conversiones.gigabyte_to_bit()
		if eleccion2=='2':
			conversiones.gigabyte_to_byte()
		if eleccion2=='3':
			conversiones.gigabyte_to_kilobyte()
		if eleccion2=='4':
			conversiones.gigabyte_to_megabyte()
		if eleccion2=='5':
			conversiones.gigabyte_to_terabyte()
		if eleccion2=='6':
			conversiones.gigabyte_to_petabyte()
	if eleccion1=='6':
		#menu de terabytes
		menu.menu_terabytes()
		eleccion2=str(input())
		#Respectivas conversiones de byte->...
		if eleccion2=='1':
			conversiones.terabyte_to_bit()
		if eleccion2=='2':
			conversiones.terabyte_to_byte()
		if eleccion2=='3':
			conversiones.terabyte_to_kilobyte()
		if eleccion2=='4':
			conversiones.terabyte_to_megabyte()
		if eleccion2=='5':
			conversiones.terabyte_to_gigabyte()
		if eleccion2=='6':
			conversiones.terabyte_to_petabyte()
	if eleccion1=='7':
		#menu de petabytes
		menu.menu_petabytes()
		eleccion2=str(input())
		#Respectivas conversiones de petabyte->...
		if eleccion2=='1':
			conversiones.petabyte_to_bit()
		if eleccion2=='2':
			conversiones.petabyte_to_byte()
		if eleccion2=='3':
			conversiones.petabyte_to_kilobyte()
		if eleccion2=='4':
			conversiones.petabyte_to_megabyte()
		if eleccion2=='5':
			conversiones.petabyte_to_gigabyte()
		if eleccion2=='6':
			conversiones.petabyte_to_terabyte()
#Bucle para repeticion de todo
main()

def bucle():
	print("\nVolver? Si/No")
	eleccionvolver=input()
	if eleccionvolver == 'Si':
		main()
	if eleccionvolver == 'No':
		sys.exit()
	if eleccionvolver == 'si':
		main()
	if eleccionvolver == 'no':
		sys.exit()
	if eleccionvolver == 'SI':
		main()
	if eleccionvolver == 'NO':
		sys.exit()
i=1
while i<10:
	bucle()
