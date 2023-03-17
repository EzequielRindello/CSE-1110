import math

def AreaCalulator(radio):
    return math.pi*(radio**2)

def main():
    radios=[23.5,46.6,56.7,7.8]

    areas=[]

    areas=list(map(AreaCalulator,radios))

    print(areas)

if __name__ == "__main__":
    main()