from datetime import datetime

n=1000000000000000
print(f"{n:_}")
print(f"{n:,}")

string="Tawfeeq"
print(f"{string:20}")
print(f"{string:<20}:")
print(f"{string:>20}:")
print(f"{string:^20}:")
print(f"{string:!^20}:")

now= datetime.now()
print(f'{now:%d.%m.%y}')
print(f'{now:%d-%m-%y [%H:%M.%S]}')
print(f'{now:%c}')
print(f'{now:%I %p}')

pi=3.14159265359
print(f'{pi:.2f}')
print(f'{pi:.0f}')
x=839472943.27845321374
print(f'{x:,.4f}')

print(f'pi + pi = {pi+pi}')
print(f'{pi + pi = }')

