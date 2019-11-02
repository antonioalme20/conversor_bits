print("""   ____                                                            
  / ___|   ___    _ __   __   __   ___   _ __   ___    ___    _ __ 
 | |      / _ \  | '_ \  \ \ / /  / _ \ | '__| / __|  / _ \  | '__|
 | |___  | (_) | | | | |  \ V /  |  __/ | |    \__ \ | (_) | | |   
  \____|  \___/  |_| |_|   \_/    \___| |_|    |___/  \___/  |_|   
                                                                   """)
import sys
print("@antonioalme_20")
def main():
	print("\n1)Bit->...\n2)Byte->...\n3)Kilobyte->...\n4)Megabyte->...\n5)Gigabyte->...\n6)Terabyte->...\n7)Petabyte->...")
	eleccion_1=input()
	if eleccion_1== '1':
		print("\n1)Bit->Byte\n2)Bit->Kilobyte\n3)Bit->Megabyte\n4)Bit->Gigabyte\n5)Bit->Terabyte\n6)Bit->Petabyte")
		eleccion_2=input()
		if eleccion_2 == '1':
			def bit_to_byte():
				print("\nPon bits:")
				num_bits=float(input())
				print(num_bits/8)
			print("\nResultado:")
			bit_to_byte()
		if eleccion_2=='2':
			def bit_to_kilobyte():
				print("\nPon bits:")
				num_bits=float(input())
				rint((num_bits/8)/1024)
			print("\nResultado:")
			bit_to_kilobyte()
		if eleccion_2=='3':
			def bit_to_megabyte():
				print("\nPon bits:")
				num_bits=float(input())
				print(((num_bits/8)/1024)/1024)
			print("\nResultado:")
			bit_to_megabyte()
		if eleccion_2=='4':
			def bit_to_gigabyte():
				print("\nPon bits:")
				num_bits=float(input())
				print((((num_bits/8)/1024)/1024)/1024)
			print("\nResultado:")
			bit_to_gigabyte()
		if eleccion_2=='5':
			def bit_to_terabyte():
				print("\nPon bits:")
				num_bits=float(input())
				print(((((num_bits/8)/1024)/1024)/1024)/1024)
			print("\nResultado:")
			bit_to_terabyte()
		if eleccion_2=='6':
			def bit_to_petabyte():
				print("\nPon bits:")
				num_bits=float(input())
				print((((((num_bits/8)/1024)/1024)/1024)/1024)/1024)
			print("\nResultado:")
			bit_to_petabyte()
	if eleccion_1== '2':
		print("\n1)Byte->Bit\n2)Byte->Kilobyte\n3)Byte->Megabyte\n4)Byte->Gigabyte\n5)Byte->Terabyte\n6)Byte->Petabyte")
		eleccion_2=input()
		if eleccion_2 == '1':
			def byte_to_bit():
				print("\nPon byte:")
				num_bytes=float(input())
				print(num_bytes*8)
			print("\nResultado:")
			byte_to_bit()
		if eleccion_2=='2':
			def byte_to_kilobyte():
				print("\nPon bytes:")
				num_bytes=float(input())
				rint(num_bytes/1024)
			print("\nResultado:")
			byte_to_kilobyte()
		if eleccion_2=='3':
			def byte_to_megabyte():
				print("\nPon bytes:")
				num_bytes=float(input())
				print(((num_bytes)/1024)/1024)
			print("\nResultado:")
			byte_to_megabyte()
		if eleccion_2=='4':
			def byte_to_gigabyte():
				print("\nPon bytes:")
				num_bytes=float(input())
				print((((num_bytes)/1024)/1024)/1024)
			print("\nResultado:")
			byte_to_gigabyte()
		if eleccion_2=='5':
			def byte_to_terabyte():
				print("\nPon bytes:")
				num_bytes=float(input())
				print(((((num_bytes)/1024)/1024)/1024)/1024)
			print("\nResultado:")
			byte_to_terabyte()
		if eleccion_2=='6':
			def byte_to_petabyte():
				print("\nPon bytes:")
				num_bytes=float(input())
				print((((((num_bytes)/1024)/1024)/1024)/1024)/1024)
			print("\nResultado:")
			byte_to_petabyte()
	if eleccion_1== '3':
		print("\n1)Kilobyte->Bit\n2)Kilobyte->Byte\n3)Kilobyte->Megabyte\n4)Kilobyte->Gigabyte\n5)Kilobyte->Terabyte\n6)Kilobyte->Petabyte")
		eleccion_2=input()
		if eleccion_2 == '1':
			def kilobyte_to_bit():
				print("\nPon kilobytes:")
				num_kilobytes=float(input())
				print((num_kilobytes*8)*1024)
			print("\nResultado:")
			kilobyte_to_bit()
		if eleccion_2=='2':
			def kilobyte_to_byte():
				print("\nPon kilobytes:")
				num_kilobytes=float(input())
				rint(num_kilobytes*1024)
			print("\nResultado:")
			kilobyte_to_byte()
		if eleccion_2=='3':
			def kilobyte_to_megabyte():
				print("\nPon kilobytes:")
				num_kilobytes=float(input())
				print((num_kilobytes)/1024)
			print("\nResultado:")
			kilobyte_to_megabyte()
		if eleccion_2=='4':
			def kilobyte_to_gigabyte():
				print("\nPon kilobytes:")
				num_kilobytes=float(input())
				print(((num_kilobytes)/1024)/1024)
			print("\nResultado:")
			kilobyte_to_gigabyte()
		if eleccion_2=='5':
			def kilobyte_to_terabyte():
				print("\nPon kilobytes:")
				num_kilobytes=float(input())
				print((((num_kilobytes/1024)/1024)/1024))
			print("\nResultado:")
			kilobyte_to_terabyte()
		if eleccion_2=='6':
			def kilobyte_to_petabyte():
				print("\nPon kilobytes:")
				num_kilobytes=float(input())
				print(((((num_kilobytes)/1024)/1024)/1024)/1024)
			print("\nResultado:")
			kilobyte_to_petabyte()
	if eleccion_1== '4':
		print("\n1)Megabyte->Bit\n2)Megabyte->Byte\n3)Megabyte->Kilobyte\n4)Megabyte->Gigabyte\n5)Megabyte->Terabyte\n6)Megabyte->Petabyte")
		eleccion_2=input()
		if eleccion_2 == '1':
			def megabyte_to_bit():
				print("\nPon megabytes:")
				num_megabytes=float(input())
				print(((num_megabytes*8)*1024)*1024)
			print("\nResultado:")
			megabyte_to_bit()
		if eleccion_2=='2':
			def megabyte_to_byte():
				print("\nPon megabytes:")
				num_megabytes=float(input())
				rint(num_megabytes*1024*1024)
			print("\nResultado:")
			megabyte_to_byte()
		if eleccion_2=='3':
			def megabyte_to_kilobyte():
				print("\nPon megabytes:")
				num_megabytes=float(input())
				print((num_megabytes)*1024)
			print("\nResultado:")
			megabyte_to_kilobyte()
		if eleccion_2=='4':
			def megabyte_to_gigabyte():
				print("\nPon megabytes:")
				num_megabytes=float(input())
				print((num_megabytes)/1024)
			print("\nResultado:")
			megabyte_to_gigabyte()
		if eleccion_2=='5':
			def megabyte_to_terabyte():
				print("\nPon megabytes:")
				num_megabytes=float(input())
				print(((num_megabytes/1024)/1024))
			print("\nResultado:")
			megabyte_to_terabyte()
		if eleccion_2=='6':
			def megabyte_to_petabyte():
				print("\nPon megabytes:")
				num_megabytes=float(input())
				print((((num_megabytes)/1024)/1024)/1024)
			print("\nResultado:")
			megabyte_to_petabyte()
	if eleccion_1== '5':
		print("\n1)Gigabyte->Bit\n2)Gigabyte->Byte\n3)Gigabyte->Kilobyte\n4)Gigabyte->Megabyte\n5)Gigabyte->Terabyte\n6)Gigabyte->Petabyte")
		eleccion_2=input()
		if eleccion_2 == '1':
			def Gigabyte_to_bit():
				print("\nPon Gigabytes:")
				num_Gigabytes=float(input())
				print(((num_Gigabytes*8)*1024)*1024*1024)
			print("\nResultado:")
			Gigabyte_to_bit()
		if eleccion_2=='2':
			def Gigabyte_to_byte():
				print("\nPon Gigabytes:")
				num_Gigabytes=float(input())
				rint(num_Gigabytes*1024*1024*1024)
			print("\nResultado:")
			Gigabyte_to_byte()
		if eleccion_2=='3':
			def Gigabyte_to_kilobyte():
				print("\nPon Gigabytes:")
				num_Gigabytes=float(input())
				print((num_Gigabytes)*1024*1024)
			print("\nResultado:")
			Gigabyte_to_kilobyte()
		if eleccion_2=='4':
			def Gigabyte_to_megabyte():
				print("\nPon Gigabytes:")
				num_Gigabytes=float(input())
				print((num_Gigabytes)*1024)
			print("\nResultado:")
			Gigabyte_to_megabyte()
		if eleccion_2=='5':
			def Gigabyte_to_terabyte():
				print("\nPon Gigabytes:")
				num_Gigabytes=float(input())
				print(num_Gigabytes/1024)
			print("\nResultado:")
			Gigabyte_to_terabyte()
		if eleccion_2=='6':
			def Gigabyte_to_petabyte():
				print("\nPon Gigabytes:")
				num_Gigabytes=float(input())
				print(((num_Gigabytes)/1024)/1024)
			print("\nResultado:")
			Gigabyte_to_petabyte()
	if eleccion_1== '6':
		print("\n1)Terabyte->Bit\n2)Terabyte->Byte\n3)Terabyte->Kilobyte\n4)Terabyte->Megabyte\n5)Terabyte->Gigabyte\n6)Terabyte->Petabyte")
		eleccion_2=input()
		if eleccion_2 == '1':
			def Terabyte_to_bit():
				print("\nPon Terabytes:")
				num_Terabytes=float(input())
				print(((num_Terabytes*8)*1024)*1024*1024*1024)
			print("\nResultado:")
			Terabyte_to_bit()
		if eleccion_2=='2':
			def Terabyte_to_byte():
				print("\nPon Terabytes:")
				num_Terabytes=float(input())
				rint(num_Terabytes*1024*1024*1024*1024)
			print("\nResultado:")
			Terabyte_to_byte()
		if eleccion_2=='3':
			def Terabyte_to_kilobyte():
				print("\nPon Terabytes:")
				num_Terabytes=float(input())
				print((num_Terabytes)*1024*1024*1024)
			print("\nResultado:")
			Terabyte_to_kilobyte()
		if eleccion_2=='4':
			def Terabyte_to_megabyte():
				print("\nPon Terabytes:")
				num_Terabytes=float(input())
				print((num_Terabytes)*1024*1024)
			print("\nResultado:")
			Terabyte_to_megabyte()
		if eleccion_2=='5':
			def Terabyte_to_gigabyte():
				print("\nPon Terabytes:")
				num_Terabytes=float(input())
				print(num_Terabytes*1024)
			print("\nResultado:")
			Terabyte_to_gigabyte()
		if eleccion_2=='6':
			def Terabyte_to_petabyte():
				print("\nPon Terabytes:")
				num_Terabytes=float(input())
				print((num_Terabytes)/1024)
			print("\nResultado:")
			Terabyte_to_petabyte()
	if eleccion_1== '7':
		print("\n1)Petabyte->Bit\n2)Petabyte->Byte\n3)Petabyte->Kilobyte\n4)Petabyte->Megabyte\n5)Petabyte->Gigabyte\n6)Petabyte->Terabyte")
		eleccion_2=input()
		if eleccion_2 == '1':
			def Petabyte_to_bit():
				print("\nPon Petabytes:")
				num_Petabytes=float(input())
				print(((num_Petabytes*8)*1024)*1024*1024*1024*1024)
			print("\nResultado:")
			Petabyte_to_bit()
		if eleccion_2=='2':
			def Petabyte_to_byte():
				print("\nPon Petabytes:")
				num_Petabytes=float(input())
				rint(num_Petabytes*1024*1024*1024*1024*1024)
			print("\nResultado:")
			Petabyte_to_byte()
		if eleccion_2=='3':
			def Petabyte_to_kilobyte():
				print("\nPon Petabytes:")
				num_Petabytes=float(input())
				print((num_Petabytes)*1024*1024*1024*1024)
			print("\nResultado:")
			Petabyte_to_kilobyte()
		if eleccion_2=='4':
			def Petabyte_to_megabyte():
				print("\nPon Petabytes:")
				num_Petabytes=float(input())
				print((num_Petabytes)*1024*1024*1024)
			print("\nResultado:")
			Petabyte_to_megabyte()
		if eleccion_2=='5':
			def Petabyte_to_gigabyte():
				print("\nPon Petabytes:")
				num_Petabytes=float(input())
				print(num_Petabytes*1024*1024)
			print("\nResultado:")
			Petabyte_to_gigabyte()
		if eleccion_2=='6':
			def Petabyte_to_terabyte():
				print("\nPon Petabytes:")
				num_Petabytes=float(input())
				print((num_Petabytes)*1024)
			print("\nResultado:")
			Petabyte_to_terabyte()

main()
def looop():
	print("\n¿Volver? Si/No")
	eleccionvolverr=input()
	eleccionvolver=eleccionvolverr.lower()
	if eleccionvolver == 'si':
		main()
	if eleccionvolver == 'no':
		sys.exit()

i=1
while i<10:
	looop()
