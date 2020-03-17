.PHONY: help bin

BIN_DIR=bin
BIN_FILE=$(BIN_DIR)/cipher.sh
CLEAN_FILE=$(BIN_DIR)/clean.sh

# Show help docstring if 'make' or 'make help' are used
.DEFAULT: help
help:
	@echo "make bin"
	@echo "       Copy binary file to root directory."
	@echo "make clean"
	@echo "       Clean binary file from root directory and any __pycache__ files."

bin: $(BIN_FILE)
	cp $(BIN_FILE) ./
	@echo "----------------------------------------------------"
	@echo "BINARY FILE READY TO EXECUTE: "
	@echo "		RUN ./cipher.sh"
	@echo "----------------------------------------------------"

clean: $(CLEAN_FILE)
	@rm -f ./cipher.sh
	@bash $(CLEAN_FILE)
	@echo "Cleaned working directory."
