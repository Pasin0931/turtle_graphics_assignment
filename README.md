# Turtle Assignment

## Overview
This project generates abstract geometric artwork using Python’s turtle graphics library.classes.  
Users can choose from 9 art styles, each producing randomized patterns made from polygons and nested shapes.
The program is organized using object-oriented programming (OOP) with two main classes: **Brush** and **Painter**.

---

## Project Structure

turtle_graphics_assignment/
pycache/             # Auto-generated Python cache
canvas/              # Store .jpg examples of generated artworks
lib.py               # Stores Brush & Painter classes
main.py              # Main program
README.md            # Documentation
test.py              # Code preview & testing

---

## Design Summary

**Brush** – Handles drawing operations.
- `draw()` – Draws a polygon using the current size, color, location, and orientation. 
- `draw_inside()` – Draws a polygon, then two smaller nested polygons inside it. 
- `setup(speed, bg, tracer, colormode)` – Configures turtle settings (speed, background color, tracer, and color mode).  

**Painter** – Controls randomization, Canvas painting choice, Drawing preperation.
- `painter_choice()` – Asks the user to choose an art mode (1–9).  
- `drawing_prep()` – Generates the first set of random drawing parameters.  
- `gennerate_solcb()` – Generates new random size, orientation, location, color, and border thickness for the next shape.    
- `random_shape()` – Returns a random polygon side count (3–5).
- `random_size()` – Returns a random size (50–150).
- `random_orientation()` – Returns a random angle (0–90°).
- `random_loc()` – Returns a random (x, y) screen location. 
- `random_color()` – Returns a random RGB color (0–255). 
- `random_border()` – Returns a random border thickness (1–10).

---

## How to Run

Run the program in your terminal:

```bash
python main.py
or click the Run ▶️ button in your editor.
```

Choose an art mode (1–9) when prompted.
A Turtle Graphics window will open and generate the artwork.

---

## Status

All features are fully implemented and functioning correctly.
No known bugs.