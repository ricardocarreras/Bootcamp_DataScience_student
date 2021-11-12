# Para importar los métodos de las clases de mobile.py

import mobile

def main():
    try:
        samsung_a20 = mobile.Samsung("4gb", "6.1", 245.00, "15MP","4500",10)
        apple_13 = mobile.Apple("8gb",6.1,900,"15MP","4500","camara3d")
        
    except Exception as e:
        print(e)
    
    finally:
        print("Samsung A20")
        print("#"*20)
        print(f"Display: {samsung_a20.get_display()}")
        print(f"Perfomance: {samsung_a20.get_perfomance()}")
        print(f"Ram: {samsung_a20.get_ram()}")
        print("#"*20)

        print("Apple 13")
        print("#"*20)
        print(f"Display: {apple_13.get_display()}")
        print(f"Perfomance: {apple_13.get_detalle()}")
        print(f"Ram: {apple_13.get_ram()}")
        print("#"*20)

main()