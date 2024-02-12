from periodic_table import PeriodicTable

if __name__ == '__main__':
    periodic_table = PeriodicTable()
    for element in periodic_table.elements:
        print(f'{element.name} [{element.symbol}]: {element.mass}'.replace('\'', '').replace("(", "").replace(")", "").replace(",", ""))
