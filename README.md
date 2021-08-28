**Pixl-Engine** is an object-oriented wrap around the [DearPyGui](https://github.com/hoffstadt/DearPyGui) graphical interface framework. The API is aimed at making things like application management, adding event handlers, and theming more pythonic.

Documentation, examples, etc will be added periodically. The source code has many comments and docstrings, and it is encouraged to read through them. MOST of the [DearPyGui documentation](https://github.com/hoffstadt/DearPyGui/wiki) will also apply here.


## Example
```python
from pixle import Application
from pixle.containers import Window
from pixle.widgets import Text

app = Application()
app.title = "ExampleApp"

with Window("Window1") as window1:
    ...

@app.on_resize
def on_app_resize():
    Text(f"{app.title} resized!", parent=window1)

@window1.on_resize
def on_window1_resize():
    Text(f"{window1.label} resized!", parent=window1)

app.start()
```

## Installation
**Pixl-Engine** is available [here](https://test.pypi.org/project/pixlengine/) on **testpypi**.

```
python -m pip install -i https://test.pypi.org/simple/ pixlengine
```


## License
Pixl-Engine and DearPyGui are both licensed under the [MIT License](https://github.com/Atlamillias/DPG-Widgets/blob/main/LICENSE).