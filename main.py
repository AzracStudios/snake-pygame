from config import *
from render import *

game = Game(Config.CELL_WIDTH, Config.GRID_ROWS)


def eval_highscore():
    current_high_score = 0

    with open("highscore.txt", "r") as f:
        raw = f.readlines()[0]
        current_high_score = max(int(raw), game.score)
        f.close()

    with open("highscore.txt", "w") as f:
        f.write(str(current_high_score))
        f.close()

    return current_high_score


def main():
    clock = pygame.time.Clock()
    generate_bg_cells_cache()

    direction = -1
    game_over = False

    static_rendered = False

    while True:
        clock.tick(Config.FPS)
        game_over = game.next(direction)

        if not game_over:
            if direction > -1:
                render_game(game)
                static_rendered = False

        else:
            Config.FPS = 200
            static_rendered = render_game_over(eval_highscore(),
                                               static_rendered)

        if direction == -1:
            Config.FPS = 200
            static_rendered = render_title(static_rendered)
        else:
            Config.FPS = 10
            static_rendered = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    direction = 0

                if event.key == pygame.K_a:
                    direction = 1

                if event.key == pygame.K_s:
                    direction = 2

                if event.key == pygame.K_d:
                    direction = 3

                if event.key == pygame.K_SPACE:
                    if game_over:
                        game.reset()

                        direction = -1
                        game_over = False
                        static_rendered = False
                        Config.FPS = 10
                        pygame.display.update()


if __name__ == "__main__":
    main()