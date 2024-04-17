import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice, randint
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particle import AnimationPlayer
from magic import MagicPlayer
from upgrade import Upgrade
from npc import NPC
from dialogue_box import DialogueBox

class Level:
    def __init__(self):

        # get the display surface
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False
        self.level_active = False
        
        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        #sprite setup
        self.create_map()

        # user interface
        self.ui = UI()
        self.upgrade = Upgrade(self.player)

        # dialogue box
        self.dialogue_box = DialogueBox()

        # particles
        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)

    def create_map(self):
        layout = {
                  'boundary': import_csv_layout('../map/map_FloorBlocks.csv'),
                  'grass': import_csv_layout('../map/map_Grass.csv'),
                  'object': import_csv_layout('../map/map_Objects.csv'),
                  'entities': import_csv_layout('../map/map_Entities.csv')
        }
        graphics = {
                    'grass' : import_folder('../graphics/grass'),
                    'objects': import_folder('../graphics/objects')
        }
        for style,layout in layout.items():
            for row_index,row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacle_sprites],'invisible')
                        if style == 'grass':
                            # create a grass tile
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y),
                                 [self.visible_sprites,self.obstacle_sprites,self.attackable_sprites],
                                 'grass',
                                 random_grass_image)
                        if style == 'object':
                            # create an object tile
                            surf = graphics['objects'][int(col)]
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)
                        if style == 'entities':
                            if col == '394':
                                self.player = Player(
                                    (x,y),
                                    [self.visible_sprites],
                                    self.obstacle_sprites,
                                    self.create_attack,
                                    self.destroy_attack,
                                    self.create_magic)
                                print(x,y)
                            else:
                                if col == '390':
                                    monster_name = 'bamboo'
                                elif col == '391':
                                    monster_name = 'spirit'
                                elif col == '392':
                                    monster_name = 'raccoon'
                                else:
                                    monster_name = 'squid'
                                Enemy(monster_name,
                                      (x,y),
                                      [self.visible_sprites,self.attackable_sprites],
                                      self.obstacle_sprites,
                                      self.damage_player,
                                      self.trigger_death_particles,
                                      self.add_xp)
        self.npc1 = NPC((1183,2275),[self.visible_sprites,self.obstacle_sprites],self.obstacle_sprites,self.talk_to_npc)

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

    def create_magic(self,style,strength,cost):
        if style == 'heal':
            self.magic_player.heal(self.player,strength,cost,[self.visible_sprites])
        if style == 'flame':
            self.magic_player.flame(self.player,cost,[self.visible_sprites,self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
            self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprite = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
                if collision_sprite:
                    for target_sprite in collision_sprite:
                        if target_sprite.sprite_type == 'grass':
                            pos = target_sprite.rect.center
                            offset = pygame.math.Vector2(0,75)
                            for leaf in range(randint(3,6)):
                                self.animation_player.create_grass_particles(pos-offset,[self.visible_sprites])
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(self.player,attack_sprite.sprite_type)
    
    #TODO: add talking to npc
    def talk_to_npc(self):
        # check if the distance is close enough
        if self.npc1.get_distance_from_player(self.player)[0] <= self.npc1.notice_radius and self.player.talking:
            pass

    def damage_player(self,amount,attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            self.animation_player.create_particles(attack_type,self.player.rect.center,[self.visible_sprites])
            self.check_player_death(self.player)

    def check_player_death(self,player):
        if self.player.health <= 0:
            self.level_active = False
            self.player.health = 100
            self.player.stats = {'health': 100, 'energy': 60, 'attack': 10, 'magic': 4, 'speed': 5}
            self.player.upgrade_cost = {'health': 100, 'energy': 100, 'attack': 100, 'magic': 100, 'speed': 100}
            self.player.health = self.player.stats['health']
            self.player.energy = self.player.stats['energy']
            self.player.exp = 200
            self.player.speed = self.player.stats['speed']
            self.player.hitbox.x = 2112 
            self.player.hitbox.y = 1344

    def trigger_death_particles(self,pos,particle_type):
        self.animation_player.create_particles(particle_type,pos,self.visible_sprites)

    def add_xp(self,amount):
        self.player.exp += amount

    def toggle_menu(self):
        self.game_paused = not self.game_paused

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.ui.display(self.player)
        if self.game_paused:
            self.upgrade.display()
        elif self.player.talking:
            # if (self.dialogue_box.npc_dialogue_index < len(self.dialogue_box.npc_dialogue)) and (self.dialogue_box.player_dialogue_index <= len(self.dialogue_box.player_dialogue)):
            #     self.dialogue_box.display(self.player)
            #     keys = pygame.key.get_pressed()
            #     if keys[pygame.K_RETURN] and self.player.can_switch_speaker:
            #         if self.player.is_speaking:
            #             self.dialogue_box.player_dialogue_index += 1
            #         else:
            #             self.dialogue_box.npc_dialogue_index += 1
            #     elif keys[pygame.K_ESCAPE]:
            #         self.dialogue_box.player_dialogue_index = 0
            #         self.dialogue_box.npc_dialogue_index = 0
            # else:
            #     self.dialogue_box.npc_dialogue_index = 0
            #     self.dialogue_box.player_dialogue_index = 0
            #     # self.player.is_speaking = False
            #     self.player.talking = False
            self.dialogue_box.display(self.player,self.npc1)
            self.npc1.update_talking()
            self.player.update_talking()
        else:
            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player)
            self.player_attack_logic()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surf = pygame.image.load('../graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
    
    def custom_draw(self,player):
        
        #getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

    def enemy_update(self,player):
        enemy_sprite = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprite:
            enemy.enemy_update(player)
