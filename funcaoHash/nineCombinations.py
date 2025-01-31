def hash_summation(key):
    return sum(ord(c) for c in key)

def hash_polynomial_rolling(key, a=31):
    hash_value = 0
    for c in key:
        hash_value = hash_value * a + ord(c)
    return hash_value

def hash_critical_shift(key):
    hash_value = 0
    for c in key:
        hash_value ^= ord(c)
        hash_value = (hash_value << 5) | (hash_value >> 27)
    return hash_value


def compression_division(hash_value, size=32):
    return hash_value % size

def compression_folding(hash_value, size=32):
    str_hash = str(abs(hash_value))
    parts = [int(str_hash[i:i+2]) for i in range(0, len(str_hash), 2)]
    return sum(parts) % size

def compression_mad(hash_value, size=32, a=31, b=7):
    return ((a * hash_value + b) % 100003) % size


def test_hashing(strings, hash_func, compression_func, size=32):
    table = [None] * size
    collisions = 0

    for s in strings:
        hash_value = hash_func(s)
        index = compression_func(hash_value, size)
        
        if table[index] is not None:
            collisions += 1
        table[index] = s
    
    return collisions, table


test_strings = ["apple", "voadora", "banjo", "banana", "cherry", "date",
                "elderberry", "fig", "grape", "honeydew", "kiwi", "xuru", "runin", "xamã",
                "mirtilho", "lemon", "mango", "nectarine", "orange", "papaya", "quince",
                "raspberry", "strawberry", "tangerine", "ugli", "voavanga", "maravilha",
                "IFCE", "maracanaú", "ceará", "manga", "rendemption", "bobo", "maluco"]


dispersion_methods = {
    "Summation": hash_summation,
    "Polynomial": hash_polynomial_rolling,
    "Critical Shift": hash_critical_shift
}

compression_methods = {
    "Division": compression_division,
    "Folding": compression_folding,
    "MAD": compression_mad
}


results = {}
for disp_name, disp_func in dispersion_methods.items():
    for comp_name, comp_func in compression_methods.items():
        collisions, table = test_hashing(test_strings, disp_func, comp_func)
        results[(disp_name, comp_name)] = collisions
        print(f"{disp_name} + {comp_name}: {collisions} colisões")
        print("Tabela Hash Resultante:")
        for i, value in enumerate(table):
            print(f"{i}: {value}")
        print("-" * 50)

best_method = min(results, key=results.get)
print(f"Melhor método: {best_method[0]} + {best_method[1]} com {results[best_method]} colisões")
