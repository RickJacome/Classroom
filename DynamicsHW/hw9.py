import numpy as np
from pyscript import Element


# ============================================================
# General settings
# ============================================================

NUMBER_OF_QUESTIONS = 10
G_ENGLISH = 32.2  # ft/s^2

# Track the student's score and whether each question was submitted.
points = [0] * NUMBER_OF_QUESTIONS
submitted = [False] * NUMBER_OF_QUESTIONS


# ============================================================
# Random-number helper functions
# ============================================================

def random_integer(base_value, minimum_value=1):
    """
    Generate an integer approximately within ±20% of base_value.
    """
    lower = int(np.floor(base_value * 0.80))
    upper = int(np.ceil(base_value * 1.20))

    lower = max(lower, minimum_value)

    return int(np.random.randint(lower, upper + 1))


def random_decimal(base_value, decimals=1, minimum_value=0.1):
    """
    Generate a decimal approximately within ±20% of base_value.
    """
    scale = 10 ** decimals

    lower = int(np.ceil(base_value * 0.80 * scale))
    upper = int(np.floor(base_value * 1.20 * scale))

    lower = max(lower, int(np.ceil(minimum_value * scale)))

    return float(np.random.randint(lower, upper + 1) / scale)


def random_angle(base_angle):
    """
    Generate an integer angle approximately within ±20% of the
    magnitude of base_angle while preserving its general sign.
    """
    if base_angle == 0:
        return 0

    magnitude = abs(base_angle)

    lower = int(np.floor(magnitude * 0.80))
    upper = int(np.ceil(magnitude * 1.20))

    generated_angle = int(np.random.randint(lower, upper + 1))

    if base_angle < 0:
        return -generated_angle

    return generated_angle


def clean_number(value):
    """
    Format a number without unnecessary trailing zeros.
    """
    value = float(value)

    if value.is_integer():
        return str(int(value))

    return f"{value:g}"


def direction_description(angle):
    """
    Return a readable description of an angle measured from the
    positive x-axis.
    """
    if angle > 0:
        return (
            f"{clean_number(angle)}° counterclockwise from the "
            f"positive x-axis"
        )

    if angle < 0:
        return (
            f"{clean_number(abs(angle))}° clockwise from the "
            f"positive x-axis"
        )

    return "along the positive x-axis"


# ============================================================
# Problem 1
# Block sliding on a freely moving wedge
# ============================================================

# Randomized values based on the original 15-lb block,
# 25-lb wedge, and 3-ft sliding distance.
weight_block_1 = random_integer(15, minimum_value=5)
weight_wedge_1 = random_integer(25, minimum_value=5)
slide_distance_1 = random_decimal(
    3.0,
    decimals=1,
    minimum_value=1.0
)

# The original question referred to a missing diagram. An angle is
# explicitly generated and included so the problem is self-contained.
wedge_angle_1 = random_integer(30, minimum_value=10)
theta_1 = np.radians(wedge_angle_1)

# Let u be the velocity of block B relative to wedge A.
#
# Horizontal momentum:
#
# (W_A/g)V_A + (W_B/g)(V_A + u cos(theta)) = 0
#
# Therefore:
#
# V_A = -W_B/(W_A + W_B) * u cos(theta)
#
# Conservation of energy gives:
#
# W_B*s*sin(theta)
#   = (1/2g)[W_A*V_A^2 + W_B*v_B^2]
#
# Solving for u:
effective_weight_1 = weight_block_1 * (
    1.0
    - (
        weight_block_1
        / (weight_wedge_1 + weight_block_1)
    ) * np.cos(theta_1) ** 2
)

relative_velocity_1 = np.sqrt(
    (
        2.0
        * G_ENGLISH
        * weight_block_1
        * slide_distance_1
        * np.sin(theta_1)
    )
    / effective_weight_1
)

wedge_velocity_1 = (
    weight_block_1
    / (weight_wedge_1 + weight_block_1)
) * relative_velocity_1 * np.cos(theta_1)

answer1 = round(float(relative_velocity_1), 1)
answer2 = round(float(wedge_velocity_1), 1)


# ============================================================
# Problem 2
# Pendulum attached to a freely rolling cart
# ============================================================

weight_block_2 = random_integer(40, minimum_value=10)
weight_cart_2 = random_integer(60, minimum_value=10)
cord_length_2 = random_decimal(
    6.0,
    decimals=1,
    minimum_value=2.0
)

# The initial cord angle was provided by a missing diagram in the
# original assignment. It is included explicitly here.
initial_angle_2 = random_integer(45, minimum_value=15)
theta_2 = np.radians(initial_angle_2)

# Vertical drop of block B.
vertical_drop_2 = cord_length_2 * (
    1.0 - np.cos(theta_2)
)

# At the bottom, let u be B's velocity relative to the cart.
#
# Horizontal momentum:
#
# W_A*v_A + W_B*v_B = 0
#
# and
#
# v_B - v_A = u
#
# Conservation of energy gives:
#
# u^2 = 2*g*h*(W_A + W_B)/W_A
relative_velocity_2 = np.sqrt(
    2.0
    * G_ENGLISH
    * vertical_drop_2
    * (weight_cart_2 + weight_block_2)
    / weight_cart_2
)

cart_velocity_2 = (
    weight_block_2
    / (weight_cart_2 + weight_block_2)
) * relative_velocity_2

block_velocity_2 = (
    weight_cart_2
    / (weight_cart_2 + weight_block_2)
) * relative_velocity_2

answer3 = round(float(cart_velocity_2), 1)
answer4 = round(float(block_velocity_2), 1)


# ============================================================
# Pool-ball collision generator
# ============================================================

def solve_pool_collision(initial_speed, angles_degrees):
    """
    Solve for the three outgoing ball speeds.

    All three balls have identical masses. Ball A initially travels
    along the positive x-axis, while balls B and C are initially at
    rest.

    The outgoing directions are specified by angles measured from
    the positive x-axis.

    The equations are:

        U @ speeds = [initial_speed, 0]

    and

        speed_A^2 + speed_B^2 + speed_C^2 = initial_speed^2

    Linear momentum provides two equations. Conservation of kinetic
    energy provides the third equation.
    """
    angles_radians = np.radians(
        np.array(angles_degrees, dtype=float)
    )

    direction_matrix = np.array([
        np.cos(angles_radians),
        np.sin(angles_radians)
    ])

    initial_momentum_per_unit_mass = np.array([
        float(initial_speed),
        0.0
    ])

    # Minimum-norm solution of the two momentum equations.
    minimum_solution = (
        direction_matrix.T
        @ np.linalg.solve(
            direction_matrix @ direction_matrix.T,
            initial_momentum_per_unit_mass
        )
    )

    # A vector in the null space of the 2-by-3 direction matrix.
    null_vector = np.cross(
        direction_matrix[0],
        direction_matrix[1]
    )

    null_norm_squared = float(
        np.dot(null_vector, null_vector)
    )

    if null_norm_squared < 1.0e-10:
        return None

    remaining_energy = (
        initial_speed ** 2
        - float(np.dot(minimum_solution, minimum_solution))
    )

    if remaining_energy <= 0:
        return None

    root_size = np.sqrt(
        remaining_energy / null_norm_squared
    )

    candidate_1 = minimum_solution + root_size * null_vector
    candidate_2 = minimum_solution - root_size * null_vector

    candidates = [candidate_1, candidate_2]

    for candidate in candidates:
        # Every requested result should represent motion in the
        # stated outgoing direction, so each speed must be positive.
        if np.all(candidate > 0.25):
            return candidate

    return None


def generate_pool_problem(base_angles):
    """
    Generate randomized incoming speed and outgoing directions for
    a physically valid elastic three-ball collision.
    """
    for attempt in range(2000):
        initial_speed = random_integer(15, minimum_value=5)

        generated_angles = [
            random_angle(base_angles[0]),
            random_angle(base_angles[1]),
            random_angle(base_angles[2])
        ]

        speeds = solve_pool_collision(
            initial_speed,
            generated_angles
        )

        if speeds is None:
            continue

        # Avoid generated cases with excessively large or nearly
        # stationary outgoing speeds.
        if np.any(speeds > 2.0 * initial_speed):
            continue

        return (
            initial_speed,
            generated_angles,
            speeds
        )

    # A safe fallback in the unlikely event random generation does
    # not produce a suitable case.
    fallback_speed = 15
    fallback_angles = list(base_angles)
    fallback_speeds = solve_pool_collision(
        fallback_speed,
        fallback_angles
    )

    if fallback_speeds is None:
        raise ValueError(
            "Unable to generate a valid pool-ball collision."
        )

    return (
        fallback_speed,
        fallback_angles,
        fallback_speeds
    )


# ============================================================
# Problem 3
# First three-ball elastic collision
# ============================================================

# The outgoing direction angles are randomized around a valid
# representative collision configuration.
(
    initial_speed_3,
    outgoing_angles_3,
    outgoing_speeds_3
) = generate_pool_problem([18, 106, -55])

angle_A_3 = outgoing_angles_3[0]
angle_B_3 = outgoing_angles_3[1]
angle_C_3 = outgoing_angles_3[2]

speed_A_3 = float(outgoing_speeds_3[0])
speed_B_3 = float(outgoing_speeds_3[1])
speed_C_3 = float(outgoing_speeds_3[2])

answer5 = round(speed_A_3, 1)
answer6 = round(speed_B_3, 1)
answer7 = round(speed_C_3, 1)


# ============================================================
# Problem 4
# Second three-ball elastic collision
# ============================================================

(
    initial_speed_4,
    outgoing_angles_4,
    outgoing_speeds_4
) = generate_pool_problem([26, 77, -61])

angle_A_4 = outgoing_angles_4[0]
angle_B_4 = outgoing_angles_4[1]
angle_C_4 = outgoing_angles_4[2]

speed_A_4 = float(outgoing_speeds_4[0])
speed_B_4 = float(outgoing_speeds_4[1])
speed_C_4 = float(outgoing_speeds_4[2])

answer8 = round(speed_A_4, 1)
answer9 = round(speed_B_4, 1)
answer10 = round(speed_C_4, 1)


# ============================================================
# Write the randomized questions to the HTML page
# ============================================================

Element("Q1a").write(
    f"1 a) A {weight_block_1}-lb block B starts from rest and "
    f"slides on a {weight_wedge_1}-lb wedge A. The wedge is "
    f"supported by a frictionless horizontal surface, and its "
    f"inclined surface makes an angle of {wedge_angle_1}° with "
    f"the horizontal. Neglecting friction, determine the magnitude "
    f"of the velocity of B relative to A [ft/s] after B has slid "
    f"{clean_number(slide_distance_1)} ft down the inclined "
    f"surface. Round to the nearest tenth."
)

Element("Q1b").write(
    f"1 b) For the {weight_block_1}-lb block and "
    f"{weight_wedge_1}-lb wedge described in part 1 a, calculate "
    f"the corresponding magnitude of the velocity of wedge A "
    f"[ft/s]. Round to the nearest tenth."
)

Element("Q2a").write(
    f"2 a) A {weight_block_2}-lb block B is suspended from a "
    f"{clean_number(cord_length_2)}-ft cord attached to a "
    f"{weight_cart_2}-lb cart A. The cart may roll freely on a "
    f"frictionless horizontal track. Initially, the cord makes an "
    f"angle of {initial_angle_2}° with the downward vertical, and "
    f"the system is released from rest. Determine the magnitude of "
    f"the velocity of cart A [ft/s] as B passes directly under the "
    f"cord attachment point. Round to the nearest tenth."
)

Element("Q2b").write(
    f"2 b) For the {weight_block_2}-lb block and "
    f"{weight_cart_2}-lb cart described in part 2 a, calculate the "
    f"magnitude of the velocity of block B [ft/s] as B passes "
    f"directly under the cord attachment point. Round to the "
    f"nearest tenth."
)

Element("Q3a").write(
    f"3 a) In a game of pool, three balls A, B, and C have "
    f"identical masses. Ball A initially moves along the positive "
    f"x-axis at {initial_speed_3} ft/s, while balls B and C are at "
    f"rest. After a perfectly elastic collision, ball A moves "
    f"{direction_description(angle_A_3)}, ball B moves "
    f"{direction_description(angle_B_3)}, and ball C moves "
    f"{direction_description(angle_C_3)}. Neglect friction. "
    f"Determine the magnitude of the velocity of ball A [ft/s]. "
    f"Round to the nearest tenth."
)

Element("Q3b").write(
    f"3 b) For the perfectly elastic collision described in "
    f"part 3 a, determine the magnitude of the velocity of ball B "
    f"[ft/s]. Round to the nearest tenth."
)

Element("Q3c").write(
    f"3 c) For the perfectly elastic collision described in "
    f"part 3 a, determine the magnitude of the velocity of ball C "
    f"[ft/s]. Round to the nearest tenth."
)

Element("Q4a").write(
    f"4 a) In a second game of pool, three balls A, B, and C have "
    f"identical masses. Ball A initially moves along the positive "
    f"x-axis at {initial_speed_4} ft/s, while balls B and C are at "
    f"rest. After a perfectly elastic collision, ball A moves "
    f"{direction_description(angle_A_4)}, ball B moves "
    f"{direction_description(angle_B_4)}, and ball C moves "
    f"{direction_description(angle_C_4)}. Neglect friction. "
    f"Determine the magnitude of the velocity of ball A [ft/s]. "
    f"Round to the nearest tenth."
)

Element("Q4b").write(
    f"4 b) For the perfectly elastic collision described in "
    f"part 4 a, determine the magnitude of the velocity of ball B "
    f"[ft/s]. Round to the nearest tenth."
)

Element("Q4c").write(
    f"4 c) For the perfectly elastic collision described in "
    f"part 4 a, determine the magnitude of the velocity of ball C "
    f"[ft/s]. Round to the nearest tenth."
)


# ============================================================
# Connect Python to the HTML elements
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
    Element("Question10")
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
    Element("outputDiv10")
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
    answer10
]


# ============================================================
# Answer checking
# ============================================================

def check_answer(question_index):
    """
    Check one submitted answer and update its score.
    """
    entered_text = inputs[question_index].value.strip()
    output = outputs[question_index]
    correct_answer = float(answers[question_index])

    output.clear()

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

    # Accept equivalent numeric entries such as 2, 2.0, and 2.00.
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
# Individual question-submit functions
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


# ============================================================
# Clear and final-submission functions
# ============================================================

def clear(*args, **kwargs):
    """
    Clear the answer inputs, feedback messages, final message,
    and recorded scores.
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
    Verify that all questions were submitted, then calculate and
    display the student's grade.
    """
    name = Element("student-name").value.strip()
    out_final = Element("outputFinal")

    out_final.clear()

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