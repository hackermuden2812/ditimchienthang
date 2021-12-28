# keys = pygame.key.get_pressed()
        # if character_a.turn:                         
        #     bulletsA.append([bulletsA[count][0] + 5 * character_a.direction,500])
        #     count+=1
        #     for bullet in bulletsA[:]:
        #         if bullet[0] < 0:
        #             bulletsA.remove(bullet)
        #     for bullet in bulletsA:
        #         window.blit(bulletpicture, pygame.Rect(
        #             bullet[0], bullet[1], 0, 0))

        #     character_a.turn = False
        #     character_b.turn = True
        # elif character_b.turn:                         
        #     bulletsB.append([bulletsB[count][0] + 5 * character_a.direction,500])
        #     count+=1
        #     for bullet in bulletsB[:]:
        #         if bullet[0] < 0:
        #             bulletsB.remove(bullet)
        #     for bullet in bulletsB:
        #         window.blit(pygame.transform.flip(bulletpicture,True,False,(0,500)))
        #         window.blit(bulletpicture, pygame.Rect(
        #             bullet[0], bullet[1], 0, 0))
        #     character_a.turn = True
        #     character_b.turn = False