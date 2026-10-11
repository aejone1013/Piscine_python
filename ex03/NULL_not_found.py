# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaoh <jaoh@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/11 15:22:23 by jaoh              #+#    #+#              #
#    Updated: 2026/10/11 15:41:39 by jaoh             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:
    """Print the type of a 'null-like' object; return 0, or 1 on error."""
    if isinstance(object, bool):
        print(f"Fake: {object} <class 'bool'>")
    elif object is None:
        print(f"Nothing: {object} <class 'NoneType'>")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: {object} <class 'float'>")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: {object} <class 'int'>")
    elif isinstance(object, str) and object == "":
        print("Empty: <class 'str'>")
    else:
        print("Type not Found")
        return 1
    return 0
