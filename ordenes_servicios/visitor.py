import pandas as pd
from antlr_gen.OrdenesServiciosVisitor import OrdenesServiciosVisitor
from antlr_gen.OrdenesServiciosParser import OrdenesServiciosParser

# Funciones tipo "switch-case"
def ejecutar_count(df, col):
    return f"→ count({col}) = {df[col].count()}"

def ejecutar_sum(df, col):
    return f"→ sum({col}) = {df[col].sum()}"

def ejecutar_average(df, col):
    return f"→ average({col}) = {df[col].mean():.2f}"

def ejecutar_between(df, col):
    filtro = df[(df[col] >= 100000) & (df[col] <= 200000)]
    return f"→ between({col} entre 100k y 200k) = {len(filtro)}"

# Diccionario que simula un switch
AGGREGATE_SWITCH = {
    "count": ejecutar_count,
    "sum": ejecutar_sum,
    "average": ejecutar_average,
    "between": ejecutar_between,
}

class MyVisitor(OrdenesServiciosVisitor):
    def __init__(self):
        self.file = None
        self.df = None
        self.filters = []
        self.aggregates = []

    def visitScript(self, ctx):
        for command in ctx.command():
            self.visit(command)

    def visitLoadCmd(self, ctx):
        self.file = ctx.STRING().getText().strip('"')
        self.df = pd.read_csv(self.file)
        print(f"[INFO] Cargado: {self.file} ({len(self.df)} filas)")

    def visitFilterCmd(self, ctx):
        column = ctx.STRING().getText().strip('"')
        operator = ctx.OPERATOR().getText()
        val = ctx.value()
        value = val.NUMBER().getText() if val.NUMBER() else val.STRING().getText().strip('"')

        condition = f'`{column}` {operator} {repr(value)}'
        self.filters.append(condition)

        if ctx.LOGIC_OP():
            logical_op = ctx.LOGIC_OP().getText()
            nested = self.visitFilterCmd(ctx.filterCmd())
            combined = f"({condition}) {logical_op.lower()} ({nested})"
            self.filters[-1] = combined
            return combined

        return condition

    def visitAggregateCmd(self, ctx):
        func = ctx.aggFunc().getText().lower()
        column = ctx.STRING().getText().strip('"')
        self.aggregates.append((func, column))

    def visitPrintCmd(self, ctx):
        if self.df is None:
            print("[ERROR] No se ha cargado ningún archivo.")
            return

        # Aplicar filtros directamente a self.df
        if self.filters:
            query_expr = " and ".join(self.filters)
            try:
                self.df = self.df.query(query_expr)
            except Exception as e:
                print(f"[ERROR] Error al aplicar filtros: {e}")
                return

        print("\n[RESULTADOS]")
        for func, col in self.aggregates:
            if func in AGGREGATE_SWITCH:
                try:
                    resultado = AGGREGATE_SWITCH[func](self.df, col)
                    print(resultado)
                except Exception as e:
                    print(f"[ERROR] al ejecutar '{func}' en '{col}': {e}")
            else:
                print(f"[AVISO] Función no reconocida: {func}")

        self.filters.clear()
        self.aggregates.clear()
