# CC_TARGET=sample
# CC_FLAGS=-ggdb
# CC_COMP_OBJ=-c
# CC=gcc $(CC_FLAGS)
#
# sample-run: sample-prepare sample-binary
# 	#gdb $(CC_TARGET)
# 	./$(CC_TARGET)
#
# sample-prepare:
# 	python3 c_generate.py
# 	$(CC) $(CC_COMP_OBJ) -o bokuro/path.o bokuro/path.c
#
# sample-binary:
# 	$(CC) -o $(CC_TARGET) bokuro/path.o sample.c

test-run: compile
	python3 sample.py

compile:
	python3 setup.py build_ext --inplace
	python3 setup.py install --user
