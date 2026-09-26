#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int choice;
    int gold = 50;
    int bet;
    int playerRoll, houseRoll;
    system("cls");


    srand(time(0));

    printf("=== THE LOST KINGDOM ===\n");
    printf("You start your journey with %d gold coins.\n\n", gold);

    printf("You arrive at a small tavern in the forest.\n");
    printf("What do you want to do?\n");
    printf("1. Enter the tavern\n");
    printf("2. Continue your journey\n");
    printf("Enter choice: ");
    scanf("%d", &choice);

    if (choice == 1) {
        printf("\nInside the tavern, a shady gambler approaches you.\n");
        printf("'Care to roll the dice? Double your gold!'\n");

        while (1) {
            printf("\nYou have %d gold.\n", gold);
            printf("Enter bet amount (0 to quit gambling): ");
            scanf("%d", &bet);

            if (bet == 0) {
                break;
            }

            if (bet > gold || bet < 0) {
                printf("Invalid bet!\n");
                continue;
            }

            playerRoll = (rand() % 6) + 1;
            houseRoll = (rand() % 6) + 1;

            printf("You rolled: %d\n", playerRoll);
            printf("House rolled: %d\n", houseRoll);

            if (playerRoll > houseRoll) {
                printf("You win!\n");
                gold += bet;
            } else if (playerRoll < houseRoll) {
                printf("You lose!\n");
                gold -= bet;
            } else {
                printf("It's a tie! No gold lost.\n");
            }

            if (gold <= 0) {
                printf("\nYou lost all your gold...\n");
                printf("The gambler laughs as you're thrown out.\n");
                printf("GAME OVER.\n");
                return 0;
            }
        }

        printf("\nYou leave the tavern with %d gold.\n", gold);

        if (gold >= 100) {
            printf("With your fortune, you buy legendary armor.\n");
            printf("You defeat the Dragon King easily.\n");
            printf("YOU WIN!\n");
        } else {
            printf("You continue your journey...\n");
            printf("Without enough gold, you struggle in battle.\n");
            printf("GAME OVER.\n");
        }

    } else if (choice == 2) {
        printf("\nYou ignore the tavern and continue walking.\n");
        printf("A bandit ambushes you on the road.\n");
        printf("Without supplies, you cannot fight.\n");
        printf("GAME OVER.\n");
    } else {
        printf("\nInvalid choice.\n");
    }

    return 0;
}
