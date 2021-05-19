# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 15:08:35 2021

@author: kalya
"""
user1 = input("Player 1,Enter your choice rock/paper/scissor: ")
user2 = input("Player2,Enter your choice rock/paper/scissor:")
def rock_paper_scissor(player_1, player_2):
    a_list = ["rock","paper","scissor"]
    
    while player_1 not in a_list or player_2 not in a_list :
        print("Invalid input!")
        player_1 = input("player1, Enter rock/paper/scissor:")
        player_2 = input("player2, Enter rock/paper/scissor:")
    
    while player_1 == player_2 :
        print("Nobody wins:")
        player_1 = input("player1,  Enter rock/paper/scissor:")
        player_2 = input("player2, Enter rock/paper/scissor:")
    
    if player_1 == "rock" and player_2 == "scissor":
        print("Player_1 wins! Do you want play again?")
    
    if player_1 == "rock" and player_2 == "paper":
        print("player_2 wins!")
        
    if player_1 == "scissor" and player_2 == "paper" :
        print("player1 wins!")
        
rock_paper_scissor(user1, user2) 