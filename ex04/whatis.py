# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaoh <jaoh@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/11 15:22:26 by jaoh              #+#    #+#              #
#    Updated: 2026/10/11 15:41:37 by jaoh             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def main():
    """Print whether the integer argument is odd or even."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 1:
            return
        assert sys.argv[1].lstrip("-").isdigit(), "argument is not an integer"
        number = int(sys.argv[1])
        print("I'm Even." if number % 2 == 0 else "I'm Odd.")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
