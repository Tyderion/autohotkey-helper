# Compiler for anonymous functions in Autohotkey

## Syntax

The Content in an .ahkp file
```
TestFunction2()
{
  name := reduce(["one", "two", "three"],anon(acc, val, delimiter){
    return acc . "blablabal" .  val
    }, ";")
  MsgBox % name
}
```

compiles to this in the main ahk
```
TestFunction2()
{
  name := reduce(["one", "two", "three"],"531ab339cc324e2e8791685978a89024", ";")
  MsgBox % name
}

```
and this in an included ahk
```
531ab339cc324e2e8791685978a89024(acc, val, delimiter){
    return acc . "blablabal" .  val
    }

```
with randomely generated function names.
