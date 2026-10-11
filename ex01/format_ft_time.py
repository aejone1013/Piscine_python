# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaoh <jaoh@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/08 16:22:51 by jaoh              #+#    #+#              #
#    Updated: 2026/10/11 14:59:59 by jaoh             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from datetime import datetime

now = time.time()
print(f"Seconds since January 1, 1970: {now:,.4f} "
    f"or {now:.2e} in scientific notation")
print(datetime.now().strftime("%b %d %Y"))