import os
import pandas as pd
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4.tree.Tree import TerminalNode
import graphviz
from antlr_gen.OrdenesServiciosLexer import OrdenesServiciosLexer
from antlr_gen.OrdenesServiciosParser import OrdenesServiciosParser
from visitor import MyVisitor

def mostrar_menu(scripts_dir="scripts"):
    scripts = [f for f in os.listdir(scripts_dir) if f.endswith(".dsl")]
    print("\n=== MENU DE SCRIPTS DISPONIBLES ===")
    for idx, script in enumerate(scripts, 1):
        print(f"{idx}. {script}")
    print("0. Salir")
    return scripts

def mostrar_tokens(archivo):
    input_stream = FileStream(archivo, encoding="utf-8")
    lexer = OrdenesServiciosLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    tokens.fill()
    print("\n=== TOKENS GENERADOS ===")
    for token in tokens.tokens:
        print(token)

def mostrar_parse_tree(archivo):
    input_stream = FileStream(archivo, encoding="utf-8")
    lexer = OrdenesServiciosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OrdenesServiciosParser(stream)
    tree = parser.script()
    print("\n=== ARBOL SINTACTICO (Parse Tree - texto) ===")
    print(tree.toStringTree(recog=parser))

def exportar_arbol_parse(archivo):
    input_stream = FileStream(archivo, encoding="utf-8")
    lexer = OrdenesServiciosLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = OrdenesServiciosParser(token_stream)
    tree = parser.script()

    dot = graphviz.Digraph(comment="Parse Tree")
    node_count = [0]

    def agregar_nodo(t, parent_id=None):
        current_id = f"node{node_count[0]}"
        if isinstance(t, TerminalNode):
            label = t.getText().replace('"', r'\"')
        else:
            label = parser.ruleNames[t.getRuleContext().getRuleIndex()]
        dot.node(current_id, label)
        if parent_id:
            dot.edge(parent_id, current_id)
        node_count[0] += 1
        if not isinstance(t, TerminalNode):
            for i in range(t.getChildCount()):
                agregar_nodo(t.getChild(i), current_id)

    agregar_nodo(tree)
    dot.render("parser_tree", format="png", cleanup=True)
    print("✅ Árbol sintáctico exportado como parser_tree.png")

def analizar_script(script_text):
    lineas = script_text.strip().splitlines()
    resumen = {
        "load": 0,
        "filters": 0,
        "aggregates": 0,
        "print": 0,
        "funciones": set()
    }
    for linea in lineas:
        if linea.startswith("load"):
            resumen["load"] += 1
        elif linea.startswith("filter"):
            resumen["filters"] += 1
        elif linea.startswith("aggregate"):
            resumen["aggregates"] += 1
            resumen["funciones"].add(linea.split()[1])
        elif linea.startswith("print"):
            resumen["print"] += 1
    print("\n=== ANALISIS SINTETICO DEL SCRIPT ===")
    print(f"- Instruccion load: {resumen['load']}")
    print(f"- Filtros aplicados: {resumen['filters']}")
    print(f"- Agregaciones aplicadas: {resumen['aggregates']}")
    print(f"- Funciones usadas: {', '.join(resumen['funciones'])}")
    print(f"- Instruccion print: {resumen['print']}")

def ejecutar_script(archivo):
    print(f"\n=== CONTENIDO DEL SCRIPT ({archivo}) ===")
    with open(archivo, encoding="utf-8") as f:
        script = f.read()
        print(script)

    analizar_script(script)

    input_stream = FileStream(archivo, encoding="utf-8")
    lexer = OrdenesServiciosLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OrdenesServiciosParser(stream)
    tree = parser.script()

    visitor = MyVisitor()
    visitor.visit(tree)

    if visitor.df is not None:
        df_filtrado = visitor.df

        if visitor.filters:
            print("\n=== CONSULTA APLICADA ===")
            query_expr = " and ".join(visitor.filters)
            print(query_expr)
            try:
                df_filtrado = df_filtrado.query(query_expr)
            except Exception as e:
                print(f"\n[ERROR] al aplicar filtros: {e}")
                return

        print(f"\n=== REGISTROS QUE CUMPLEN LA CONDICION ({len(df_filtrado)}) ===")
        print(df_filtrado.to_string(index=False))

        count_aggregates = [col for func, col in getattr(visitor, "aggregates", []) if func == "count"]
        for col in count_aggregates:
            if col in df_filtrado.columns:
                print(f"\n=== REGISTROS COMPLETOS AGRUPADOS POR '{col}' ===")
                for valor in df_filtrado[col].unique():
                    print(f"\n→ {col}: {valor}")
                    print(df_filtrado[df_filtrado[col] == valor].to_string(index=False))

if _name_ == "_main_":
    while True:
        scripts = mostrar_menu()
        opcion = input("\nSeleccione un script (0 para salir): ")
        if opcion == "0":
            print("Saliendo...")
            break
        elif opcion.isdigit() and 1 <= int(opcion) <= len(scripts):
            archivo = os.path.join("scripts", scripts[int(opcion) - 1])

            print("\n=== OPCIONES ===")
            print("1. Ejecutar y mostrar resultados")
            print("2. Mostrar tokens")
            print("3. Mostrar árbol sintáctico (texto)")
            print("4. Exportar árbol sintáctico (imagen PNG)")
            opcion2 = input("Seleccione opción: ")

            if opcion2 == "1":
                ejecutar_script(archivo)
            elif opcion2 == "2":
                mostrar_tokens(archivo)
            elif opcion2 == "3":
                mostrar_parse_tree(archivo)
            elif opcion2 == "4":
                exportar_arbol_parse(archivo)
            else:
                print("Opción inválida.")
        else:
            print("Opción inválida. Intente nuevamente.")
