def move(screen, icon: str = "", x: int = playerY, y: int = playerX) -> None:
    """Draw on the screen

    Keyword Arguments:
        x {int} -- move on x-axis (default: {0})
        y {int} -- move on y-axis (default: {0})
    """
    screen.blit(icon, (x, y))


def boundaries(true, x: float):
    if (x > 800.0):
        x = 0
    elif (x < 0.0):
        x = 800
    return x
