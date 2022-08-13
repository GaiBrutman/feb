# FEB API

As stated in [README.md](README.md), FEB travels inside a binary, then extracts values from it.

## Cursor

The basic part of traveling is the cursor.
A cursor is basically an integer representing the current location inside the binary.

```py
c = Cursor(0x1234)
c += 1  # Cursor(0x1235)
```

The binary cursor is *always* the absolute non-rebased offset of the file.
Because an executable is commonly rebased to a certain offset, a `RebasedCursor` can be used.
The `RebasedCursor` follows it's inner cursor and maps the cursor values to it's base offset.

```py
c = Cursor(5)
rebased_c = RebasedCursor(c, base=10)
c.value += 1  # 6
rebased_c.value  # 16

rebased_c += 1 # RebasedCursor(17)
c.value  # 7
```

## Expressions and Operands

The extraction process is performed using `Expression`s and `Operand`s.
An `Expression` represents a singular code unit, that holds `Operand`s.

For example, in disassembly, an expression can be an assembly instruction:

```py
expression = AsmInstruction("mov ax, 1")
```

And operands can be any part of the expression that can produce a value:

```py
# [X86Register("ax"), Integer(1)]
operands = expression.get_operands()
```

## Binary

A binary holds shared information about the binary state.
The main usage of `Binary` is to share a `Cursor` between different `View`s.

```py
binary = Binary("executable.bin")
binary.cursor += 1
```
