from config import *


def generate_bg_cells_cache():
    for i in range(0, Config.GRID_ROWS):
        for j in range(0, Config.GRID_ROWS):
            if (i + j) % 2 == 0:
                Config.BG_CELLS_CACHE.append(
                    pygame.Rect(i * Config.CELL_WIDTH, j * Config.CELL_WIDTH,
                                Config.CELL_WIDTH, Config.CELL_WIDTH))


def render_game(game):
    Config.SCREEN.fill(Config.CHECKER_LIGHT)
    ## SCORE TEXT ##
    score_text = Config.FONT_S.render(f"Score: {game.score}", True,
                                      Config.TEXT)

    ## BG_CELLS
    for cell in Config.BG_CELLS_CACHE:
        pygame.draw.rect(Config.SCREEN, Config.CHECKER_DARK, cell)

    ## APPLE ##
    apple_rect = pygame.Rect(game.apple.x * game.board_res,
                             game.apple.y * game.board_res, Config.CELL_WIDTH,
                             Config.CELL_WIDTH)

    pygame.draw.rect(Config.SCREEN, Config.APPLE, apple_rect)

    ## SNAKE ##
    piece = game.snake.head

    while piece:
        pos = piece.get_pos()

        ## CHECK IF SNAKE HITS ITgame ##
        if piece != game.snake.head:
            if game.snake.hit_self(piece):
                game.game_over = True
                break

        ## RENDER SNAKE ##
        snake_rect = pygame.Rect(pos[0] * game.board_res,
                                 pos[1] * game.board_res, Config.CELL_WIDTH,
                                 Config.CELL_WIDTH)
        pygame.draw.rect(
            Config.SCREEN, Config.SNAKE_HEAD
            if piece.get_type() == "head" else Config.SNAKE_BODY, snake_rect)
        piece = piece.next_piece

    Config.SCREEN.blit(score_text, (10, 10))
    pygame.display.update()


def render_game_over(score, rendered):
    if rendered: return True
    game_over_text = Config.FONT_L.render("GAME OVER!", True, Config.TEXT)
    restart_text = Config.FONT_S.render("Press space to restart", True,
                                        Config.TEXT)
    high_score_text = Config.FONT_S.render(f"Highscore: {str(score)}", True,
                                           Config.TEXT)

    Config.SCREEN.blit(
        game_over_text,
        ((Config.WIN_WIDTH / 2 - (game_over_text.get_width() / 2)),
         (Config.WIN_WIDTH / 2 - (game_over_text.get_height() / 2) -
          restart_text.get_height() - 10 - high_score_text.get_height())))

    Config.SCREEN.blit(
        restart_text,
        ((Config.WIN_WIDTH / 2 - (restart_text.get_width() / 2)),
         (Config.WIN_WIDTH / 2 -
          (restart_text.get_height() / 2) - 5 - high_score_text.get_height())))

    Config.SCREEN.blit(
        high_score_text,
        ((Config.WIN_WIDTH / 2 - (high_score_text.get_width() / 2)),
         (Config.WIN_WIDTH / 2 - (high_score_text.get_height() / 2))))

    pygame.display.update()
    return True


def render_title(rendered):
    if rendered: return True

    ## BG GRID ##
    Config.SCREEN.fill(Config.CHECKER_LIGHT)

    for cell in Config.BG_CELLS_CACHE:
        pygame.draw.rect(Config.SCREEN, Config.CHECKER_DARK, cell)

    ## TEXT ##
    title_text = Config.FONT_L.render("Snake", True, Config.TEXT)
    dir_text = Config.FONT_S.render("Move to start", True, Config.TEXT)

    Config.SCREEN.blit(
        title_text,
        ((Config.WIN_WIDTH / 2 - (title_text.get_width() / 2)),
         (Config.WIN_WIDTH / 2 -
          (title_text.get_height() / 2) - dir_text.get_height() - 2)))

    Config.SCREEN.blit(dir_text,
                       ((Config.WIN_WIDTH / 2 - (dir_text.get_width() / 2)),
                        (Config.WIN_WIDTH / 2 - (dir_text.get_height() / 2))))

    pygame.display.update()

    return True