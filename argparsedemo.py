import argparse

def main():
    print("Time for a big glass of", args.drink)
    print("Time for a big plate of", args.f)

if __name__ == "__main__":
    #create a parser
    parser= argparse.ArgumentParser(description="Parameters for accessing the GOT API.")

    # teach it what arguments you are going to accept
    parser.add_argument("-d", "--drink",required=True, type=str, default="water", help="What you drinkin'?")
    parser.add_argument("-f", type=str, default="bread", help="What you eatin'?")

    args=parser.parse_args()

    main()
