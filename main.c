#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <unistd.h>

void update() {
    system("git pull origin master");
}

int main(int argc, char **argv) {
    while (true) {
        printf("Press [CTRL+C] to stop...");
        system("python3 bot.py");
        
        update();
	    sleep(1);
    }

    return 0;
}