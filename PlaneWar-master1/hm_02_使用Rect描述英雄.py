import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)

print("主人公の起源 %d %d" % (hero_rect.x, hero_rect.y))
print("ヒーローサイズ %d %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size)
