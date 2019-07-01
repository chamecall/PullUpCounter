import cv2


class Drawer:
    """Class performing simple drawing tasks."""
    YELLOW_COLOR = (0, 255, 255)
    RED_COLOR = (0, 0, 255)
    BLUE_COLOR = (255, 0, 0)
    GREEN_COLOR = (0, 255, 0)
    BLACK_COLOR = (0, 0, 0)
    WHITE_COLOR = (255, 255, 255)
    ORANGE_COLOR = (16, 108, 168)
    DARK_RED_COLOR = (1, 1, 75)
    PURPLE_COLOR = (120, 5, 120)

    DEFAULT_FONT_THICKNESS = 2
    DEFAULT_LINE_THICKNESS = 3
    DEFAULT_COLOR = YELLOW_COLOR

    def __init__(self):
        pass

    @staticmethod
    def draw_skeleton(frame, points, pose_pairs, line_color=DEFAULT_COLOR, circle_color=RED_COLOR, radius=8,
                      line_thickness=DEFAULT_LINE_THICKNESS):

        for pair in pose_pairs:
            part_a = pair[0]
            part_b = pair[1]

            if points[part_a] and points[part_b]:
                cv2.line(frame, points[part_a], points[part_b], line_color, line_thickness, lineType=cv2.LINE_AA)
                Drawer.draw_point(frame, points[part_a], circle_color, radius)
                Drawer.draw_point(frame, points[part_b], circle_color, radius)

    @staticmethod
    def draw_numbered_joints(frame, points: dict, needed_points: dict, text_color=RED_COLOR,
                             thickness=DEFAULT_FONT_THICKNESS, font_scale=1):
        for joint, point in points.items():
            if not point:
                break
            joint_number = needed_points[joint]
            cv2.putText(frame, f'{joint_number}', (point[0], point[1]), cv2.FONT_HERSHEY_SIMPLEX, font_scale,
                        text_color, thickness,
                        lineType=cv2.LINE_AA)

    @staticmethod
    def print_message(frame, message, x, y, text_color=RED_COLOR, thickness=DEFAULT_FONT_THICKNESS, font_scale=1):
        cv2.putText(frame, message, (x, y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, text_color, thickness,
                    lineType=cv2.LINE_AA)

    @staticmethod
    def draw_point(frame, point, color, radius):
        cv2.circle(frame, (point[0], point[1]), radius, color, thickness=-1, lineType=cv2.FILLED)

    @staticmethod
    def print_message_with_text_edging(frame, x, y, value, border_size=5, thickness=DEFAULT_FONT_THICKNESS,
                                       text_color=RED_COLOR, border_color=DEFAULT_COLOR):
        Drawer.print_message(frame, f'{value}', x, y, text_color=border_color, thickness=thickness + border_size,
                             font_scale=1.1)
        Drawer.print_message(frame, f'{value}', x, y, thickness=thickness, text_color=text_color,
                             font_scale=1.1)
