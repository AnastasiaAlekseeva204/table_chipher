from enhanced_table_cipher import encrypt, decrypt

def run_test(name, func, expected):
    result = func()
    if result == expected:
        print(f"[PASS] {name}")
    else:
        print(f"[FAIL] {name}\n  expected: {expected}\n  got:      {result}")

def test_cases():
    run_test("Encrypt basic", lambda: encrypt("HELLO WORLD", "ZEBRAS"), "OXRWDELHLLO")
    run_test("Decrypt basic", lambda: decrypt("OXRWDELHLLO", "ZEBRAS"), "HELLOWORLD")
    run_test("Encrypt short", lambda: encrypt("ATTACKATDAWN", "CARGO"), "TCWTNAKADATX")
    run_test("Decrypt short", lambda: decrypt("TCWTNAKADATX", "CARGO"), "ATTACKATDAWN")

if __name__ == "__main__":
    test_cases()