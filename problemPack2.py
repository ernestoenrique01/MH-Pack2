'''
    Tarea 2

enunciado: pack2
equipo:
    Pablo D. Morales
    Mario Perera
    Ernesto E. Serrano
'''
import random
from typing import List, Container


### Clases Contenedor, Paquete y Solución###
class Package:
    id: int
    volume: float

    def __init__(self, id: int, volume: float):
        self.id = id
        self.volume = volume

    def getVolume(self) -> float:
        return self.volume

    def getId(self) -> int:
        return self.id


class Container:
    id: int
    totalVolume: float
    emptyVolume: float
    packageList: List[Package]

    def __init__(self, id: int, totalVolume: float):
        self.id = id
        self.totalVolume = totalVolume
        self.emptyVolume = totalVolume
        self.packageList = []

    def getId(self) -> int:
        return self.id

    def getTotalVolume(self) -> float:
        return self.totalVolume

    def getEmptyVolume(self) -> float:
        return self.emptyVolume

    def getPackageList(self):
        return self.packageList

    def addPackage(self, package: Package):
        self.packageList.append(package)
        self.emptyVolume -= package.getVolume()

    def thatPackageFit(self, package: Package) -> bool:
        return package.getVolume() <= self.emptyVolume


class Solution:
    def __init__(self):
        self.value = 0
        self.container_list = []
        self.unassigned_packages = []

    def get_value(self):
        return self.value

    def get_container_list(self):
        return self.container_list

    def get_unassigned_packages(self):
        return self.unassigned_packages

    def set_value(self, new_value):
        self.value = new_value

    def set_container_list(self, new_container_list):
        self.container_list = new_container_list

    def set_unassigned_packages(self,new_unassigned_packages):
        self.unassigned_packages = new_unassigned_packages

    def add_container(self, container):
        self.container_list.append(container)

    def copy(self):
        new_solution = Solution()
        new_solution.container_list = self.container_list.copy()
        new_solution.unassigned_packages = self.unassigned_packages.copy()
        return new_solution

##############################################
Presentation  = 'Pack2 Problem'

def present_problem():
    print('----------------------------------------------------------------------')
    print(Presentation)
    print(f'CANTIDAD_CONTENEDORES = 3, CAPACITY = (90,90,150),'
          f'CANTIDAD DE OBJETOS = (16), VOLUMEN TOTAL = (849)')
    print('----------------------------------------------------------------------')

def objective_function(solution): #Función objetivo
    value = 0
    for c in solution:
        for p in c.getPackageList():
            value = value + p.getVolume()
    return value


def random_solution():
    solution = Solution()
    random.shuffle(packList)  # Barajamos los paquetes aleatoriamente

    for package in packList:
        random_container = random.choice(containers)  # Elegimos un contenedor aleatorio

        if random_container.thatPackageFit(package):  # Si el paquete cabe en el contenedor
            random_container.addPackage(package)  # Lo agregamos al contenedor
            solution.set_value(solution.get_value() + package.getVolume())  # Actualizamos el valor de la solución
        else:
            solution.get_unassigned_packages().append(
                package)  # Agregamos el paquete a la lista de paquetes no asignados

    for container in containers:
        solution.add_container(container)  # Agregamos todos los contenedores a la solución

    return solution.get_container_list()

def random_change(solution, max_attempts: int = 10):
    containers = solution
    unassigned_packages = get_unassigned_packages(solution)

    # Intercambio de paquetes entre contenedores o con paquetes sin asignar
    attempts = 0  # Contador de intentos
    while attempts < max_attempts:
        random_container1 = random.choice(containers)
        random_container2 = random.choice(containers + [None])  # Agregar opción de intercambiar con paquete sin asignar

        # Verificar que los contenedores sean diferentes
        if random_container2 is None or random_container1 != random_container2:
            package1 = random.choice(random_container1.getPackageList() if random_container1 else unassigned_packages)
            package2 = random.choice(random_container2.getPackageList() if random_container2 else unassigned_packages)

            # Verificar que los paquetes tengan volúmenes diferentes
            if package1.getVolume() != package2.getVolume():
                if random_container1 and random_container1.thatPackageFit(package2):  # Verificar si el paquete 2 cabe en el contenedor 1
                    random_container1.getPackageList().remove(package1)
                    random_container1.addPackage(package2)
                elif random_container2 and random_container2.thatPackageFit(package1):  # Verificar si el paquete 1 cabe en el contenedor 2
                    random_container2.getPackageList().remove(package2)
                    random_container2.addPackage(package1)
                else:
                    # Si no caben en los contenedores correspondientes, incrementar el contador de intentos y continuar con el siguiente intento
                    attempts += 1
                    continue

                # Actualizar el volumen vacío de los contenedores
                for container in containers:
                    container.emptyVolume = container.totalVolume - sum(package.getVolume() for package in container.packageList)

                break

        attempts += 1

    return solution

def not_random_solution() -> Solution:
    # Empaquetando primero los de mayor volumen
    solution = Solution(0)

    sorted_packages = sorted(packList, key=lambda package: package.getVolume(), reverse=True)  # Ordenamos los paquetes de mayor a menor tamaño

    for package in sorted_packages:
        added_to_container = False  # Variable para verificar si el paquete se ha agregado a algún contenedor

        for container in containers:
            if container.thatPackageFit(package):  # Si el paquete cabe en el contenedor
                container.addPackage(package)  # Lo agregamos al contenedor
                solution.set_value(solution.get_value() + package.getVolume())  # Actualizamos el valor de la solución
                added_to_container = True
                break  # Pasamos al siguiente paquete después de colocarlo en un contenedor

        if not added_to_container:
            solution.get_unassigned_packages().append(package)  # Agregamos el paquete a la lista de paquetes no asignados

    for container in containers:
        solution.add_container(container)  # Agregamos todos los contenedores a la solución

    return solution

def not_random_change(solution):
    containers = solution
    unassigned_packages = get_unassigned_packages(solution)

    # Obtener el paquete con el menor volumen de la lista de paquetes no asignados
    min_volume_package = min(unassigned_packages, key=lambda package: package.getVolume())

    # Buscar el contenedor con el mayor volumen vacío
    max_empty_volume_container = max(containers, key=lambda container: container.emptyVolume)

    # Verificar si el paquete con el menor volumen cabe en el contenedor con el mayor volumen vacío
    if max_empty_volume_container.thatPackageFit(min_volume_package):
        # Remover el paquete de la lista de paquetes no asignados
        unassigned_packages.remove(min_volume_package)

        # Agregar el paquete al contenedor con el mayor volumen vacío
        max_empty_volume_container.addPackage(min_volume_package)

        # Actualizar el volumen vacío del contenedor
        max_empty_volume_container.emptyVolume -= min_volume_package.getVolume()
    make_solution_feasible(solution)
    return

def random_combination(solution1, solution2):
    # Crear una nueva solución vacía con los mismos contenedores que la solución original
    new_solution = solution1.copy()

    # Obtener la longitud de la solución más corta
    min_length = min(len(solution1), len(solution2))

    # Realizar el intercambio aleatorio de contenedores
    for i in range(min_length):
        # Determinar aleatoriamente si se realiza el intercambio
        do_swap = random.choice([True, False])

        if do_swap:
            # Intercambiar los contenedores de la solución original
            new_solution[i], solution2[i] = solution2[i], solution1[i]

    make_solution_feasible(new_solution) #Convertir en solución factible

    return new_solution

def get_unassigned_packages(containers):
    assigned_packages = [package for container in containers for package in container.getPackageList()]
    unassigned_packages = [package for package in packList if package not in assigned_packages]
    return unassigned_packages

def show_solution(solution):
    print("Container List:")
    for container in solution:
        print(f"Container {container.getId()}:")
        print(f"Total Volume: {container.getTotalVolume()}")
        print(f"Empty Volume: {container.getEmptyVolume()}")
        print("Package List:")
        for package in container.getPackageList():
            print(f"Package {package.getId()}: Volume {package.getVolume()}")
        print("------------------------")
    print(f"Total Value: {objective_function(solution)}")


def remove_duplicate_packages(solution):
    unique_packages = set()  # Conjunto para realizar un seguimiento de los paquetes únicos

    for container in solution:
        package_list = container.getPackageList()
        new_package_list = []

        for package in package_list:
            if package not in unique_packages:
                unique_packages.add(package)
                new_package_list.append(package)

        container.packageList = new_package_list
        container.emptyVolume = container.totalVolume - sum([p.getVolume() for p in new_package_list])

def make_solution_feasible(solution):
    remove_duplicate_packages(solution)
    for container in solution:
        while container.getEmptyVolume() < 0:
            package_list = container.getPackageList()
            if len(package_list) > 0:
                # Seleccionar el paquete de menor volumen para eliminarlo
                package_to_remove = package_list[0]
                for package in package_list:
                    if package.getVolume() < package_to_remove.getVolume():
                        package_to_remove = package
                # Eliminar el paquete del contenedor
                container.getPackageList().remove(package_to_remove)
                container.emptyVolume += package_to_remove.getVolume()
            else:
                break

def showContainerList(containers: List[Container]):
    print('. .Contenedores. .')

    for c in containers:
        print(f'ID: {c.getId()}')
        print(f'Volumen total: {c.getTotalVolume()}')
        print(f'Volumen vacío: {c.getEmptyVolume()}')

        if (len(c.getPackageList()) > 0):
            showPackageList(c.getPackageList())


def showPackageList(packageList: List[Package]):
    print('  Paquetes')

    for p in packageList:
        print(f'  id: {p.getId()}. Volumen: {p.getVolume()}')
    #    print(f'Volumen: {p.getVolume()}')

def best_solution(solution_1: Solution, solution_2: Solution) -> Solution:
    if solution_1.get_value() > solution_2.get_value():
        return solution_1
    else:
        return solution_2

import math
def search_space_size(n_packages, m_containers):
    total_sum = 0
    for i in range(1, n_packages + 1):
        coefficient = math.comb(n_packages, i)
        total_sum += coefficient * (m_containers ** i)

    return total_sum

### Main ###
main_solution : Solution

c1 = Container(1, 80)
c2 = Container(2, 120)
c3 = Container(3, 180)
c4 = Container(4, 40)
c5 = Container(5, 90)
c6 = Container(6, 150)
containers: List[Container]
containers = [c1, c2, c3, c4]
containers2 = [c4, c5, c6]

p1 = Package(1, 55)
p2 = Package(2, 32)
p3 = Package(3, 33)
p4 = Package(4, 46)
p5 = Package(5, 190)
p6 = Package(6, 66)
p7 = Package(7, 77)
p8 = Package(8, 87)
p9 = Package(9, 92)
p10 = Package(10, 104)
p11 = Package(11, 110)
p12 = Package(12, 34)
p13 = Package(13, 27)
p14 = Package(14, 58)
p15 = Package(15, 12)
p16 = Package(16, 17)
packList: List[Package]
packList = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]

#s1 = create_solution_max_volumen_packages(containers, packList)
#s2 = random_solution(containers2, packList)
#show_solution(s1)
#print("--------------------SDASFDASDFSDF-------------------")
#show_solution(s2)
#print("--------------------SDASFDASDFSDF-------------------")
#show_solution(best_solution(s1, s2))
#print(objective_function(s2.get_container_list()))

s2 = random_solution()
show_solution(s2)
print("--------------------SDASFDASDFSDF-------------------")
not_random_change(s2)
show_solution(s2)

#showPackageList(packList)
#fillContainers_ByOrderList(containers, packList)
#showContainerList(containers)
