import numpy as np
from pyscript import Element


# ============================================================
# General settings and random-number helper functions
# ============================================================

NUMBER_OF_QUESTIONS = 11


def random_integer(base_value, minimum_value=None):
    """
    Return an integer within approximately ±20% of base_value.

    Parameters
    ----------
    base_value:
        Center value for the random range.
    minimum_value:
        Optional minimum allowed result.
    """
    lower = int(np.floor(base_value * 0.80))
    upper = int(np.ceil(base_value * 1.20))

    if minimum_value is not None:
        lower = max(lower, minimum_value)

    return int(np.random.randint(lower, upper + 1))


def random_decimal(base_value, decimals=1, minimum_value=None):
    """
    Return a decimal number within approximately ±20% of base_value.
    """
    lower = base_value * 0.80
    upper = base_value * 1.20

    if minimum_value is not None:
        lower = max(lower, minimum_value)

    scale = 10 ** decimals
    lower_scaled = int(np.ceil(lower * scale))
    upper_scaled = int(np.floor(upper * scale))

    return float(
        np.random.randint(lower_scaled, upper_scaled + 1) / scale
    )


def random_signed_integer(base_value):
    """
    Randomize the magnitude of a signed, nonzero integer while
    preserving its sign.
    """
    if base_value == 0:
        return 0

    magnitude = random_integer(abs(base_value), minimum_value=1)

    if base_value < 0:
        return -magnitude

    return magnitude


def random_signed_decimal(base_value, decimals=1):
    """
    Randomize the magnitude of a signed decimal while preserving
    its sign.
    """
    if base_value == 0:
        return 0.0

    magnitude = random_decimal(
        abs(base_value),
        decimals=decimals,
        minimum_value=1 / (10 ** decimals)
    )

    if base_value < 0:
        return -magnitude

    return magnitude


def clean_number(value):
    """
    Format a number for display without unnecessary trailing zeros.
    """
    value = float(value)

    if value.is_integer():
        return str(int(value))

    return f"{value:g}"


def vector_text(vector, units=""):
    """
    Convert a three-dimensional vector into readable i-j-k form.
    """
    labels = ["i", "j", "k"]
    terms = []

    for component, label in zip(vector, labels):
        component = float(component)

        if np.isclose(component, 0.0):
            continue

        magnitude = abs(component)
        magnitude_text = clean_number(magnitude)

        if len(terms) == 0:
            if component < 0:
                terms.append(f"-{magnitude_text}{label}")
            else:
                terms.append(f"{magnitude_text}{label}")
        else:
            if component < 0:
                terms.append(f"- {magnitude_text}{label}")
            else:
                terms.append(f"+ {magnitude_text}{label}")

    if not terms:
        result = "0"
    else:
        result = " ".join(terms)

    if units:
        result += f" {units}"

    return result


# Keep track of answers submitted by the student.
points = [0] * NUMBER_OF_QUESTIONS
submitted = [False] * NUMBER_OF_QUESTIONS


# ============================================================
# Problem 1
# Angular momentum of the satellite system
# ============================================================

# Random masses, generally within ±20% of the original values.
mass_base = random_integer(20, minimum_value=1)
mass_A = random_integer(4, minimum_value=1)
mass_B = random_integer(6, minimum_value=1)
mass_C = random_integer(8, minimum_value=1)

# Random position vectors in meters.
# The signs and general geometry of the original vectors are retained.
r_A = np.array([
    random_signed_integer(2),
    random_signed_integer(-1),
    random_signed_integer(3)
], dtype=float)

r_B = np.array([
    random_signed_integer(-1),
    random_signed_integer(2),
    random_signed_integer(1)
], dtype=float)

r_C = np.array([
    random_signed_integer(3),
    random_signed_integer(1),
    random_signed_integer(-2)
], dtype=float)

# Random velocity vectors in meters per second.
v_A = np.array([
    random_signed_integer(4),
    random_signed_integer(-2),
    random_signed_integer(2)
], dtype=float)

v_B = np.array([
    random_signed_integer(1),
    random_signed_integer(4),
    0
], dtype=float)

v_C = np.array([
    random_signed_integer(2),
    random_signed_integer(2),
    random_signed_integer(4)
], dtype=float)

# Angular momentum about the base satellite:
#
# H_O = sum(r × mv)
#
# The base satellite is located at O, so it has zero angular
# momentum about O at the instant considered.
H_A = np.cross(r_A, mass_A * v_A)
H_B = np.cross(r_B, mass_B * v_B)
H_C = np.cross(r_C, mass_C * v_C)

H_O_problem1 = H_A + H_B + H_C

answer1 = round(float(H_O_problem1[0]))
answer2 = round(float(H_O_problem1[1]))
answer3 = round(float(H_O_problem1[2]))


# ============================================================
# Problem 2
# Angular momentum of three identical particles
# ============================================================

g_english = 32.2  # ft/s²; physical conversion constant

# Random particle weight and angular momentum magnitude.
particle_weight = random_decimal(
    19.32,
    decimals=2,
    minimum_value=1.0
)

particle_mass = particle_weight / g_english

H_O_magnitude = random_decimal(
    1.2,
    decimals=2,
    minimum_value=0.1
)

H_required = np.array([
    0.0,
    0.0,
    H_O_magnitude
])

unit_i = np.array([1.0, 0.0, 0.0])
unit_j = np.array([0.0, 1.0, 0.0])
unit_k = np.array([0.0, 0.0, 1.0])


def generate_problem2_data():
    """
    Generate randomized position vectors and solve for the three
    particle velocities.

    Values are regenerated if the resulting coefficient matrix is
    singular, nearly singular, or produces excessively large speeds.
    """
    while True:
        # Position-vector components in feet, randomized by about ±20%.
        x_A = random_decimal(2.0, decimals=1, minimum_value=0.1)
        z_A = random_decimal(1.0, decimals=1, minimum_value=0.1)

        y_B = random_decimal(2.0, decimals=1, minimum_value=0.1)
        z_B = random_decimal(1.5, decimals=1, minimum_value=0.1)

        x_C = random_decimal(1.0, decimals=1, minimum_value=0.1)
        y_C = random_decimal(1.0, decimals=1, minimum_value=0.1)

        position_A = np.array([x_A, 0.0, z_A])
        position_B = np.array([0.0, y_B, z_B])
        position_C = np.array([x_C, y_C, 0.0])

        # Velocity directions:
        # v_A = velocity_A*j
        # v_B = velocity_B*i
        # v_C = velocity_C*k
        column_A = np.cross(
            position_A,
            particle_mass * unit_j
        )

        column_B = np.cross(
            position_B,
            particle_mass * unit_i
        )

        column_C = np.cross(
            position_C,
            particle_mass * unit_k
        )

        coefficient_matrix = np.column_stack(
            (column_A, column_B, column_C)
        )

        determinant = np.linalg.det(coefficient_matrix)

        if abs(determinant) < 1.0e-5:
            continue

        velocities = np.linalg.solve(
            coefficient_matrix,
            H_required
        )

        # Avoid nearly zero or unreasonable generated answers.
        if np.any(np.abs(velocities) < 0.05):
            continue

        if np.any(np.abs(velocities) > 100.0):
            continue

        return (
            position_A,
            position_B,
            position_C,
            velocities
        )


r_2A, r_2B, r_2C, problem2_velocities = generate_problem2_data()

velocity_A = float(problem2_velocities[0])
velocity_B = float(problem2_velocities[1])
velocity_C = float(problem2_velocities[2])

v_2A = velocity_A * unit_j
v_2B = velocity_B * unit_i
v_2C = velocity_C * unit_k

answer4 = round(velocity_A, 1)
answer5 = round(velocity_B, 1)
answer6 = round(velocity_C, 1)

# Since all three particles have identical masses, their mass-center
# position is the arithmetic average of their position vectors.
r_G = (r_2A + r_2B + r_2C) / 3.0

# Angular momentum about the mass center G.
H_G = (
    np.cross(r_2A - r_G, particle_mass * v_2A)
    + np.cross(r_2B - r_G, particle_mass * v_2B)
    + np.cross(r_2C - r_G, particle_mass * v_2C)
)

answer7 = round(float(H_G[0]), 1)
answer8 = round(float(H_G[1]), 1)
answer9 = round(float(H_G[2]), 1)


# ============================================================
# Problem 3
# Motion of the mass center of the three-car system
# ============================================================

# Car weights are randomized in increments of 100 lb.
weight_car_A = 100 * random_integer(30, minimum_value=1)
weight_car_B = 100 * random_integer(26, minimum_value=1)
weight_car_C = 100 * random_integer(24, minimum_value=1)

# Car speeds are randomized within approximately ±20%.
speed_car_A_mph = random_integer(75, minimum_value=1)
speed_car_B_mph = random_integer(45, minimum_value=1)
speed_car_C_mph = random_integer(60, minimum_value=1)

# Random initial coordinates of car C.
car_C_initial_x = random_integer(32, minimum_value=1)
car_C_initial_y = random_integer(10, minimum_value=1)

# Random elapsed time to the nearest tenth of a second.
elapsed_time = random_decimal(
    2.4,
    decimals=1,
    minimum_value=0.1
)

# Initial car positions in feet.
r_car_A_initial = np.array([0.0, 0.0])
r_car_B_initial = np.array([0.0, 0.0])
r_car_C_initial = np.array([
    float(car_C_initial_x),
    float(car_C_initial_y)
])

# Conversion from mi/h to ft/s.
mph_to_fts = 5280.0 / 3600.0

speed_car_A = speed_car_A_mph * mph_to_fts
speed_car_B = speed_car_B_mph * mph_to_fts
speed_car_C = speed_car_C_mph * mph_to_fts

# Positive x is east and positive y is north.
v_car_A = np.array([
    speed_car_A,
    0.0
])

v_car_B = np.array([
    0.0,
    speed_car_B
])

v_car_C = np.array([
    -speed_car_C,
    0.0
])

total_weight = (
    weight_car_A
    + weight_car_B
    + weight_car_C
)

# Because all masses contain the common factor 1/g, weights may be
# used directly when calculating the mass-center position.
r_G_initial = (
    weight_car_A * r_car_A_initial
    + weight_car_B * r_car_B_initial
    + weight_car_C * r_car_C_initial
) / total_weight

# With horizontal pavement forces neglected, the horizontal velocity
# of the system's mass center remains constant.
v_G_cars = (
    weight_car_A * v_car_A
    + weight_car_B * v_car_B
    + weight_car_C * v_car_C
) / total_weight

# When all cars are together at pole P, their common position is also
# the position of the system's mass center.
r_P = r_G_initial + v_G_cars * elapsed_time

answer10 = round(float(r_P[0]), 1)
answer11 = round(float(r_P[1]), 1)


# ============================================================
# Write randomized questions to the HTML page
# ============================================================

Element("Q1a").write(
    f"1 a) A {mass_base} kg base satellite deploys three "
    f"sub-satellites A, B, and C having masses {mass_A} kg, "
    f"{mass_B} kg, and {mass_C} kg, respectively. Their position "
    f"vectors from the base satellite are "
    f"r_A = {vector_text(r_A, 'm')}, "
    f"r_B = {vector_text(r_B, 'm')}, and "
    f"r_C = {vector_text(r_C, 'm')}. "
    f"Their velocities are "
    f"v_A = {vector_text(v_A, 'm/s')}, "
    f"v_B = {vector_text(v_B, 'm/s')}, and "
    f"v_C = {vector_text(v_C, 'm/s')}. "
    f"At the instant shown, calculate the i-component of the "
    f"angular momentum H_O [kg·m²/s] of the system about the base "
    f"satellite. Round to the nearest integer."
)

Element("Q1b").write(
    f"1 b) Using the satellite masses, position vectors, and "
    f"velocities given in part 1 a, calculate the j-component of "
    f"the angular momentum H_O [kg·m²/s] of the system about the "
    f"base satellite. Round to the nearest integer."
)

Element("Q1c").write(
    f"1 c) Using the satellite masses, position vectors, and "
    f"velocities given in part 1 a, calculate the k-component of "
    f"the angular momentum H_O [kg·m²/s] of the system about the "
    f"base satellite. Round to the nearest integer."
)

Element("Q2a").write(
    f"2 a) A system consists of three identical "
    f"{clean_number(particle_weight)}-lb particles A, B, and C. "
    f"Their position vectors are "
    f"r_A = {vector_text(r_2A, 'ft')}, "
    f"r_B = {vector_text(r_2B, 'ft')}, and "
    f"r_C = {vector_text(r_2C, 'ft')}. "
    f"The velocities of the particles are "
    f"v_A = v_A j, v_B = v_B i, and v_C = v_C k. "
    f"Knowing that the angular momentum of the system about O is "
    f"H_O = {clean_number(H_O_magnitude)}k ft·lb·s, determine "
    f"the velocity v_A [ft/s]. Round to the nearest tenth."
)

Element("Q2b").write(
    f"2 b) For the system of three identical "
    f"{clean_number(particle_weight)}-lb particles described in "
    f"part 2 a, determine the velocity v_B [ft/s]. "
    f"Round to the nearest tenth."
)

Element("Q2c").write(
    f"2 c) For the system of three identical "
    f"{clean_number(particle_weight)}-lb particles described in "
    f"part 2 a, determine the velocity v_C [ft/s]. "
    f"Round to the nearest tenth."
)

# The following paragraph IDs match the corrected hw8.html.
Element("Q3a").write(
    f"2 d) For the particle system described in part 2 a, calculate "
    f"the x-component of the angular momentum about the system's "
    f"mass center G [ft·lb·s]. Round to the nearest tenth."
)

Element("Q3b").write(
    f"2 e) For the particle system described in part 2 a, calculate "
    f"the y-component of the angular momentum about the system's "
    f"mass center G [ft·lb·s]. Round to the nearest tenth."
)

Element("Q3c").write(
    f"2 f) For the particle system described in part 2 a, calculate "
    f"the z-component of the angular momentum about the system's "
    f"mass center G [ft·lb·s]. Round to the nearest tenth."
)

Element("Q3d").write(
    f"3 a) Car A was traveling east at "
    f"{speed_car_A_mph} mi/h when it collided at point O with "
    f"car B, which was traveling north at "
    f"{speed_car_B_mph} mi/h. Car C, which was traveling west at "
    f"{speed_car_C_mph} mi/h, was {car_C_initial_x} ft east and "
    f"{car_C_initial_y} ft north of point O at the time of the "
    f"collision. The weights of cars A, B, and C are "
    f"{weight_car_A} lb, {weight_car_B} lb, and "
    f"{weight_car_C} lb, respectively. The cars eventually become "
    f"stuck together and reach utility pole P "
    f"{clean_number(elapsed_time)} s after the first collision. "
    f"Neglect the horizontal forces exerted on the cars by the wet "
    f"pavement. Determine the x-coordinate of utility pole P [ft]. "
    f"Round to the nearest tenth."
)

Element("Q4a").write(
    f"3 b) For the cars described in part 3 a, determine the "
    f"y-coordinate of utility pole P [ft]. "
    f"Round to the nearest tenth."
)


# ============================================================
# Connect to the HTML input and output elements
# ============================================================

inputs = [
    Element("Question1"),
    Element("Question2"),
    Element("Question3"),
    Element("Question4"),
    Element("Question5"),
    Element("Question6"),
    Element("Question7"),
    Element("Question8"),
    Element("Question9"),
    Element("Question10"),
    Element("Question11")
]

outputs = [
    Element("outputDiv1"),
    Element("outputDiv2"),
    Element("outputDiv3"),
    Element("outputDiv4"),
    Element("outputDiv5"),
    Element("outputDiv6"),
    Element("outputDiv7"),
    Element("outputDiv8"),
    Element("outputDiv9"),
    Element("outputDiv10"),
    Element("outputDiv11")
]

answers = [
    answer1,
    answer2,
    answer3,
    answer4,
    answer5,
    answer6,
    answer7,
    answer8,
    answer9,
    answer10,
    answer11
]


# ============================================================
# Answer checking
# ============================================================

def check_answer(question_index):
    """
    Check one submitted answer and update the student's score.
    """
    entered_text = inputs[question_index].value.strip()
    output = outputs[question_index]
    correct_answer = float(answers[question_index])

    if entered_text == "":
        output.write(
            "Blank value provided, please try again."
        )
        points[question_index] = 0
        submitted[question_index] = False
        return

    try:
        entered_answer = float(entered_text)
    except ValueError:
        output.write(
            f"You typed in {entered_text}. "
            f"Please enter a numeric value."
        )
        points[question_index] = 0
        submitted[question_index] = True
        return

    submitted[question_index] = True

    # This accepts numerically equivalent entries such as
    # 2, 2.0, and 2.00.
    if np.isclose(
        entered_answer,
        correct_answer,
        rtol=0.0,
        atol=1.0e-9
    ):
        output.write("Correct!")
        points[question_index] = 1
    else:
        output.write(
            f"You typed in {entered_text}; that is not correct."
        )
        points[question_index] = 0


# ============================================================
# Individual submit-button functions
# ============================================================

def print_num1(*args, **kwargs):
    check_answer(0)


def print_num2(*args, **kwargs):
    check_answer(1)


def print_num3(*args, **kwargs):
    check_answer(2)


def print_num4(*args, **kwargs):
    check_answer(3)


def print_num5(*args, **kwargs):
    check_answer(4)


def print_num6(*args, **kwargs):
    check_answer(5)


def print_num7(*args, **kwargs):
    check_answer(6)


def print_num8(*args, **kwargs):
    check_answer(7)


def print_num9(*args, **kwargs):
    check_answer(8)


def print_num10(*args, **kwargs):
    check_answer(9)


def print_num11(*args, **kwargs):
    check_answer(10)


# ============================================================
# Clear and final-submission functions
# ============================================================

def clear(*args, **kwargs):
    """
    Clear all answer fields, feedback, and recorded scores.
    """
    for input_element in inputs:
        input_element.element.value = ""

    for output in outputs:
        output.clear()

    Element("outputFinal").clear()

    for index in range(NUMBER_OF_QUESTIONS):
        points[index] = 0
        submitted[index] = False


def final_sub(*args, **kwargs):
    """
    Verify that every answer has been submitted, then display the
    student's final grade.
    """
    name = Element("student-name").value.strip()
    out_final = Element("outputFinal")

    if name == "":
        out_final.write(
            "Please enter your name before submitting your answers."
        )
        return

    unanswered_questions = [
        str(index + 1)
        for index in range(NUMBER_OF_QUESTIONS)
        if not submitted[index]
    ]

    if unanswered_questions:
        out_final.write(
            "You have not submitted all questions. "
            "Please submit question(s): "
            + ", ".join(unanswered_questions)
            + "."
        )
        return

    grade = round(
        (sum(points) / NUMBER_OF_QUESTIONS) * 100.0,
        1
    )

    out_final.write(
        f"Thank you {name}, your answers have been submitted. "
        f"Your score is: {grade}%"
    )