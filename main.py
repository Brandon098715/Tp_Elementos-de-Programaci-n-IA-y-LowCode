from funciones import (
    cargar_gastos,
    guardar_gastos,
    crear_gasto,
    mostrar_gastos,
    pedir_categoria,
    pedir_mes,
    filtrar_por_categoria,
    filtrar_por_mes,
    buscar_por_id,
    pedir_id,
    confirmar,
    modificar_gasto,
    mostrar_indicadores,
    generar_grafico,
)


def mostrar_menu() -> None:
    print("\n===== GASTOS PERSONALES =====")
    print("1. Registrar gasto")
    print("2. Listar gastos")
    print("3. Filtrar por categoría")
    print("4. Filtrar por mes (AAAA-MM)")
    print("5. Modificar gasto")
    print("6. Eliminar gasto")
    print("7. Ver indicadores")
    print("8. Generar gráfico por categoría")
    print("9. Salir")


def main() -> None:
    gastos: list[dict] = cargar_gastos()
    opcion: str = ""

    while opcion != "9":
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            print("\n--- Registrar gasto ---")
            gasto: dict = crear_gasto(gastos)
            gastos.append(gasto)
            guardar_gastos(gastos)
            print(f"Gasto registrado con id {gasto['id']} por ${gasto['monto']:,.2f}.")

        elif opcion == "2":
            print("\n--- Listado de gastos ---")
            mostrar_gastos(gastos)

        elif opcion == "3":
            print("\n--- Filtrar por categoría ---")
            categoria: str = pedir_categoria()
            mostrar_gastos(filtrar_por_categoria(gastos, categoria))

        elif opcion == "4":
            print("\n--- Filtrar por mes ---")
            mes: str = pedir_mes()
            mostrar_gastos(filtrar_por_mes(gastos, mes))

        elif opcion == "5":
            print("\n--- Modificar gasto ---")
            if len(gastos) == 0:
                print("No hay gastos para modificar.")
            else:
                id_gasto: int = pedir_id(gastos)
                gasto_elegido: dict = buscar_por_id(gastos, id_gasto)
                if modificar_gasto(gasto_elegido):
                    guardar_gastos(gastos)
                    print(f"Gasto {id_gasto} modificado y guardado.")
                else:
                    print("No se hicieron cambios.")

        elif opcion == "6":
            print("\n--- Eliminar gasto ---")
            if len(gastos) == 0:
                print("No hay gastos para eliminar.")
            else:
                id_gasto = pedir_id(gastos)
                gasto_elegido = buscar_por_id(gastos, id_gasto)
                mostrar_gastos([gasto_elegido])
                if confirmar("¿Seguro que querés eliminar este gasto?"):
                    gastos.remove(gasto_elegido)
                    guardar_gastos(gastos)
                    print(f"Gasto {id_gasto} eliminado.")
                else:
                    print("Eliminación cancelada.")

        elif opcion == "7":
            print("\n--- Indicadores ---")
            mostrar_indicadores(gastos)

        elif opcion == "8":
            print("\n--- Gráfico por categoría ---")
            generar_grafico(gastos)

        elif opcion == "9":
            print("¡Hasta luego!")

        else:
            print("Opción inválida. Elegí un número del 1 al 9.")


if __name__ == "__main__":
    main()
