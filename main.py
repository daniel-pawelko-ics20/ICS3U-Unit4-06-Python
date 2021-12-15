#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Dec 2021
# RGB


def main():
    # main function for creating rbg program

    # process/output
    for red in range(256):
        for green in range(256):
            for blue in range(256):
                print(f"RGB({red},{green},{blue})")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
