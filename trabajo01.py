from ortools.init.python import init
from ortools.linear_solver import pywraplp

def main():
    print("Google OR-Tools version:", init.OrToolsVersion.version_string())

    #Se crea la funcion que soluciona los problemas
    solver : pywraplp.Solver = pywraplp.Solver.CreateSolver("GLOP")
    #En caso que no se crea el objeto
    if not solver:
        print("No se pudo crear solver GLOP")
        return
    #Creacion de las restricciones
    x_var :pywraplp.Variable = solver.NumVar(0,1,"x")
    y_var: pywraplp.Variable = solver.NumVar(0,2,"y")
    print("Valores de las variables = ", solver.NumVariables())

    infinito = solver.infinity()

    restriccion: pywraplp.Constraint =  solver.Constraint(-infinito, 2, "ct1")
    restriccion.SetCoefficient(x_var,1)
    restriccion.SetCoefficient(y_var,1)

    restriccion2: pywraplp.Constraint = solver.Constraint(-infinito, 5, "ct2")
    restriccion2.SetCoefficient(x_var,2)
    restriccion2.SetCoefficient(y_var,-1)
    print("Numero de restriccion  = ", solver.NumConstraints())

    #Funcion objetivo
    objetivo : pywraplp.Objective = solver.Objective()
    objetivo.SetCoefficient(x_var,4)
    objetivo.SetCoefficient(y_var,2)
    objetivo.SetMaximization()

    #Resolucion del problema
    estado = solver.Solve()
    if estado != pywraplp.Solver.OPTIMAL:
        print("No se encontro una solucion optima")
    else:
        print("Se encontro una solucion optima")
        print("Solucion")
        print("Valor objetivo =", objetivo.Value())
        print("x = ", x_var.solution_value())
        print("y = ", y_var.solution_value())
    print("Datos tecnicos: ")
    print(f"Se resuelve en {solver.wall_time():d} millisegundos")
    print(f"Se resuelve en {solver.iterations():d} iteraciones")


#Llamma la funcion main
if __name__ == "__main__" : 
    init.CppBridge.init_logging("wa.py")
    cpp_flag = init.CppFlags()
    cpp_flag.stderrthreshold = True
    cpp_flag.log_prefix = False
    init.CppBridge.set_flags(cpp_flag)
    main()

