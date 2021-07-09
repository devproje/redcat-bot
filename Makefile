run_catbot: .object/main.o
	gcc -o run_catbot .object/main.o

.object/main.o: main.c
	mkdir .object/
	gcc -c -o .object/main.o main.c

clean_obj:
	rm -rf .object/

clean:
	rm -rf .object/ run_catbot