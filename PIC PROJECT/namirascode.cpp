#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int choice;
    int gold = 50;
    int bet;
    int playerRoll, houseRoll;
    int mc, chh, ch, jk;
    int code=0;

    srand(time(0));

    printf("=== THE STRANDED ISLAND ===\n");
    printf("This is your narrator speaking,my name need not be shared.I will be assisting you and presenting you with choices that either make or break your journey\n ");
    printf("Choose your player and enter number for the player\n");
printf("1. Aman\t2. Natalie\t3. Yuki\n");

scanf("%d", &mc);

if (mc == 1) {
    printf("\nYou have chosen Aman\n");
    printf("He is a native Indian from Bihar, aged 47 and an early retired Navy officer.\n");
    printf("(He was injured in duty and now has weak knees)\n");
}
else if (mc == 2) {
    printf("\nYou have chosen Natalie\n");
    printf("She is native to Ukraine, aged 32 and an overworked nurse.\n");
    printf("(She has a blind spot in her right eye)\n");
}
else if (mc == 3) {
    printf("\nYou have chosen Yuki\n");
    printf("She is a dynamic young citizen of Japan, aged 25, studying Botany.\n");
    printf("(She suffers from seasonal depression)\n");
}
else {
    printf("\nKindly enter a valid number assigned to the characters.\n");
    return 0;
}
    
    printf("You start your journey with %d gold coins.\n\n", gold);

    printf("A hurricane in your village caused a blackout. ");
    printf("You were helping the villagers is the last thing you remember. ");
    printf("You are now stranded on an unknown island.\n\n");

    printf("Press 1 to continue, 2 to exit: ");
    scanf("%d", &mc);

    if (mc != 1) {
        printf("GAME OVER\n");
        return 0;
    }

    printf("\nYou walk around and spot a shady tavern. What do you do?\n");
    printf("1. Enter the tavern\n");
    printf("2. Continue your journey\n");
    printf("Enter choice: ");
    scanf("%d", &choice);

    /* ================= TAVERN PATH ================= */

    if (choice == 1) {

        printf("\nInside the tavern, a gentleman in a cloak approaches you.\n");
        printf("'Care to roll the dice? Double your gold!' he says suspiciously.\n");

        while (1) {
            printf("\nYou have %d gold.\n", gold);
            printf("Enter bet amount (0 to quit gambling): ");
            scanf("%d", &bet);

            if (bet == 0)
                break;

            if (bet > gold || bet < 0) {
                printf("Invalid bet!\n");
                continue;
            }

            playerRoll = (rand() % 6) + 1;
            houseRoll = (rand() % 6) + 1;

            printf("You rolled: %d\n", playerRoll);
            printf("House rolled: %d\n", houseRoll);

            if (playerRoll > houseRoll)
                gold += bet;
            else if (playerRoll < houseRoll)
                gold -= bet;

            if (gold <= 0) {
                printf("You lost all your gold.\nGAME OVER.\n");
                return 0;
            }
        }

        printf("\nYou leave the tavern with %d gold.\n", gold);

        if (gold >= 100) {
            printf("With your fortune, you can buy anyone's trust.\n");
            printf("Woah, don't let your luck run out.... here is a secret code, use when required\n");
            printf("\n65579")

        ;}

        printf("You continue your journey...\n");
    }

    /* ================= BANDIT PATH ================= */

    printf("\nA bandit ambushes you on the road.\n");
    printf("What do you do?\n1. Fight\n2. Negotiate\n");
    scanf("%d", &chh);

    if (chh == 1) {
        printf("You're too weak from the hurricane.\nIf you have an extra life you may use it, type secret code for extra life.\n");
        scanf("%d",&code);
         if(code=65579)
        printf("You're a lucky one, aren't you? ");
        else (code!=65579);
       { printf("GAME OVER");
        return 0;}
    }

    else if (chh == 2) {

        printf("'What do you have to offer us?'\n");
        printf("1. Offer gold coins\n2. Stall\n");
        scanf("%d", &ch);

        if (ch == 1) {
            if (gold >= 50) {
                gold -= 50;
                printf("They take your gold and let you go.\n");
                printf("YOU SURVIVED.\n");
            } else {
                printf("Not enough gold.\nGAME OVER.\n");
            }
            return 0;
        }

        else if (ch == 2) {

            printf("Do you:\n1. Tell a joke\n2. Beg\n");
            scanf("%d", &jk);

            if (jk == 1) {
                int r = rand() % 2;

                if (r == 0)
                    printf("They liked your joke and decided to spare you.\nYOU SURVIVED.\n");
                else
                    printf("They hate the joke.\nGAME OVER.\n");
            }

            else
                printf("They see weakness.\nGAME OVER.\n");

            return 0;
        }
    }
    return 0;
}
