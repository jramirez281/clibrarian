from src.search import search
from src.agent import synthesize

def main():
    print("Welcome to CLIbrarian. Type 'exit' to quit.\n")
    while True:
        query = input("Ask a question: ").strip()
        if query.lower() == "exit":
            print("Goodbye!")
            break
        if not query:
            continue
        print("\nSearching...\n")
        results = search(query)
        print("Synthesizing answer...\n")
        answer = synthesize(query, results)
        print(f"Answer:\n{answer}\n")

if __name__ == "__main__":
    main()
