import pygame
from settings import *
from debug import debug

class DialogueBox:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(DIALOGUE_BOX_FONT, DIALOGUE_BOX_FONT_SIZE)

        self.dialogue_box_rect = pygame.Rect(250,550,DIALOGUE_BOX_WIDTH,DIALOGUE_BOX_HEIGHT)

        self.current_speaker = None

        self.player_dialogue = ["Hello there!","*Lightsaber turning on*","Your move?"]
        self.player_dialogue_index = 0
        self.npc_dialogue = ["General Kenobi! *laughing* You are a bold one","Back away! I will deal with this jedi slime myself","You fool! I have been trained in your jedi arts by Count Dooku!"]
        self.npc_dialogue_index = 0
        self.input_text = ""
        self.touching = False
        self.touch_time = None
        self.chat = "Player: "
        self.text = ""

    def get_current_speaker(self,player):
        if player.is_speaking:
            self.current_speaker = "Player"
        else:
            self.current_speaker = "NPC"
    
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.touching:
            if current_time - self.touch_time > 100:
                self.touching = False

    def display(self,player,npc,automated=False):
        pygame.draw.rect(self.display_surface,DIALOGUE_BOX_COLOR,self.dialogue_box_rect)
        self.get_current_speaker(player)
        text_surf = self.font.render(self.current_speaker,False,TEXT_COLOR)
        x = self.dialogue_box_rect.x + 10
        y = self.dialogue_box_rect.y + 10
        text_rect = text_surf.get_rect(topleft=(x,y))
        self.display_surface.blit(text_surf,text_rect)
        if automated:
            if self.current_speaker=="Player":
                text_surf = self.font.render(self.player_dialogue[self.player_dialogue_index],False,TEXT_COLOR)
                x = self.dialogue_box_rect.x + 10
                y = self.dialogue_box_rect.y + 50
                text_rect = text_surf.get_rect(topleft=(x,y))
                self.display_surface.blit(text_surf,text_rect)
                # self.player_dialogue_index += 1
            else:
                text_surf = self.font.render(self.npc_dialogue[self.npc_dialogue_index],False,TEXT_COLOR)
                x = self.dialogue_box_rect.x + 10
                y = self.dialogue_box_rect.y + 50
                text_rect = text_surf.get_rect(topleft=(x,y))
                self.display_surface.blit(text_surf,text_rect)
                # self.npc_dialogue_index += 1
        else:
            if self.current_speaker=="Player":
                # takes an input text from the player
                keys = pygame.key.get_pressed()
                if keys[pygame.K_BACKSPACE] and not self.touching:
                    self.input_text = self.input_text[:-1]
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_a] and not self.touching:
                    self.input_text += "A"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_b] and not self.touching:
                    self.input_text += "B"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_c] and not self.touching:
                    self.input_text += "C"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_d] and not self.touching:
                    self.input_text += "D"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_e] and not self.touching:
                    self.input_text += "E"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_f] and not self.touching:
                    self.input_text += "F"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_g] and not self.touching:
                    self.input_text += "G"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_h] and not self.touching:
                    self.input_text += "H"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_i] and not self.touching:
                    self.input_text += "I"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_j] and not self.touching:
                    self.input_text += "J"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_k] and not self.touching:
                    self.input_text += "K"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_l] and not self.touching:
                    self.input_text += "L"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_m] and not self.touching:
                    self.input_text += "M"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_n] and not self.touching:
                    self.input_text += "N"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_o] and not self.touching:
                    self.input_text += "O"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_p] and not self.touching:
                    self.input_text += "P"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_q] and not self.touching:
                    self.input_text += "Q"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_r] and not self.touching:
                    self.input_text += "R"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_s] and not self.touching:
                    self.input_text += "S"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_t] and not self.touching:
                    self.input_text += "T"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_u] and not self.touching:
                    self.input_text += "U"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_v] and not self.touching:
                    self.input_text += "V"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_w] and not self.touching:
                    self.input_text += "W"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_x] and not self.touching:
                    self.input_text += "X"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_y] and not self.touching:
                    self.input_text += "Y"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_z] and not self.touching:
                    self.input_text += "Z"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_SPACE] and not self.touching:
                    self.input_text += " "
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_EXCLAIM] and not self.touching:
                    self.input_text += "!"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_QUOTE] and not self.touching:
                    self.input_text += "'"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_QUESTION] and not self.touching:
                    self.input_text += "?"
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_QUOTEDBL] and not self.touching:
                    self.input_text += '"'
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_PERIOD] and not self.touching:
                    self.input_text += "."
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_COMMA] and not self.touching:
                    self.input_text += ","
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                elif keys[pygame.K_RETURN] and not self.touching:
                    self.chat += self.input_text
                    self.chat += "\nMaria:"
                    self.input_text = ""
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                    self.chat,self.text = npc.complete_dialogue(self.chat)

                # for event in pygame.event.get():
                #     if event.type == pygame.KEYDOWN:
                #         if event.key == pygame.K_BACKSPACE:
                #             self.input_text = self.input_text[:-1]
                #         else:
                #             self.input_text += event.unicode

                text_surf = self.font.render(self.input_text,False,TEXT_COLOR)
                x = self.dialogue_box_rect.x + 10
                y = self.dialogue_box_rect.y + 50
                text_rect = text_surf.get_rect(topleft=(x,y))
                self.display_surface.blit(text_surf,text_rect)
                self.cooldowns()
            else:
                text_surf = self.font.render(self.text,False,TEXT_COLOR)
                x = self.dialogue_box_rect.x + 10
                y = self.dialogue_box_rect.y + 50
                text_rect = text_surf.get_rect(topleft=(x,y))
                self.display_surface.blit(text_surf,text_rect)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN] and not self.touching:
                    self.chat += "\nPlayer:"
                    # print(self.chat)
                    # print(npc.relationship_with_player)
                    self.touching = True
                    self.touch_time = pygame.time.get_ticks()
                self.cooldowns()
