import pyray as rl
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450
MAX_COLUMNS = 20

# Initialize window
rl.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "pyray [core] example - 3D camera first person")

# Define the camera
camera = rl.Camera3D()
camera.position = rl.Vector3(0.0, 2.0, 4.0)
camera.target = rl.Vector3(0.0, 2.0, 0.0)
camera.up = rl.Vector3(0.0, 1.0, 0.0)
camera.fovy = 60.0
camera.projection = rl.CAMERA_PERSPECTIVE

camera_mode = rl.CAMERA_FIRST_PERSON

# Generate some random columns
heights = [random.uniform(1, 12) for _ in range(MAX_COLUMNS)]
positions = [
    rl.Vector3(random.uniform(-15, 15), heights[i] / 2.0, random.uniform(-15, 15))
    for i in range(MAX_COLUMNS)
]
colors = [
    rl.Color(random.randint(20, 255), random.randint(10, 55), 30, 255)
    for _ in range(MAX_COLUMNS)
]

rl.disable_cursor()
rl.set_target_fps(60)

while not rl.window_should_close():
    # Update camera mode
    if rl.is_key_pressed(rl.KEY_ONE):
        camera_mode = rl.CAMERA_FREE
    if rl.is_key_pressed(rl.KEY_TWO):
        camera_mode = rl.CAMERA_FIRST_PERSON
    if rl.is_key_pressed(rl.KEY_THREE):
        camera_mode = rl.CAMERA_THIRD_PERSON
    if rl.is_key_pressed(rl.KEY_FOUR):
        camera_mode = rl.CAMERA_ORBITAL

    rl.update_camera(camera, camera_mode)

    # Draw scene
    rl.begin_drawing()
    rl.clear_background(rl.RAYWHITE)
    rl.begin_mode3d(camera)

    rl.draw_plane(rl.Vector3(0.0, 0.0, 0.0), rl.Vector2(32.0, 32.0), rl.LIGHTGRAY)
    rl.draw_cube(rl.Vector3(-16.0, 2.5, 0.0), 1.0, 5.0, 32.0, rl.BLUE)
    rl.draw_cube(rl.Vector3(16.0, 2.5, 0.0), 1.0, 5.0, 32.0, rl.LIME)
    rl.draw_cube(rl.Vector3(0.0, 2.5, 16.0), 32.0, 5.0, 1.0, rl.GOLD)

    for i in range(MAX_COLUMNS):
        rl.draw_cube(positions[i], 2.0, heights[i], 2.0, colors[i])
        rl.draw_cube_wires(positions[i], 2.0, heights[i], 2.0, rl.MAROON)

    if camera_mode == rl.CAMERA_THIRD_PERSON:
        rl.draw_cube(camera.target, 0.5, 0.5, 0.5, rl.PURPLE)
        rl.draw_cube_wires(camera.target, 0.5, 0.5, 0.5, rl.DARKPURPLE)

    rl.end_mode3d()

    rl.draw_text("Camera controls: W, A, S, D, Space, Ctrl", 15, 30, 10, rl.BLACK)
    rl.draw_text("Modes: 1-Free, 2-First Person, 3-Third Person, 4-Orbital", 15, 45, 10, rl.BLACK)
    rl.draw_text(f"Mode: {camera_mode}", 15, 75, 10, rl.BLACK)
    rl.end_drawing()

rl.close_window()


