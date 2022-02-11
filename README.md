# flex-aliases

It is a repository to facilitate quick styling by providing extremelly small shortcuts for complex and repeatable flexbox blocks.

If you want some html element to be:
```css
display: flex;
align-items: center;
justify-content: center;
flex-direction: column-reverse;
```

Just add the class _fccc_ to that element, the _f_ means that it is _display: flex_, the first _c_ is _align-items: center_ and so on...

### All the possible combinations are:

- First char must always be "f".
- Second can be: "c" for center, "e" for flex-end and "s" for flex-start.
- Third can be: "a" for space-around, "b" for space-between, "e" for space-evenly, "c" for center, "e" for flex-end, and "s" for flex-start.
- Fourth/Fifth can be: "c" for column, "cr" for column-reverse, "r" for row and "rr" for row_reverse.

At any position you can also insert a "0", meaning that it will ignore that property.

For example:
```css
.f0bc {
  display: flex;
  justify-content: space-between;
  flex-direction: column;
}
```
Ignores the align-items property.

### How to install

Just import the css file into your html file:
```html
<link rel="stylesheet" href="flexAliases.css">
```

### How to improve/change

Simply edit the _main.py_ file and run:
```python
python3 main.py
```
To generate the css file.
