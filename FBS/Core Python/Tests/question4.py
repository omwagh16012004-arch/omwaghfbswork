
area = float(input('Enter area of one wall: '))

interior_walls = int(input('Enter number of interior wall surfaces: '))
exterior_walls = int(input('Enter number of exterior wall surfaces: '))

interior_rate = float(input('Enter interior painting rate per unit area: '))
exterior_rate = float(input('Enter exterior painting rate per unit area: '))

interior_area = area * interior_walls
exterior_area = area * exterior_walls

interior_cost = interior_area * interior_rate
exterior_cost = exterior_area * exterior_rate

total_cost = interior_cost + exterior_cost

print('Interior painting cost =', interior_cost)
print('Exterior painting cost =', exterior_cost)
print('Total painting cost =', total_cost)
