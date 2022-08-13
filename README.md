# feb

FEB Explores Binaries.

Exploration consists of two parts:

- Travel: Moving through the binary to a specific location
- Extraction: Extracting a value from the expression at the current location

## Example

Considering the following disassembly view:

```nasm
0   push rbp
1   mov rbp, rsp
2   sub rsp, 0x10
3   mov edi, 0x50
4   call sym.imp.malloc
5   mov qword [var_8h], rax
6   lea rdi, str.Please_enter_your_name:
7   mov al, 0
```

Traveling to the next `lea rdi` instruction will get us to location `6`.
Now moving 1 instruction will travel to the next expression (`7`).

After traveling, we axtract the value of the second operand - `0`
