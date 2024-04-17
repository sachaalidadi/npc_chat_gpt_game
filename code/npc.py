import pygame
from settings import *
from support import import_folder
from entity import Entity
from debug import *
import openai

openai.api_key = "ENTER YOUR API KEY HERE"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024, # max_tokens is 
        n=1,
        stop=None,
        temperature=0.5,
    )

    message=completions.choices[0].text
    return message

class NPC(Entity):
    def __init__(self,pos,groups,obstacle_sprites,talk_to_npc):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/npc1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.notice_radius = 200
        self.talk_to_npc = talk_to_npc
        self.relationship_with_player = 0
        self.must_follow_player = False
        self.status = 'idle'
    def get_distance_from_player(self,player):
        npc_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - npc_vec).magnitude()
        if distance > 0:
            direction = (player_vec - npc_vec).normalize()
        else:
            direction = pygame.math.Vector2(0,0)
        return distance,direction
    
    def get_status(self,player):
        if self.must_follow_player:
            self.status = "move"
        else:
            self.status = "idle"
    
    def actions(self,player):
        if self.status == "move":
            self.direction = self.get_distance_from_player(player)[1]
    
    def complete_dialogue(self,chat):
        text = generate_response(f"You are Maria an NPC in a video game, your job is to reply to the player talking to you. Be short in your reply. Here is the history of conversation, between you and the Player {chat}")
        chat += text
        #update the relationship with the player
        grade = generate_response(f"You are Maria an NPC in a video game, your job is to evaluate the relationship with the player. It is {self.relationship_with_player} right now. The number is between -2 and 2, -2 means you hate the player, 2 means you love the player. Here is the history of conversation, between you and the Player {chat}. Return only the number you chose.")
        self.relationship_with_player = int(grade)
        return chat,text
    def npc_update(self,player):
        self.get_status(player)
        self.actions(player)

    def update_talking(self):
        self.talk_to_npc()