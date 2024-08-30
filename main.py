from chess.move_generator import MoveGenerator
from chess.evaluator import Evaluator
from chess.search import Search
from chess.uci_handler import UCIHandler

def main():
    move_generator = MoveGenerator()
    evaluator = Evaluator()
    search = Search(move_generator, evaluator)
    uci_handler = UCIHandler(search, move_generator)

    while True:
        try:
            command = input().strip()
            if command == "quit":
                break
            uci_handler.handle_command(command)
        except EOFError:
            break  # End loop if there's no more input

if __name__ == "__main__":
    main()
