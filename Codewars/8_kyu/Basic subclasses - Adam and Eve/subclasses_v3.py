Human = type("", (), {})
Man = Woman = type("", (Human,), {})
God = lambda: [Man(), Woman()]
