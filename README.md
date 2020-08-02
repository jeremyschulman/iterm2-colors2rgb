# Convert iTerm2 profile colors to RGB dataset

As a user of iTerm2 and a developer that wants to use python packages supporting colorization 
such as [Rich](), I want to extract the colors from my iTerm2 Profile into an RGB dataset 
that provides:

   * Background (R,G,B)
   * Foreground (R,G,B)
   * List of 8 "normal" colors of (R, G, B)
   * List of 8 "bright" colors of (R, G, B)
   
# Usage

You will first need to export your profile colors from iTerm, as described in the section
below. You can then either use this package directly or programaticaly.

**direct module**<br/>
Consider an iTerm profile with color values that look like this in the app:

![colors in iTerm](https://github.com/jeremyschulman/iterm2-colors2rgb/blob/master/iterm2-profile-colors.png)


After exporting these settings to the default filename "Untitled.itemcolors",
run python:

```
python -m iterm2_colors2rgb Untitled.itermcolors
```   

Outputs (formatted for clarity):
````
(
   (0, 0, 0), 
   (199, 199, 199), 
   [(0, 0, 0), (201, 27, 0), (0, 194, 0), (199, 196, 0), (2, 37, 199), (202, 48, 199), (0, 197, 199), (199, 199, 199), (104, 104, 104)], 
   [(255, 110, 103), (95, 250, 104), (255, 252, 103), (104, 113, 255), (255, 119, 255), (96, 253, 255), (255, 255, 255)]
)
````

**programmatic**<br/>

```python
from iterm2_colors2rgb import iterm2_colors2rgb

# as a tuple (bg, fb, normal_list, bright_list)
colors = iterm2_colors2rgb("Untitled.itermcolors")
```

# Installation
```
pip install iterm2-colors2rgb
```  

# Exporting Profile Colors from iTerm

![export steps](https://github.com/jeremyschulman/iterm2-colors2rgb/blob/master/export-steps.png)

Steps:

  1. Open the iTerm2 app settings
  2. Select the Prefrences option
  3. Select the Profiles option
  4. Select the profile that you want to export
  5. Click the _Color Presents ..._ dropdown to reveal the Export option
  6. Click the Export option
  
You will then be presented with a Save File diaglog box which allows you to
choose the name and location where you want to save your settings.


# Usage with Rich TerminalTheme

If you are using the Rich package and you want to save your console output to file with thes colors you can

```python
from rich.console import TerminalTheme, Console

HTML_SAVE_THEME = TerminalTheme(
    (0, 0, 0),
    (199, 199, 199),
    [(0, 0, 0),
     (201, 27, 0),
     (0, 194, 0),
     (199, 196, 0),
     (2, 37, 199),
     (202, 48, 199),
     (0, 197, 199),
     (199, 199, 199),
     (104, 104, 104)],
    [(255, 110, 103),
     (95, 250, 104),
     (255, 252, 103),
     (104, 113, 255),
     (255, 119, 255),
     (96, 253, 255),
     (255, 255, 255)]
)

# create the Console instance with `record=True` to use the save methods
console = Console(record=True)

# ... console.print(...) usage to render text to screen

# now save the console output to an HTML file using the color theme
console.save_html('mytabledata.html', theme=HTML_SAVE_THEME)
```