from random import randint
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm

# ------------------------------
# ایجاد ماتریس با حاشیه صفر
# ------------------------------
matrix = [[0] * 12 for _ in range(12)]

for i in range(1, 11):
    for j in range(1, 11):
        matrix[i][j] = randint(0, 1)

print("Initial Matrix:")
for i in range(1, 11):
    for j in range(1, 11):
        print(matrix[i][j], end="  ")
    print()

# ------------------------------
# ورود اطلاعات موش و پنیر
# ------------------------------
mouse_row = int(input("\nEnter mouse row (1-10): "))
mouse_col = int(input("Enter mouse col (1-10): "))

cheese_row = int(input("Enter cheese row (1-10): "))
cheese_col = int(input("Enter cheese col (1-10): "))

if matrix[mouse_row][mouse_col] != 1:
    print("Error: Mouse is on a wall! (Cell value must be 1)")
    exit()

if matrix[cheese_row][cheese_col] != 1:
    print("Error: Cheese is on a wall! (Cell value must be 1)")
    exit()

# ------------------------------
# جهت‌های حرکت (۸ جهت)
# ------------------------------
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

path = [(mouse_row, mouse_col)]


# ------------------------------
# تابع بازگشتی مسیر‌یابی
# ------------------------------
def find_path(current_row, current_col, cheese_row, cheese_col):
    if current_row == cheese_row and current_col == cheese_col:
        return True

    matrix[current_row][current_col] = 2  # علامت بازدید

    for dr, dc in directions:
        new_row, new_col = current_row + dr, current_col + dc
        if 1 <= new_row <= 10 and 1 <= new_col <= 10:
            if matrix[new_row][new_col] == 1:
                print(f"Moving to: ({new_row}, {new_col})")

                path.append((new_row, new_col))
                if find_path(new_row, new_col, cheese_row, cheese_col):
                    return True
                path.pop()

    return False


# ------------------------------
# اجرای الگوریتم
# ------------------------------
print("\nSearching for path...")
result = find_path(mouse_row, mouse_col, cheese_row, cheese_col)

if result:
    print("\nCheese found!")
else:
    print("\nNo path found!")

print("\nFinal Matrix (2 = visited cells):")
for i in range(1, 11):
    for j in range(1, 11):
        print(matrix[i][j], end="  ")
    print()

# ------------------------------
# بخش گرافیکی حرفه‌ای‌تر
# ------------------------------

plt.style.use("seaborn-v0_8-whitegrid")

fig, ax = plt.subplots(figsize=(7, 7))
fig.patch.set_facecolor("#fafcff")
ax.set_facecolor("#f3f6fa")

# تعریف رنگ‌ها: [دیوار، مسیرآزاد، بازدیدشده]
cmap = ListedColormap(["#454545", "#ffffff", "#ffe671"])
norm = BoundaryNorm([0, 1, 2, 3], cmap.N)

# نمایش ماز
maze_square = np.array(matrix)
plot = ax.imshow(maze_square, cmap=cmap, norm=norm, origin="upper")

# grid خطوط
ax.set_xticks(np.arange(-0.5, 11.5, 1), minor=True)
ax.set_yticks(np.arange(-0.5, 11.5, 1), minor=True)
ax.grid(which="minor", color="#bdbdbd", linestyle="--", linewidth=0.5)
ax.tick_params(
    which="both", left=False, bottom=False, labelleft=False, labelbottom=False
)

# مسیر پیدا شده
if result and len(path) > 1:
    path_x = [x for (_, x) in path]
    path_y = [y for (y, _) in path]
    ax.plot(
        path_x,
        path_y,
        color="#47d147",
        linewidth=3,
        marker="o",
        markersize=7,
        markerfacecolor="#47d147",
        markeredgewidth=0.5,
        alpha=0.85,
        label="Path",
    )

# نمایش موش و پنیر
mouse_marker = ax.scatter(
    [mouse_col],
    [mouse_row],
    marker="o",
    s=300,
    c="#3498db",
    edgecolors="white",
    linewidths=2,
    label="Mouse",
    zorder=5,
)
cheese_marker = ax.scatter(
    [cheese_col],
    [cheese_row],
    marker="*",
    s=350,
    c="#ffd700",
    edgecolors="#c9ac01",
    linewidths=1.3,
    label="Cheese",
    zorder=6,
)

# برچسب START/GOAL برای تجربه بهتر
ax.text(
    mouse_col,
    mouse_row - 0.35,
    "START",
    color="#25507a",
    fontsize=13,
    ha="center",
    va="center",
    fontweight="bold",
)
ax.text(
    cheese_col,
    cheese_row + 0.35,
    "GOAL",
    color="#c19400",
    fontsize=13,
    ha="center",
    va="center",
    fontweight="bold",
)

# legend حرفه‌ای‌تر
handles = [
    plt.Line2D([0], [0], color="#47d147", lw=3, label="Path"),
    plt.Line2D(
        [0],
        [0],
        marker="o",
        markersize=12,
        color="w",
        markerfacecolor="#3498db",
        markeredgecolor="white",
        label="Mouse",
        lw=0,
    ),
    plt.Line2D(
        [0],
        [0],
        marker="*",
        markersize=18,
        color="w",
        markerfacecolor="#ffd700",
        markeredgecolor="#c9ac01",
        label="Cheese",
        lw=0,
    ),
    plt.Rectangle((0, 0), 1, 1, color="#454545", label="Wall", ec="none"),
    plt.Rectangle((0, 0), 1, 1, color="#ffe671", label="Visited", ec="none"),
]
ax.legend(handles=handles, loc="upper right", fontsize=12, frameon=False)

ax.set_title(
    "Maze Path Visualization", fontsize=18, fontweight="bold", pad=12, color="#343a40"
)
plt.tight_layout()
plt.show()
